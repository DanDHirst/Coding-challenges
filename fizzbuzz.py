for i in range(1,200):
    user = input("Enter fizz or buzz or fizzbuzz else the number: ").lower()
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
        if user != "fizzbuzz":
            print("You entered " + user + " and it should have been number fizzbuzz")
            break
    elif i%3==0:
        print ("fizz")
        if user != "fizz":
            print("You entered "+ user + " and it should have been fizz" )
            break
    elif i%5==0:
        print("buzz")
        if user != "buzz":
            print("You entered " + user + " and it should have been buzz" )
            break
    else:
        print (i)
        if user != str(i):
            print("You entered " + user + " and it should have been" + str(i) )
            break
    
