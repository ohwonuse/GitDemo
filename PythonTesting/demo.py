# print('hello')
#
# # here are the comments i have defined
#
# a = 3
# print(a)
#
# Str = 'Hello World'
# print(Str)
#
# b, c, d = 5, 6.4, 'Great'
# # print('Value is ' +b)
# print('{} {}'.format('Value is', b))
# print(type(b))
# print(type(c))
# print(type(d))
#
# values = [1, 2, 'rahul', 4, 5]
# print(type(values))
# print(values[0])
# print(values[1:4])
# values.insert(3, 'shetty')
# print(values)
# values.append('End')
# print(values)
# values[2] = 'RAHUL'
# print(values)
# del values[0]
# print(values)
#
# val = (1, 2, 'rahul', 4, 5)
# print(val[1])
# # val[2] = 'RAHUL'
# print(val)
#
# dic = {'a':2, 4:'bcd', 'c':'Hello world'}
#
# print(dic[4])
# print(dic['c'])
#
# dict = {}
# dict['firstname'] = 'Rahul'
# dict['lastname'] = 'shetty'
# dict['gender'] = 'Male'
# print(dict)
# print(dict['lastname'])

#greeting = 'Good Morning'
# if greeting == 'Morning':
#     print('Condition matches')
#     print('second line')
# else:
#     print('condition do not match')
# print('if else condition code is completed')

# obj = [2, 3, 5, 7, 9]
# for i  in obj:
#     print(i*2)

# summation = 0
# for j in range(1, 6):
#     summation = summation + j
# print(summation)

# for k in range(1,10,2):
#     print(k)

# for m in range(10):
#     print(m)

# it = 4
# while it >  1:
#     print(it)
#     it = it -1
# print('while loop execution is done')

# it = 4
# while it >  1:
#     if it != 3:
#         print(it)
#     it = it -1
# print('while loop execution is done')

# it = 10
# while it >  1:
#     if it == 3:
#         break
#     print(it)
#     it = it -1
# print('while loop execution is done')

# it = 10
# while it >  1:
#     if it == 9:
#         it = it - 1
#         continue
#     if it == 3:
#         break
#     print(it)
#     it = it -1
# print('while loop execution is done')

# def GreetMe(name):
#     print('Good Morning ' + name)
# GreetMe('Rahul Shetty')

# def AddInteger(a, b):
#     return (a+b)
# print(AddInteger(2,  3))

# class Calcualtor:
#     num = 100
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         print('I an called automatically when object is created')
#
#     def getData(self):
#         print('I an now executing as method in class')
#
#     def Summation(self):
#         return  self.a + self.b + Calcualtor.num
#
# obj = Calcualtor(2, 3)
# obj.getData()
# print(obj.Summation())
#
# obj1 = Calcualtor(4, 5)
# obj1.getData()
# print(obj1.Summation())

# str = 'RahulShettyAcademy.com'
# str1 = 'Consulting firm'
# str3 = 'RahulShetty'
# str4 = ' great '
# print(str[1])
# print(str[0:5])
# print(str + str1)
# print(str3 in str)
# var = str.split('.')
# print(var)
# print(var[0])
# print(str4.strip())
# print(str4.lstrip())
# print(str4.rstrip())

# file = open('test.txt')
# print(file.read(5))
# print(file.readline())
# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()
# for line in file.readlines( ):
#     print(line)
# file.close()

# with open('test.txt', 'r') as reader:
#     content = reader.readlines()
#     reversed(content)
#     with open('test.txt', 'w') as writer:
#         for line in content:
#             writer.write(line)

# ItemsInCart = 0
# # if ItemsInCart != 2:
# #     raise Exception('Products Cart count not matching')
#
# if ItemsInCart !=2:
#     pass
# assert (ItemsInCart == 0 )

# try:
#     with open('filelog.txt', 'r') as reader:
#         reader.read()
# except:
#     print('Somehow I reached this block because there is failure in try block')

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print('cleaning up records')