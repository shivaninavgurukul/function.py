

# def primeOrnot(num):
#     for i in range(0,num):
#         c=0
#         for j in range(2,i):
#             if (i%j==0):
#                 c=1
#         if (c==0):
#             print(i,end=" ")
#     print("prime number in of num list")
# primeOrnot(406)            


# def greet(*names):
#     for name in names:
#         print("hello",name)
# greet("sonu","kartik","umesh",'pradhuman')        


# def sumOfdigit(number):
#     sum=0
#     modul=0
#     while number !=0:
#         modul=number%10
#         sum+=modul
#         number/=10
#         return sum
# print(sumOfdigit(123))        
       

# def meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="denner":
#             return "roti sabji"
#         else:
#             return "time not found"            
#     elif day=="monday":
#         if time=="breakfast":
#             return "poha"
#         elif time=="lunch":
    #         return "pulaw"
    #     elif time=="denner":
    #         return "roti sabji"
    #     else:
    #         return "time not found" 
    # elif day=="other":
#         if time=="breakfast":
#             return "aalu parada"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="denner":
#             return " maharastri chapati sabji"
#     else:
#         return "time not found"  
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))






# def checkKey():
#     car ={"brand":"ford",
#     "model":"mustang",
#     "year":1964
#     }
#     if "model" in car:
#         print("yes ,'model'is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.") 
# checkKey()                                                  