# Lab 3

## Team Members
- Tina Habibi
- Faith Klein

## Lab Question Answers

Question 1: Why are RESTful APIs scalable? 
    Servers in REST are stateless menaing they do not record session data. This means any available server can communicate with an incoming connection from a client, allowing multiple connections at the same time. 

Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?
    individual mails, inbox, sent list

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
    PUT is not used. We could use PUT to update an existing email entry.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!
    API keys are commonly used in RESTful APIs for managing access, ensuring security, and tracking. APIs ensure that only authorized applications and services can access the data provided, act as a gatekeeper to prevent unauthorized access to sensitive data, and facilitate the integration of services/software by allowing secure communication, in addition to other useful components as well. 