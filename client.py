import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    data = MESSAGE.encode()
    sock.sendto(data, server)
    print(f'Send data: {data.decode()} to server: {server[0]}')
    sock.recvfrom(1024)
    sock.close()


if __name__ == '__main__':
    run_client(UDP_IP, UDP_PORT)
