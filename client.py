import socket
import time
import threading

shutdown = True
join = True


def receving(sock):
    while shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode('utf-8'))
                time.sleep(0.2)
        except:
            pass


host = 'localhost'
port = 0

server = ('localhost', 5001)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
name_client = input("Name = ")
rt = threading.Thread(target=receving, args=(s,))
rt.start()
while shutdown:
    if join:
        s.sendto((f'{name_client} => join to cryptocurrency').encode('utf-8'), server)
        join = not join
    else:
        try:
            message = input()
            if message:
                st = f'{name_client} ::: {message}'
                s.sendto(st.encode('utf-8'), server)
            time.sleep(0.2)
        except:
            s.sendto((f'{name_client} ::: LEFT CHAT').encode('utf-8'), server)
            shutdown = not shutdown
rt.join()
s.close()
