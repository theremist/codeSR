from decimal import Decimal


class User():
    def __init__(self, name, email, phone, userid):
        self.name = name
        self.email = email
        self.phone = phone
        self.userid = userid
       
        self.balance = 100


class RegistrationSystem():
    def __init__(self, name):
        self.company_name = name
        self.users_list = list()


    def findUser(self, name):
        for user in self.users_list:
            if name == user.name:
                return user
        
        return False

    def findUserById(self, uid):
        for user in self.users_list:
            if uid == user.userid:
                return user
        return False


    def newUser(self):
        while True:
            name = str(input("\n\tName: "))

            if not self.findUser(name):
                break
            else:
                print("\t\tThere is already an user registered with that name!")

        while True:
            email = str(input("\tEmail: "))
            if "@" in email:
                break
            else:
                print("\t\tInvalid email!")
        
        while True:
            phone = str(input("\tPhone: "))
            if phone.isdigit() and len(phone) == 9:
                break
            else:
                print("\t\tInvalid phone number!")

        while True:
            userid = str(input("\tUser ID: "))
            if userid.isdigit() and len(userid) == 5:
                break
            else:
                print("\t\tInvalid User ID! Insert a 5 digit number.")

        user = User(name, email, phone, userid)
        self.users_list.append(user)


    def displayUsers(self):
        print("\n\tNumber of users registered in the system: " + str(len(self.users_list)))
        for user in self.users_list:
            print("\t\t" + str(user.name) + "\t|\t" + str(user.email) + "\t|\t" + str(user.phone))


    def findByName(self, name):
        user = self.findUser(name)

        if user:
            print("\t'" + str(user.name) + "' found.\n\t\tEmail: " + str(user.email) + "\n\t\tPhone: " + str(user.phone))
        else:
            print("\t'" + str(name) + "' not found.")


    def saveResults(self):
        f = open("results.txt", "w")

        f.write("Company's name: " + str(company_name) + "\n")
        f.write("Users registered in the system:\n")
        for user in self.users_list:
            f.write("\t\t" + str(user.name) + "\t|\t" + str(user.email) + "\t|\t" + str(user.phone) + "\t|\t" + str(user.userid) + "\t|\t" + str(user.balance) + "\n")

        f.close()


    def makeTransfer(self, sender_id, receiver_name, value: Decimal):
        sender = self.findUserById(sender_id)
        receiver = self.findUser(receiver_name)

        if sender == False:
            return 0

        if receiver == False:
            return 1

        if sender.balance < value:
            return 2

        sender.balance -= value
        receiver.balance += value
        return 3


if __name__ == "__main__":
    print("Welcome to the system!")

    company_name = str(input("Insert the company's name: "))

    registrationObject = RegistrationSystem(company_name)

    option = int()
    while True:
        print("""\nOptions:\n\t[1] Register a new user\n\t[2] Display all users\n\t[3] Find a user by name\n\t[4] Make a transfer\n\t[5] Save\n\t[0] Leave""")
        option = str(input("> "))

        if option.isdigit():
            if option == "1":
                registrationObject.newUser()
                print("Saving results...")
                registrationObject.saveResults()
            elif option == "2":
                registrationObject.displayUsers()
            elif option == "3":
                person_name =  str(input("\tInsert the name of the person that you want to find: "))
                registrationObject.findByName(person_name)
            elif option == "4":
                sender_id = str(input("\tInsert the user id of the sender: "))
                receiver_name = str(input("\tInsert the name of the receiver: "))
                value = Decimal(input("\tInsert the value of the transfer: "))

                res = registrationObject.makeTransfer(sender_id, receiver_name, value)
                if res == 0:
                    print("\t\tThe sender doesn't exist!")
                elif res == 1:
                    print("\t\tThe receiver doesn't exist!")
                elif res == 2:
                    print("\t\tThe sender doesn't have enough money!")
                else:
                    print("\t\tTransfer made successfully!")
            elif option == "5":
                user_n = input('\nPlease insert number ID: ')
                if registrationObject.findUserById(user_n) == False:
                    print ("Please insert your number ID.")
                else:
                    print ("Thank you", eval(user_n))
                    print("Saving results...")
                    registrationObject.saveResults()
            elif option == "0":
                break
        else:
            print("Invalid option!")
    

    print("End.")