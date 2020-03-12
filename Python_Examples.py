# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
x=input("Enter the charecter:")
if "cat" and "dog" in x:
    print("Dog and Dog")
elif "dog" in  x:
    print("Dog")
elif "cat" in x:
    print("Cat")
else:
    print("None")
#%%
x=int(input("Enter the charecter:"))
if type(x) is int:  
    if x<=0:
        prin]}t("UNBORN")
    elif x>0 and x<=150:
        print("ALIVE")
    else:
        print("VAMPIRE")
else:
    print("Please enter integer vaue")
#%%
x=int(input("Enter the charecter:"))
if type(x) is int:  
    if x<=0 and x>=168:
        print("INVALID")
    elif x>0 and x<=40:
        a=x*8
        print("YOU MADE",a,"DOLLARS THIS WEEK")
    elif x>=41 and x<=49:
        i=x-40
        b=(i*9)+(40*8)
        print("YOU MADE",b,"DOLLARS THIS WEEK")
    elif x>=50 and x<=167:
        j=x-40
        k=j-9
        y=(40*8)+(k*10)+(9*9)
        print("YOU MADE",y,"DOLLARS THIS WEEK")
else:
    print("Please enter integer vaue")    
#%%
no_cookies=0
while no_cookies==0 or no_cookies<20:
    no_cookies+=1
    print("I eat a cookie",no_cookies)
    
#%% 
    # Infinte LOOp
while True:
    print("Looping")
#%%
#Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. 
#( 1 and 101 are included) (Use while loop)
i=0
x=0
while i<=101:
    if i%5==0:
        x+=i
        z=x
    i+=1
print(z)
    
#%%
#Write a program using while loop, which asks the user to type a positive integer, n, 
#and then prints the factorial of n. A factorial is defined as the product of 
#all the numbers from 1 to n (1 and n inclusive).
 #For example factorial of 4 is equal to 24. (because 1*2*3*4=24)

x=int(input("Enter the charecter:"))
i=1
y=1
while i<x:
    a=i+1
    y=a*y
    #z=y*a#z=a*i
    #y=z
    #j=y*a
    i+=1
print(y)
    

#%%
#Write a program using while loop, which prints the sum of every third numbers
 #from 1 to 1001( both 1 and 1001 are included)(1 + 4 + 7 + 10 + ....)

x=1001
i=1
y=0
while i<=x:
    #a=i+3
    y=y+i
    #z=y*a#z=a*i
    #y=z
    #j=y*a
    #print(y)
    i=i+3
print(y)

#%%

#DIsplay books in for list using for loop
books=["Aerica","India","Russia","China","England"]
for x in books:
    print("The books in the order:",x)

#%%
    
    #Using a for loop, write a program which prints the sum of 
    #all the even numbers from 1 to 101. 
    a=0
    for x in range(1,100):
        if x%2==0:
            a=a+x
            #z=a
            y=z+a
            print(x)
       # else:
       #     print("odd Number")
    print(y)
#%%
    #Using a for loop, write a program which asks the user to type an integer, n, and then 
    #prints the sum of all numbers from 1 to n (including both 1 and n).
x=int(input("ENter the number:"))
a1=0
for i in range(1,x+1):
    a1=a1+i
print(a1)
    

#%%

#Using a for loop, write a program which asks the user to type a positive integer, n, 
#and then prints the sum of the square of all numbers form 1 to n (including both 1 and n).
#For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14

x=int(input("ENter the number:"))
a2=0
for i in range(1,x+1):
    a2+=(i**2)
print(a2)
#%%
#Usage of continue and break statement
for char in "computer":
    print(char)
print("With continue statement on char 'p'")
for char in "computer":
    if char=="p":
        continue
    print(char)
print("With break statement on 'p'")
for char in "computer":
    if char=="p":
        break
    print(char)
        
#%%
m = 0
for x in range(1,4):
    for y in range(1,3):   
        m = m + 1
        print(m)
print (m)
#%%
# Lets sort the following list by the first item in each sub-list. 
my_list = [[2, 4], [0, 13], [11, 14], [-14, 12], [100, 3]]
# First, we need to define a function that specifies what we would like our items sorted by
def my_key(item):
    return item[-1]                                            # Make the first item in each sub-list our key
new_sorted_list = sorted(my_list, key=my_key)                 # Return a sorted list as specified by our key
print("The sorted list looks like:", new_sorted_list)        

#%%
#use of enumerat()
num=([1,2,3,4,5])
for item in enumerate(num,50):
    print("item number is:",item)



#%%
#To find the maximum from their digit sum
    
def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

num = [15, 300, 2700, 821, 52, 10, 6,999]
print('Maximum is:', max(num, key=sumDigit))
    
 #%%%
 
 wrong
def diffdigit(num):
     diff=0
     diff1=0
     while(num):
         diff1=abs(diff)
         diff1-=num%10
         num=int(num/10)
     return diff1
     print (diff1)
num = [ 300, 2700, 821, 52, 6,999]
print('Maximum  from subtraction is:', max(num, key=diffdigit))
 
#%%    
def diffdigit(num):
    diff=0
    #for i in number[i]:
    while (num): 
        number1=str(num)
        print (len(number1))
        diff=0
        for i in range(0,(len(number1))-1):
            diff-=abs(int((number1[int(i)])))#-abs(diff))
            diff=abs(diff)
        
        return diff
        
       # print (diff)
    #return diff       
        #diff=abs(diff)
        #diff-=1num%10
        #diff1=diff%100
        #num=int(num/10)
     #return abs(diff)
num = [ 30, 2100, 81, 52, 999]  
print('Maximum  from subtraction is:', max(num, key=diffdigit))
#%%
length=str(600)
print(len(length))
#%%
test =['J','A','G','A','N']
print(list(reversed(test)))
#%%
def takeSecond(elem):
    return elem[-1]

# random list
random = [(2, 2,2), (3,5, 4), (4,0, 1), (1, 7,3)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print('Sorted list:', sortedList)
#%%
x = [1, 2, 3, 4, 5]                                      # Create a list
y = ['a', 'b', 'c']                                      # Note that this list only has 3 elements
zipped = set(zip(x, y) )                                # Return the zipped object as a list of tuples
print("The result of the operation is:", zipped)        

#%%
### To write a program for square root

def square_root(input_num):
    half=input_num/2
    acc=0.01
    while abs(input_num-(half**2))>acc:
        half=(half+(input_num/half))/2
    return half

x=int(input("Enter the number to find square_root:"))
for i in range(1,x):
    y=square_root(i)
    print("Squared value of", i," is:",y)

#%%
def square(num):
    out=num**2
    return out
 
x=int(input("Enter the number:"))
y=square(x)
print(y)
#%%
# Type your code here
def sum(num):
    add=0
    for i in range(0,len(num)):
        add+=int(num[i])
    return add
x=list(input("Enter the numbers:"))
print(x)
y=sum(x)
print(y)
#%%

# Type your code here
def multi(num1,num2,num3):
    out=num1*num2*num3
    return out
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))
y=multi(num1,num2,num3)
print(y)

#%%
def evennum(num):
    #num=list(num)
    #print (num)
    out=[]
    for item in range(0,len(num)):
        if int(num[item]) % 2==0:
            out.append(num[item])
        else:
            continue
    return out

#x=input("enter the list:")


print(evennum([1,4,5,8]))


#%%%

#%%

# Type your code here
def minimum(num):
    a=num[0]
    for item in num:
            if item<a:
            #b=num[i+1]
                small=item
           # else:
           #     small=a
    return small



#x7=(input("enter the list:"))


print(minimum([4,2,5,7]))


#%%

def evalute(x):
    y=(((x**2)*(x**2))-12*((x**2)*x)+13*(x**2)+11)
    #y=(x**4)-12*(x**3)+13*(x**2)+11
    return y

input_value=int(input("Enter the value"))
out=print(evalute(input_value))


#%%
# Type your code here
def magnitude_calc(num):
    x=int(num[0])
    y=int(num[1])
    z=int(num[2])
    added=int((x**2)+(y**2)+(z**2))
    half=added/2
    acc=0.001
    while abs(added-(half**2))>acc:
        out=(half+(added/half))/2
    return out
#num=[2,3,-4]
print(magnitude_calc([2,3,-4]))
#%%
def ave(list1):
    #list2=list1
    sumed=0
    for item in list1:
        sumed+=(int(item))
    return sumed

#list1=[1,4,7,9]
#out=ave(list1)
print(ave([1,2,3,4]))
#%%
def maxi(list1):
    #maxed=0
    #max_final=0
    for i in range(0,(len(list1)-1)):
      #print(i)
      if list1[i]>list1[i+1]:
          max1=list1[i]
          if list1[i+1]>list1[i+2]:
              out_max=list1[i+1]
              print(out_max)
          else:
              out_max=list1[i+2]
              print(out_max)
      else:
          max1=list1[i+1]
          print(max1)
    return (out_max)
print(maxi([12,4,6]))
#%%
'''Writing a functioon insuide a function'''
def max_fun(x,y):
    sum_result=x+y
    def condition(value):
        if (value % 2)==0:
            return True
        else:
            return False
    
    status=condition(sum_result)
    return(status)

print(max_fun(5,21))

#%%
'''Triangle unction'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

x=int(input("Please enter the pos integer:"))
for i in range(1,(2*x)):
    #count=0
    sym='*' 
    if i<=((2*x/2)):
        symbol=sym
        print(sym*(i))
    elif i>=(x/2):
        print(sym*((2*x)-i))



#%%
#list4=[1,2,3,4,5]
#print(len(list4))
def main_func(list1):
    odd_num=[]
    for i in (0,(len(list1)-1)):
        if (list1[i]%2)!=0:
           # value=list1[i]
           # print(value)
           
           odd_num.append(list1[i])
      #  else:
        #   odd_num.append(list1[i])
    print (odd_num)
    #print(int(list1[3])%2)
print(main_func([2,1,3,6]))

#%%

def main_func(list1):
    odd_num=[]
    for item in list1:
        if (item%2)!=0:
           # value=list1[i]
           # print(value)
           
           odd_num.append(item)
        #else:
        #   odd_num.append(list1[int(i)])
    print (odd_num)
    #print(int(list1[3])%2)
print(main_func([2,1,3,6]))

#%%
def main_func(list1):
    odd_num=[]
    for item in list1:
        if (item%2)!=0:
            odd_num.append(item)
    #print (odd_num)
    def add(list2):
        added=0
        for item in list2:
            added+=item
        return added
    out=add(odd_num)
    return(out)
print(main_func([2,1,101,6]))
#%%
list1=[1,2,3,4,5]
#list1.remove(1)
#list1.pop(2)
#list1.sort()
#list1.sort(reverse=True)
list1.reverse()
print(list1)
#%%
my_list = ['two', 5, ['one', 2]]
print(len(my_list))
#%%
MyList = [1, 5, 67, 3, 4]
MyList.sort()
print (MyList)
#%%
MyList = [3, "dog", 9, "cat"]
MyList.pop()
print (MyList)
#%%
my_list = []
for x in range(1,10):
    if not(x % 5):
        my_list.append(x)
print(my_list)

#%%

def multiple5(value):
    out=[]
    for i in range (1,(6*value)):
        if i%value==0:
            out.append(i)
    return out
print(multiple5(3))
#%%
def even_num(a,b):
    even=[]
    for i in range(a,b):
        if i%2==0:
            even.append(i)
    return even
print(even_num(2,100))
#%%
my_list = [5, 'old', 'new', 8, 'time', 2]
print(my_list[3:2])
my_list = [5, 'old', 'new', 8, 'time', 2]
print(my_list[3:7])
#%%
my_list=[54,'cow',0.25,32,'worm']
print(my_list[3:-1])
#%%

def manipu(list1,string):
    out1=[]
    out2=[]
    for i in range(1,4):
        out1.append(string)
        list1[i]=string
    return list1
print(manipu(['fdsf','dfdsf','dfsf','fdsf','fdsf','fdsf','fdsf'], 'jagan'))
#%%
def _custom_bubble_sort_sample_(original_list):
    # This is an implementation of the
    # famous bubble sort algorithm
    # This can a very inefficient algorithm
    # when used with large data
         
    # our purpose here however is to show how to sort
    # a list without any built-in methods
	

    # make a copy of the original list
    my_list = original_list[:]
  
    # get the length of the list
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            # if next element is greater element then swap them
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unSorted = True
    return my_list
print(_custom_bubble_sort_sample_([1,2,3,8,5]))
#%%
def ascending(list1):
    out=[]
    out2=[]
    for i in (0,(len(list1)-1)):
        if list1[i]<=list1[i+1]:
            small=list1[i]
        else:
            small=list1[i+1]
        out.append[small]
        if out==[]:
            continue
        else :
            if out[i]<=small
        
#%%
def numbering(list1):
    input1=list1
    count=0
    out=[]
    for i in range(0,(len(list1))):
        #a=True
        #for i in range(0,(len(list1)-1)):
        if list1[0]==list1[i]:
            count+=1
        out.append(count)
        if list1[1]==list1[i]:
            count+=1
        out.append(count)
    return out
numbering([1,2,1,2,1])            
#%%
# Type your code here
def adds(list1,list2):
    odd1=[]
    odd2=[]
    for i in list1:
        if i%2!=0:
            odd1.append(i)
    for j in list2:
        if j%2!=0:
            odd1.append(j)
    odd1.extend(odd2)
    sum=0
    for item in odd1:
        sum+=item
    return sum
adds([1,2,2,2,1],[5,2,2,2,5])    
#%%
n=(input('please enter an integer between 1 and 9999: '))
num=list(n)
number=[0,1,2,3,4,5,6,7,8,9]
print (number)
ones=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tenses=['thousand', 'hundred']
tens_1=['eleven', 'twelve','thirteen', 'fourteen', 'fifteen','sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

huns=[]
thous=[]
#a=int(num[3])
#print (num[3])

if int(num[3]) in number:
    ones=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    x=number.index(int(num[3]))
    out4=ones[x]
    print (out4)
if int(num[3]) and int(num[2]) in number:
    if int(num[3])==0:
        
#return (x)
#%%
x = ["dog", 2, "cat", 34, 5.8]
m = 0
for i in range(len(x)):
    m = m + i
print(m)
#%%
def my_fun(x,y):
    m = x ** y  
y = my_fun(2, 3)    
print(y)
#%%


i = 1
while False:
    if i % 5 == 0:
        break
    i = i + 2
print(i)
#%%
count = 0
list_1 = []
for i in range(1,4):
    list_1.append(i**2)
for x in list_1:
    count = count + x
print(count)
#%%
def my_fun(my_list,s,e):
    del (my_list[s:e])
 
values = [2, 9, 16, 3, 24, 13, 15]
my_fun(values,-6,-4)
my_fun(values,2,4)
print(values)        
#%%
def divisor(list1):
    out=[]
    for item in list1:
        count=0
        for i in range(1,(item+1)):
            
            if int(item)%i==0:
                count+=1
            #return count
        out.append(count)
        print(out)
    x=max(out)
    posi=out.index(x)
    output=list1[posi]
    print('max divisor element is:',output)
print(divisor([108,2,3,12]))     
#%%
out=[]
out1=""
for i in range(20000,20501):
    out.append(chr(i))
    out1+=chr(i)
#print(out)
print("\a",out1)
#%%
#print("who \n \"the hell\" \n")
s="wow"
print(s.clear())
#%%
s="my NamE and my is Jagan. mymy  "
s.capitalize()
#s.center([n])
#s.title()
#s.lower()
#s.strip()
#s.count("my",5,6)
#s.replace("my","I",1)
s.split("my")
#%%
s="jagannathan"
print(len(s))
#list1=list(s)
#print(list1)
out=[]
for i  in range(1,len(s)+1):
    #print(s[i])
    out.append(s[-i])
#print (out)
s1=str(out)
#make = ''.join(map(str, out))
make1=''.join(out)
print(make1)
#output=str(out)
#%%
s="jagannathan"   
out=""
for i in s:
    out=i+out
print(out)
#%%
def num_word(stri,n):
    word=stri.split()
    count=0
    for i in word:
        if len(i)==n:
            count+=1
    return count
print(num_word("my nme is to wasa as such that",3))
#%%
'''Plindrome Test'''
def palindrome(string):
    rev=""
    for i in string:
        rev=i+rev
    if rev==string:
        return True
#%%
result=[["jagan",90,80,80],["raj",90,85,70],["shankar",70,90,80]]
#print(result[0][1][1])
for outer_list in result:
    #print(outer_list)
    total=0
    for inner_list in range(1,len(outer_list)):
        print(outer_list[inner_list])
        total+=outer_list[inner_list]
    print("The average for",outer_list[0],"is :",total/3)
    #%%
'''Addition of two elements in 2D array'''
result1=[[90,80,80],[90,85,70],[70,90,80]]
def addition(list1):
    total=0
    for outer_list in list1:
        for inner_list in range(0,len(outer_list)):#outer_list:
            total+=outer_list[inner_list]
    print(total)
addition(result1)
#%%
'''Average for given number'''
result1=[[90,80,80],[90,85,70],[70,90,80]]
def addition(list1):
    total=0
    count=0
    for outer_list in list1:
        
        for inner_list in range(0,len(outer_list)):#outer_list:
            total+=outer_list[inner_list]
            count+=1
    return (total/count)
addition(result1)
#%%
'''2D to 1D'''
def one_dim(list1):
    a=[]
    for outer_list in list1:
        for inner_list in range(0,len(outer_list)):#outer_list:
            b=outer_list[inner_list]
            a.append(b)
            a.sort()
    return a
print (one_dim([[90,80,80],[90,85,70],[70,90,80]]))
#%%
a=[[1,2,3],[1,5,6]]
b=[[1,1],[1,1]]
def multi_check(list1,list2):
    a=len(list1)
    b=len(list2)
    if a==b:
        return True
    elif a!=b:
        return False
print(multi_check(a,b))
#%%
#import numpy
a = [[2, 3, 4],[3, 4, 5]]
b = [[4, -3, 12],[1, 1, 5],[1, 3, 2]]
#y=b[:][:1]#
#print (y)
def multi_mat(a,b):
    #mu0000000000l
    out=[]
    for m_out_index in a:
       for m_inn_index in range(0,len(m_out_index)):#range(0,len(b[:][0]))
           for n_outer_index in b:
               for n_inner_index in range(0,1):
               #range
                   x=m_out_index[m_inn_index]*n_outer_index[n_inner_index]
                   #out.append[x]
                #print(x)
                   
                   return (x)#return x
multi_mat(a,b)   
#%%
person={'Name':'Jagan','age':25,'job':'nil', 'prof':'student','weight':75}
#person.clear()
x=person.get('height',wow)
print(x)
    #%%
numbers={"one": "uno", "two": "dos", "three": "tres"}
print (numbers.get("test",'dos'))
#%%
def multiplication_table(n):
    out=[]
    out1=""
    for i in range(1,((n*n)+1)):
        out1=out1+str(i)
        #out=out+str(i)
        if i%5==0:
            out1=out1+str('q')            
            #out=out+str('q')            
    out=out1
    out1.split('q')
    
    #x=str(out)
    return (out1)
    return (out)
print(multiplication_table(5))
#%%
file=open('/home/jagan/Desktop/spyder/data.txt','r')
#read=file.read(1000)
#line=file.readline()
all_lines=file.readlines(1000)
#print(read)
print(all_lines)
#print(line)
#%%
file=open('/home/jagan/Desktop/spyder/write.txt','w')
file.write("My name is jagan")
file.close()
#%%
'''Using tuple to return the Multiple Value from a function'''

def sum_1(x,y):
    return (x+y,x*y,x/y)
(s,p,d)=sum_1(10,10)
print(s,p,d)
#%%
def mean(tuples):
    s=0
    for item in tuples:
        s+=item
    mean=(s/len(tuples))
    for item in tuples:
        if (len(tuples)%2)==0:
            mid=tuples[(len(tuples)//2)-1]+tuples[((len(tuples)//2))]
            median=mid/2
        elif (len(tuples)%2)!=0:
            median=tuples[((len(tuples)//2))]
    return (mean,median)
print(mean((3, 3, 0, 1, 12, 13, 15, 16)))

#%%
'''mean and median for '''
def _statistics_with_a_tuple_sample_(sample_tuple):
    import numpy
    mean = sum(sample_tuple)/len(sample_tuple)
    median = numpy.median(numpy.array(sample_tuple))
    return mean, median
print(_statistics_with_a_tuple_sample_((3, 3, 0, 1, 12, 13, 15, 16),))
#%%

input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"} 
def dic_tuple(dic):
    key=[]
    out=[]
    x=dic.keys()
    list1=list(x)
    list1_out=tuple(list1)
    y=dic.values()
    list2=list(y)
    list2_out=tuple(list2)
    out.append(list1_out)
    out.append(list2_out)
    out_tup=tuple(out)
    return out_tup
dic_tuple(input_dictionary)
#%%
'''Analysing the Scope'''
def fun1():
    def fun2():
        y=100
        print("x inside fun2 is:",y)
    y=50
    print("x inside fun1 is:",y)
    fun2()

#y=35
print("x inside main is:",y)
fun1()
#%%
def factorial(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    return fac
print (factorial(3))
#%%
'''Recursive function to return the same of numbers given an integer 10'''
def number(x):
    if x <= 1:
        return 1
    else:
        return (x+ number(x-1))
print(number(10))
#%%
'''calculate nth fibonnaci number for given number'''
def fibonnaci(num):
    out=[]
    #sec=1
    #temp1=1
    if num==0:
        return 0
    elif num==1:
        return 1
    
    else:
        #print(fibonnaci(num-1)+fibonnaci(num-2))
        #out.append((fibonnaci(num-1)+fibonnaci(num-2)))
        return(fibonnaci(num-1)+fibonnaci(num-2))
        #return out
        
        '''
        if num>=2:
            for i in range(1,num):
                #temp1=sec
                sec+=temp1
                temp2=sec
        #for i in range(2,(num+1)):
            return sec
        '''
print(fibonnaci(10))
#%%
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''
'''TEst Series'''

#%%
x={'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
def group_by_owners(x):
    key=[]
    value=[]
    value_out=[]
    keys=list(x.keys())
    values=list(x.values())
    print(keys)
    print(values)
    #temp=""
    for item in keys:
        if item not in key:
            key.append(item)
            print(key)
        if item in key:
            temp=x.pop(item)
            print(temp)
            value.append(temp)
            
        value_out.append(value)
        value.clear()
    print(key)
    print(value_out)
            
group_by_owners(x)
#%%

x={'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
def group_by_owners(x):
    key=[]
    value=[]
    value_out=[]
    keys=list(x.keys())
    values=list(x.values())
    #print(keys)
    #print(values)
    #temp=""
    for item in values:
        if item  not in value:
            value.append(item)
            print(value)
        #if item is not  values:
            #res_key=x.keys()
            index=values.index(item)
            #temp=x.pop(item)
            temp=keys[index]
            print(temp)
            value.append(temp)
            
        value_out.append(value)
        #value.clear()
    print(key)
    print(value_out)
            
group_by_owners(x)
#%%
class palindrome:
    def __init__(self,inp):
        self.inpu=inp
    def is_palindrome(self):
        text=self.inpu
        textlow=text.lower()
        print(textlow)
        rev=""
        #rev.reverse()
        #print (rev)
        for i in range(1,(len(text)+1)):
            rev+=text[-i]
           # print(rev)
        if rev==text:
            return True
        else:
            return False
pal=palindrome('woOw')
pal.is_palindrome()
#is_palindrome('woow')
#%%
