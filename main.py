from socket import *

# TODO: Function to list online users, function to send a message, function to close connection


def list_users(client_socket):
    # Need to craft message to server asking for the user list
    client_socket.send("List\n".encode())
    users = client_socket.recv(1024)[7:-1].decode()
    user_list = users.split(",")
    for user in user_list:
        print(user)


def send_message(client_socket):
    user_to_send_to = input("Enter user to message: ")
    message_to_send = input("Enter message: ")
    complete_message = "To:" + user_to_send_to + ":" + message_to_send + "\n"
    client_socket.send(complete_message.encode())


def sign_in(client_socket):
    username = input("Enter student ID/Username: ")
    password = input("Enter password: ")
    client_socket.send(("AUTH:" + username + ":" + password + "\n").encode())
    while client_socket.recv(1024)[:-1].decode() == "AUTHNO":
        username = input("Enter student ID/Username: ")
        password = input("Enter password: ")
        client_socket.send(("AUTH:" + username + ":" + password + "\n").encode())


# List online users - server returns a comma deliminated list - list comprehension to display each name on it's own line

# Send a message - Should be fairly simple

# Exit - Close the connection

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server_name = '132.198.11.12'
    server_port = 12000
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    # Will need to modify
    client_socket.send("HELLO\n".encode())
    response_message = client_socket.recv(1024)[:-1].decode()
    print(response_message)
    if response_message == "HELLO":
        # Put into it's own function
        # Needs error correcting
        if client_socket.recv(1024)[:-1].decode() == "AUTHYES":
            # Put while loop here
            print("Welcome " + username)
            list_users(client_socket)
    else:
        print("Error connecting to server")
