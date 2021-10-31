ch='y'
while ch=='y' or ch=='Y':
    x=input("1.area of rectangle\n 2.area of circle\n 3.area of square\n 4. area of triangle\n")
    if(x=='1'):
        l=int(input("Enter the lenght of rectangle="))
        b=int(input("Enter the breadth of rectangle="))
        print("AREA OF RECTANGLE=",l*b)
    elif(x=='2'):
        r=int(input("Enter radius of the circle="))
        print("AREA OF CIRCLE=",r**2)
    elif(x=='3'):
        s=int(input("Enter side of the square="))
        print("AREA OF SQUARE=",s**2)
    elif(x=='4'):
        b = int(input("enter the base of triangle = "))
        h = int(input("enter the height of triangle = "))
        print("area of triangle is" , 1/2 * b * h)
    else:
        print("wrong input")
    ch=input("do you want more calculations y\n")
print("Thanks for using!!")
             
         
    

