#!/usr/bin/env python 
# coding:utf-8
f = open("information.db", "r")  # open db file
account = {

}

# 将信息读入account字典
for line in f:
    line = line.strip().split(",")
    user = line[0]
    print(user)
    account[user] = line
    print(line)
print(account)
f.close()
while True:
    user = input("Input username").strip()
    if user in account:
        if account[user][2] == "1":
            print("your account has been locked,please contact the administrator for help")
            exit('''sorry , your account has been locked,
                          please contact the administrator for help''')
        count = 1
        passwd = input("pleaese Input your password").strip()
        while count < 3:
            if passwd == account[user][1]:
                print(f"Welcome {user} to log in ")
                exit("bye.")
            else:
                count += 1
                passwd = input("Wrong password,please try again...\n").strip()
        account[user][2] = "1"
        print('''sorry , your account has been locked,
                          please contact the administrator for help''')
        break

    else:
        user = input("add your username").strip()
        passwd = input("please input you password").strip()
        account[user] = [user, passwd, '0']
        print(f"Welcome {user} to sign up for the first time")
        break;

f = open("information.db", "w")
for user, val in account.items():
    print(val)
    line = ",".join(val) + "\n"
    print(line)
    f.write(line)
f.close()
