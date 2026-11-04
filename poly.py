# #polymophism
# 03/11/2026

# class CashPayment:    
#     def pay(self,amount):
#         print("Paid",amount,"using cash")


# class UPIPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# class cardPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using card")

# class Nebanking:
#     def pay(self,amount):
#         print("Paid",amount,"using neBanking")

# payment=[
#     CashPayment(),
#     UPIPayment(),
#     cardPayment(),
#     Nebanking(),
# ]

# choice=input("choose payment methode(cash/upi/card/nebanking): ")
# if choice == "cash":
#     payment=CashPayment()
# elif choice == "upi":
#     payment = UPIPayment()
# elif choice == "card":
#     payment = cardPayment()
# elif choice == "netbanking":
#     payment = Nebanking()
#     exit()

# payment.pay(1000)

# class SMS:
#     def send(self,message):
#         print("Sending massage through SMS:",message)

# class Email:
#     def send(self,message):
#         print("Sending massage through Email:",message)
# class Whatsapp:
#     def send(self,message):
#         print("Sending massage through Whatsapp:",message) 

# class Telegram:
#     def send(self,message):
#         print("Sending massage through Telegram:",message)


# choice=input("choose massage methode(SMS/email/whatsapp/telegram): ").lower()
# if choice == "sms":
#     message=SMS()

# elif choice == "email":
#     message = Email()

# elif choice =="whatsapp":
#     message = Whatsapp()

# elif choice == "telegram":
#     message = Telegram()

#     exit()

# message.send("Hello, How are you")
