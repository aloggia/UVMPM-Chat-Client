from socket import *

# TODO: Function to list online users, function to send a message, function to close connection

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server_name = input("Enter server name: ")
    server_port = 1200
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    # Will need to modify
    client_socket.send("HELLO\n".encode())
    response_message = client_socket.recv(1024)
    if response_message == "HELLO":
        # Put into it's own function
        username = input("Enter student ID/Username: ")
        password = input("Enter password: ")
        client_socket.send(("AUTH:" + username + ":" + password).encode())
    else:
        print("Error connecting to server")
