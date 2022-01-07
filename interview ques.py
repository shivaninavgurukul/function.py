"accending order me"
# def binary_search(a,size,key):
#     i=0
#     j=size-1
#     flag=0
#     while i<=j and flag==0:
#         mid=(i+j)//2
#         if a[mid]==key:
#             pos=mid+1
#             flag=1
#         if a[mid]<key:
#             i=mid+1
#         if a[mid]>key:
#             j=mid-1
#     if flag==1:
#         print("Element found at",pos,"position")
#     else:
#         print("Element not found")
# size=int(input("enter size of the list:-"))                          
# a=[]
# for i in range(size):
#     val=int(input("enter the number:-"))
#     a.append(val)
# key=int(input("enter number to search:-"))
# binary_search(a,size,key)      


"desaccending order"
# def binary_search(a,size,key):
#     i=0
#     j=size-1
#     flag=0
#     while i<=j and flag==0:
#         mid=(i+j)//2
#         if a[mid]==key:
#             pos=mid+1
#             flag=1
#         if a[mid]>key:
#             i=mid+1
#         if a[mid]<key:
#             j=mid-1
#     if flag==1:
#         print("Element found at",pos,"position")
#     else:
#         print("Element not found")
# size=int(input("enter size of the list:-"))                          
# a=[]
# for i in range(size):
#     val=int(input("enter the number:-"))
#     a.append(val)
# key=int(input("enter number to search:-"))
# binary_search(a,size,key)      

# n=int(input("enter"))
# d=[]
# i=0
# while i<=n:
#     k=int(input("enter the number:-"))
#     d.append(k)
#     i+=1
# print(d)    



"recursion"
# def recsbinary(a,key,low,high):
#     if low>high:
#         return -999
#     mid=int((low+high)//2)
#     if a[mid]==key:
#         return mid
#     if a[mid]>key:
#         recsbinary(a,key,low,mid-1)
#     if a[mid]<key:
#         recsbinary(a,key,mid+1,high)
# a=[3,4,5,8,10,15,18,25,27,29]
# key=int(input("enter number to search:-"))
# x=recsbinary(a,key,0,9)
# if x == -999:
#     print("not found")
# else:
#     print("no found at",x,"positon")    


"insertion"
# def insert(a,val,size):
#     i=size-1
#     a.append(None)
#     while i>=0 and a[i]>val:
#         a[i+1]=a[i]
#         i=i-1
#     a[i+1]=val
#     print("update list is:",a)
# a=[]
# size=int(input("enter size of list:-"))
# for i in range(size):
#     val=int(input("enter value:-"))
#     a.append(val)
# val=int(input("enter element to inser:-"))
# print("original list is :",a)
# insert(a,val,size)            



"selection sort"
# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp=nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j+1]=temp
#                 print(nums)
# nums=[5,3,8,1,7,2,4,6,9]
# sort(nums)
# print(nums) 




"list me selection sort"
# def section():
#   ele=[12,34,89,76,45,1,4,5,8,9,6]
#   size=len(ele)
#   for i in range(size-1):
#      min=i
#      for j in range(min+1,size):
#         if ele[j]<ele[min]:
#             min=j
#      if i!=min:
#          ele[i],ele[min]=ele[min],ele[i]
#          print(ele)   
# section()              



def rular(n):
   if n==0:
     return  
   print(" - "*n)
   rular(n-1)
   print(" - "*n)
n=int(input("enter the number:-"))
rular(n)
