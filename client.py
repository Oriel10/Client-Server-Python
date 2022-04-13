import socket
import sys



def main():
    if len(sys.argv) == 3:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
    else:
        print("number of arguments has to be 3")
        return
    request_data = "GET / HTTP/1.1\r\nHost: " + HOST + "\r\n\r\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # s.sendall(b'Hello, world')
        
        s.sendall(bytes(request_data, 'ascii'))
        recieved_data = s.recv(1024)
    print(recieved_data)

main()