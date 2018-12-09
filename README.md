# rpn-client-server
Simple client server in python to calculate RPN expressions

rpnclient.py - RPN client
rpnserver.py - RPN server
sample.txt - some sample tests

Instructions-
1. Navigate to directory containing rpnserver.py file and run server using - python rpnserver.py
2. Navigate to directory containing rpnclient.py and run commands like - python rpnclient.py 65432 "1 2 3 +"
   Format - python rpnclient.py <port number> <rpn expression>

Protocol description-
Format of messages from client to server is of the kind - "a b op", where a and b are integers and op is one of "+","-","*","/"
Format of messages from server to client is of the kind - "a" where a an integer obtained after computation
Error - in case of wrong format from client to server or invalid arguments(eg - division by 0) "ERROR 400" string is returned from the server

Limitations-
1. Handles only integer division - 4/3 = 1 and maximuum values supported are limited by int datatype of python
