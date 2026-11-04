#nested loop
    # for i in range (1,6):
    #     for j in range (1,5):
    #        print("outer loop:",i,"Inner loop:",j)

# for r in range (1,5):
#     for c in range (1,6):
#         print("*",end=" ")
#     print()

# for r in range (1,5):
#     for c in range (r):
#         print("*",end="")
#     print()

# for r in range (5,0,-1):
#     for c in range (r):
#         print("*",end="")
#     print()

# for r in range (1,6):
#     for c in range (1,r+1):
#         print(c, end=",")
#     print()

# for r in range (1,6,5):
#     print(r, end="")
# print()

# for num in range (2,11):
#     print("Multiplication of:",num)
#     for multiply in range (1,11):
#         print(num,"*",multiply,"=",num*multiply)
#     print()


#while loop
# i=1

# while i<= 10:
#     print(i)
#     i +=1

    #even number b/t 1 to 20

# i=2
# while i<=20:
#     if i == 12:
        # Break
#      print(i)
#     i += 2
#     continue

# #calculator program
# print("My calculator !")
# print("Type 'exit' to quit")

# while True:

#    op=input("Enter operation (+,-,*,/, or exit:)")
#    if op == "exit":
#        print("calculator closed!")
#        break
#    num1=float(input("Enter first number:"))
#    num2=float(input("Enter second number:"))

#    if op == "+":
#       print(num1,"+",num2,"=",num1+num2)
#    elif op == "_":
#       print(num1,"-",num2,"=",num1-num2)
#    elif op =="*":
#       print(num1,"*",num2,"=",num1*num2)
#    elif op =="/":
#       print(num1,"/",num2,"=",num1/num2)
#    else: 
#       print("Invalid operation")    