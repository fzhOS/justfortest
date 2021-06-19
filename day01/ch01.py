# # for value in range(1, 5):
# #     print(value)
# # print(value)
# #
#
#
# # #使用range时，可以使用list（）将结果转化为列表。
# # #eg
# # numbers=list(range(1,6))
# # print(numbers)
# # square=[]
# # print(square)
# # square.append('java')
# # print(square)
# # square.append('python')
# # square.append('c++')
# # square.append('scala')
# # square.insert(0,'c#')
# # print(square)
# # square.sort()
# # print(square)
# # del square[0]
# # print(square)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min1 = min(digits)
# max1 = max(digits)
# sum1 = sum(digits)
# print(min1, max1, sum1)
# print(digits[-5])
# #切片的使用
# print(digits[0:3])
# print(digits[-2:-1])
# print(digits[-2:])
# print(digits[3:])
# print(digits[2:])
# for digit in digits[:]:
#     print(digit)
# 如果要复制列表，必须用整个列表的切片，才能创建这个列表的副本，再将副本存储到新变量。
# 若不使用切片，则是将原变量赋给新的变量，而不是将副本存储到新变量中。此时这两个变量都指向同一个列表。
copy_digits = digits[:]
print(copy_digits)
print(digits)
digits.append(56)
copy_digits.append(88)
print(digits)
print(copy_digits)

copy2 = digits
copy2.append(44)
digits.append(33)
print(digits, copy2)
if 1 in digits:
    print('adding'+str(1)+'.')
elif 2 in digits:
    print('adding'+str(2)+'.')
else:
    for i in digits:
        print(i)
print('\nprint over')
print(len(digits))
hello=(1, 5)
print(len(hello))
print(type(hello[0]))
dic={"type":'python', "kinds":4}
print(dic)
print(dic['type'])
