#!/usr/bin/env python 
# coding:utf-8
def register_api():
    phonelist, identitylist = load_validatee_data(db_file)
    print("欢迎来到路飞学城".center(50,"-"))
    print("请完成学籍注册")
    name=input("姓名:").strip()
    age=input("年龄:").strip()
    number=input("手机号:").strip()
    while True:
        if number not in phonelist:
            break
        else:
            number=input("请重新输入你的手机号")
    identity=input("身份证号").strip()
    while True:
        if identity not in identitylist:
            break
        else:
            identity=input("请重新输入你的身份证号")
    course_list=["Python开发","Linux云计算","网络安全","数据分析"]
    for index,course in enumerate(course_list):

        print(f"{index}. {course}")
    selected_id=input("选择想学的课")
    if selected_id.isdigit():
        selected_id=int(selected_id)
        if(selected_id>=0 and selected_id<len(course_list)):
            pick_course=course_list[selected_id]
        else:
            exit("不合格的选项...")
    else:
        exit("非法输入")
    student={}
    student["name"]=name
    student["age"]=age
    student["number"]=number
    student["identity"]=identity
    student["course"]=pick_course
    return student

db_file="student.db"

def commit_to_database(databasefile,student_data):
    file=open(databasefile,"a+")
    str=f"{student_data['name']},{student_data['age']},{student_data['number']}" \
        f",{student_data['identity']},{student_data['course']}\n"
    file.write(str)
    file.close()

def  load_validatee_data(filename):
    f=open(filename)
    phone=[]
    identity=[]
    for line in f:
        list=line.strip().split(",")
        phone.append(list[2])
        identity.append(list[3])
    return phone ,identity
commit_to_database(db_file,register_api())



