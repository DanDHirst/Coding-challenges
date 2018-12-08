import time
start = time.time()
length = 0
longestNum = 0
longestlength = 0
for tempnum in range(1,1000001):

    length = 0
    i=tempnum
    while i != 1:
        if(i % 2==0):
            i =i/2
            length +=1
        elif(i%2!=0):
            i  = (i*3) +1
            length +=1
    if length> longestlength:
        longestlength = length
        longestNum = tempnum
print (longestNum)
print("length")
print(longestlength)
end = time.time()
print("time elapsed")
print(end - start)
    
    
    
