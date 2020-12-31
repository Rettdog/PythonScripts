import threading
import socket

class User:
    def __init__(self, sock, addr, name="UNKNOWN"):
        self.sock, self.addr, self.id = sock, addr, name

class NonSockUser:
    def __init__(self, id='', addr='', name=''):
        if id == '':
            self.id = genId()
        self.addr = addr
        self.name = name
        self.status = True

class Server:
    def __init__(self, user, chats, contacts, port=8082):
        self.user = user
        self.chatDict = {chat.id: chat for chat in chats}
        self.contacts = contacts
        print('Setting up...')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Binding...')
        self.s.bind(('', port))
        self.s.listen()
        self.run = True

        self.users = []

        threading.Thread(target=self.mainloop, daemon=True).start()

    def mainloop(self):
        print('Accepting connections.')
        while self.run:
            clientsocket, address = self.s.accept()
            print(f"[INFO] Connection from {address} has been established.")
            self.users.append(User(clientsocket, address))
            threading.Thread(target=self.client, args=[self.users[-1]]).start()

    def initialize(self, user, data):
        global h
        if user.id == "UNKNOWN":
            stuff = data.split(",") # id, name
            # if stuff[0] in [i.name for i in self.users]:
            #     print(f"[WARN] {user.addr} username already taken.")
            #     user.sock.send(bytearray([6]))
            #     continue
            user.chatID, user.id, user.name = stuff[0], stuff[1], stuff[2]
            print(f"[INFO] {user.addr} initialized. ID is {user.id}, name is {user.name}")

            self.contacts[user.id] = NonSockUser(id=user.id, addr=user.addr[0], name=user.name)
            self.chatDict[user.chatID].messages += f"\n{user.name} has come online."

            msg = f'{self.user.id},HOST,{self.user.name}'
            user.sock.send(bytearray([1, len(msg)]))
            user.sock.send(msg.encode())

            msg = f'{self.chatDict[user.chatID].name}'
            user.sock.send(bytearray([4, len(msg)]))
            user.sock.send(msg.encode())

            for u in [i for i in self.users if i.id != user.id]:
                msg = f'{u.id},{u.addr},{u.name}'
                user.sock.send(bytearray([1, len(msg)]))
                user.sock.send(msg.encode())
                print(f"told {user.name} that {u.name} exists")
                msg = f'{user.id},{user.addr},{user.name}'
                u.sock.send(bytearray([1, len(msg)]))
                u.sock.send(msg.encode())
                print(f"told {u.name} that {user.name} exists")

    def client(self, user):
        while self.run:
            try:
                command = int.from_bytes(user.sock.recv(1), "little")
                header = int.from_bytes(user.sock.recv(1), "little")
                data = user.sock.recv(header).decode()

                if command == 1: # Client is telling us it has connected and sends credentials
                    self.initialize(user, data)

                elif command == 2: # Client is sending a message to a group
                    stuff = data.split(",") # group ID, timestamp, message
                    if stuff[0] in self.chatDict.keys():
                        self.chatDict[stuff[0]].history[int(stuff[1])] = (user.id, stuff[2])
                        self.chatDict[stuff[0]].messages += f'\n{user.name}: {stuff[2]}'
                        self.chatDict[stuff[0]].members[user.id] = self.contacts[user.id]
                        self.distribute(user, 2, f'{stuff[0]},{stuff[1]},{user.id},{stuff[2]}')
                        print(f'{user.name}: {stuff[2]}')
                    else:
                        print(f'User {user.id} aka {user.name} sent a message to a group that does not exist?')

            except ConnectionResetError:
                threading.Thread(target=self.inform, args=[user]).start()
                return
            except IndexError:
                print(f"[WARN] Received bad packets from {user.name}.")
            # except Exception as e:
            #     print(f"[ERR] [{user.addr}] {e}")
            #     self.users.remove(user)
            #     return
        print(f'Disconnecting from {user.addr}')

    def distribute(self, user, command, msg):
        for u in [i for i in self.users if i != user]:
            u.sock.send(bytearray([command, len(msg)]))
            u.sock.send(msg.encode())

    def inform(self, user):
        try:
            self.users.remove(user)
            print(f"[INFO] {user.id} aka {user.name} has left.")
            self.chatDict[user.chatID].messages += f"\n{user.name} has gone offline."
            user.sock.close()
            self.contacts[user.id].status = False
            for u in [i for i in self.users if i != user]:
                try:
                    u.sock.send(bytearray([3, len(user.id)]))
                    u.sock.send(user.id.encode())
                except ConnectionResetError:
                    self.inform(u)
        except ValueError:
            return
        except AttributeError:
            print(f'Unknown client from address {user.addr} disconnected.')
