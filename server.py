import socket
import sys

def main():
    if len(sys.argv) == 2:
        HOST = 'localhost'
        PORT = int(sys.argv[1])
    else:
        print("number of arguments has to be 2")
        return
    # HOST = 'localhost'        # Symbolic name meaning all available interfaces
    # PORT = 50007              # Arbitrary non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            # answer = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<content>"
            answer = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            
            file = open('example.html', mode = 'r')
            # # read all lines at once
            file_string = file.read()
            answer += file_string
            # # close the file
            file.close()
           
            # print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(bytes(answer, 'ascii'))

main()