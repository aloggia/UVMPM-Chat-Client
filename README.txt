Known bugs:
- Program has a tendancy to crash with a broken pipe error when running list_users multiple times in a row
    - I think this is an error relating to the system stdin/stdout
- Program only works on silk in a unix enviroment due to select.select
- Select.select can cause the program to crash when recieving multiple inputs simultaneously
- Sometimes doesn't send messages

Commentary:
My biggest struggle with this project is that I'm not used to socket programming or using the select module.
My code should in theory work, but I keep getting erratic behaviour when running the program. For example I'll run the
program and it'll print all users online sometimes, but not other times.