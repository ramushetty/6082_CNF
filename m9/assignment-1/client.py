import socket


def main():

    host_name = socket.gethostname()
    port = 4040
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = socket.gethostbyname(host_name)
    s.connect((host_ip, port))
    print("Connected!\n")
    print("Welcome to 'Guess my number'")
    print("I'm thinking of a number between 1 and 50. Please guess the number")
    message = input("Enter your guess: Q for abort")
    while message != 'Q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print(data)
        val = data.split()
        if (val[0] == 'Correct' or val[0] == 'q'):
            s.send('Q'.encode())
            break
        message = input("Enter your guess: ")
    s.close()


if __name__ == '__main__':
    main()