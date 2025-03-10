"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    host = socket.gethostbyname("172.20.10.13")  # Get the hostname
    port = 12345  # Connect to the same port as the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    client_socket.connect((host, port))  # Connect to the server
    
    # TODO: Get user input and send it to the server using your TCP socket
    message = input("Enter message: ")
    client_socket.send(message.encode())  # Send data to the server
    
    # TODO: Receive a response from the server and close the TCP connection
    data = client_socket.recv(256)  # Receive data from the server
    print("I got your message")

    client_socket.close()  # Close the socket
    pass


if __name__ == '__main__':
    main()