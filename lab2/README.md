# Lab 2

## Team Members
- Tina Habibi
- Faith Klein

## Lab Question Answers

Question 1: How did the reliability of UDP change when you added 50% loss to your local
environment? Why did this occur?
    UDP did not deliver all the messages and dropped some due to congestion. 
    This occurs because UDP prioritizes speed over realiability.

Question 2: How did the reliability of TCP change? Why did this occur? 
    TCP remained reliable and delivered all messages but with much longer delay.
    This is because TCP is a reliable protocol and prioritizes sending all messages over speed. 

Question 3: How did the speed of the TCP response change? Why might this happen?
    TCP became much slower. This happens because TCP has to ensure it sends all messages
    in the correct order and uses congestion control protocols that introduce delay. 


## Code Questions 
1. What is argc and *argv[]?
    argc is used to count how many arguments are passed when the code is run
    *argv[] is an array that holds anything that is on the run line  
    
2. What is a UNIX file descriptor and file descriptor table?
    It's an integer that represents an open file, socket, or I/O resource in a process. The OS assigns an FD when a file is opened.

3. What is a struct? What's the structure of sockaddr_in?
    in object oriented programming, a struct is a user-defined data type that groups certain variables together under a single name, and all of its members and methods are public.
    
    struct sockaddr_in {
        sa_family_t    sin_family;  // Address family (AF_INET for IPv4)
        in_port_t      sin_port;    // Port number (in network byte order) 
        struct in_addr sin_addr;    // IP address (uint32_t s_addr)
    };


4. What are the input parameters and return value of socket()
    int socket(int domain, int type, int protocol)
    1) domain : AF_INET, AF_INET6, AF_UNIX
    2) type : SOCK_STREAM (TCP), SOCK_DGRAM (UDP), SOCK_RAW
    3) protocol : 0 (automatic), IPPROTO_TCP (for TCP), IPPROTO_UDP (for UDP)

    socket() returns a non-negative interger if the socket is created successfully, and -1 otherwise. 


5. What are the input parameters of bind() and listen()?
    int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
    1) sockfd : the file descriptor of the created socket
    2) addr : points to sockaddr struct to access address and port no. 
    3) addrlen : the size of sockaddr structure

    int listen(int sockfd, int backlog)
    1) sockfd : the file descriptor of the created socket
    2) backlog : max number of pending connections that can be queued before accept()
    

6.  Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
    The loop is used to continuously listen for connections. The problem is that it handles one connections at a time and if there are others, they have to wait in the queue.


7. Research how the command fork() works. How can it be applied here to better handle multiple connections?
    fork() creates a child process that can handle independent client connections. This way the server can handle multiple clients. 

    pid_t pid = fork(); // create a child process
    and run the rest if pid is successful, i.e. 0

8. This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?
    System calls allow programs to access the operating system's kernel. They are necessary because user applications are restricted and do not have access to the kernel. The user can include libraries with functions that implicitly invoke system calls.  



