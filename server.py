import socket
import threading
from BTC_rate import rate
from w_r_json import read_rate

host = 'localhost'
port = 5001

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("== Server Started ==")
thread_rate = threading.Thread(target=rate)
thread_rate.start()
while True:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
            print(f'=={addr[0]}=={addr[1]}==', end="")
            print(data.decode('utf-8'))
            s.sendto(data, addr)
        else:
            data_req = data.decode('utf-8').split(" ::: ")
            print(data_req)
            if data_req[1] in ['exmo', 'binance', 'bittrex']:
                data_rate = read_rate(data_req[1])
                s.sendto(data_rate.encode('utf-8'), addr)
            else:
                s.sendto("ERROR".encode('utf-8'), addr)
    except:
        print('\n == Server Stoped ==')
        break
thread_rate.join()
s.close()
