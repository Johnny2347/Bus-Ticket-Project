import csv
password="12345" #User must enter this password to gain admin privileges.
admin=False
categoryObjectList = []
listOfCatClasses =[]     #Lists for storing and printing out choices for the user
listOfCategories = []
listOfTopUps =[]


#Class for the Categorys
class Category:
    def __init__(self, category, CatCode):
        self.category = category
        self.CatCode = CatCode
    def GetCategory(self):
        return self.category
    def GetCatCode(self):
        return self.CatCode
    

#Class for Topup Types
class TopUpTypes:
    def __init__(self, topupType, category, CatCode, TopupCode,price):
        self.topupType = topupType
        self.TopupCode = TopupCode
        self.CatCode = CatCode
        self.price= price
    def GettopupType(self):
        return self.topupType
    def GetCategory(self):
        return self.category
    def GetCatCode(self):
        return self.CatCode
    def GetTopupCode(self):
        return self.TopupCode
    def Getprice(self):
        return self.price

        
#Login Function, users choose Admin or User login, admin must enter password, if incorrect they must try again
def login():
    choice=input("Please type U for user and A for admin login\n")
    if choice == "U" or choice == "u":
        return "user"
    elif choice == "A" or choice == "a":
    
        choice=input("Please enter admin password\n")
        if choice==password:
            return "admin"
        else:
            print("Incorrect\n")
            return "failed"            
    else:
        print("Incorrect\n")
        return "failed"
        
           
#Menu, opens the csv file and reads it to collect topup types and category data, allows user to select category and topup type, displays user choices
def menu(userType):
    with open('mobile_products.csv', mode = 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile: 
            category = lines['category_title']
            CatCode=lines['category_id']
            TopupCode=lines['topup_id']
            if category not in listOfCategories:
                listOfCategories.append(category)
                cat1 = Category(category,CatCode)
                listOfCatClasses.append(cat1)
            price= lines['topup_price_in_pence']
            topupType= TopUpTypes(lines['topup_title'],category,CatCode,TopupCode, price)
            listOfTopUps.append(topupType)

                           
#Offers user a choice of categories from the csv file, takes user input for choice and displays users choice back to them
            
#try:
    for cat1 in listOfCatClasses:
        print("For ", cat1.GetCategory(), " enter ",cat1.CatCode)
    choice = int(input("Enter Choice\n"))
    print("You have chosen:", listOfCatClasses[choice].GetCategory())
#except ValueError:
    #print("Please enter integer between 1-6")

#finally:

#Offers user a selection of topups, based on their previous choice of categories
    for topup in listOfTopUps:
        if choice == int(topup.GetCatCode()):
            print("For ", topup.GettopupType(), " enter ",topup.TopupCode)
    choice = int(input("Enter Choice\n"))
    print ("You have chosen:", listOfTopUps[choice].GettopupType())

#Gets the price for selected item from the csv file, divides it by 100 so it is in £, users can then checkout or change their choice
    for topupType in listOfTopUps:
        TopupCode = int(topupType.GetTopupCode())
        if choice ==int(TopupCode):
            price = int(topupType.Getprice())
            PriceInPounds=price /100
            print(topupType.GettopupType(),"costs £", PriceInPounds)
            choice=input("Do you want to checkout (1) or choose a different ticket (2)\n")
            if choice=="1":
                print("Thank you")
                quit()
            elif choice=="2":
                menu(userType)                    

#Gets the user type, admin or user, error handling, choice must be from list of login options
userType = "none"
while userType == "none":
    userType = login()
    if userType == "failed":
        userType = "none"
        print("Not a valid input, try again")
    if userType =="user":
        menu(userType)
    elif   userType =="admin":
        choice=input("Press 1 to edit prices")
        


