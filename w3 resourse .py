"sum of digit"
# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))

"multiplay of digit"
# def multi(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
# print(multi((8, 2, 3, -1, 7)))


"reverse string/number"
# def reverse(list):
#     i=0
#     while i<len(list):
#         d=list[::-1]
#         return(d)
#     i+=1
# print(reverse(("1234abcd")))        

"factorial number"
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

"dublicate remuve"
# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,4,5,6,6,7,3,8,9,8,7,6])) 

"even/odd number in function"
# def evenodd(num):
#     if num%2==0:
#         print("even",num )
#     else:
#         print("odd",num)    
# evenodd(12)    

# def is_even_num(l):
#     even = []
#     for n in l:
#         if n % 2 == 0:
#             even.append(n)
#     return even
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"upper case and lower case"
# def case(letter):
#     d=Upper=0
#     c=Lower=0
#     for i in  letter:
#         if i.isupper():
#             d+=1
#         elif i.islower():
#             c+=1
#     print("upper case",d)
#     print("lower case",c)
# case('The Quick Brown Fox,And Box Are Suppotet And Help Full')                


"square list"
# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l)
# printValues()

# def find(num):
#     d=[]
#     for i in num:
#         if i not in d:
#             d.append(i)
#     return d
# print(find([1,2,2,3,4,5,6,7,7,8,8,9,9,1,2,3]))            

"positive and nagative count"
# def my(list):
#     p=0
#     n=0
#     for i in list:
#         if i>0:
#             p+=1
#         elif i<0:
#             n+=1
#     print(p)
#     print(n)
# my([2,-7,5,-64,-14])                


"prime number"
# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))

"maximum and minimum"
def maxOrmini(list):
    d=max(list)
    print(d)
    i=0
    max2=0
    while i<len(list):
        if list[i]>max2:
            if list[i]!=d:
                max2=list[i]
        i+=1
    print(max2)
    print("(",d,"+",max2,")","=",d+max2)
maxOrmini([10,14,2,23,19])                
def second(a):
    
         
