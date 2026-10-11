import csv

categoryList = []
categoryObjectList = []



class Category:
    def __init__(self, category, code):
        self.category = category
        self.code = code
    def GetCategory(self):
        return self.category
    def GetCode(self):
        return self.code
    
listOfCatClasses =[]
listOfCategories = []
listOfCodes = []



with open('mobile_products.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)
    code = 0
    for lines in csvFile:
        category = lines['category_title']
        if category not in listOfCategories:
            listOfCategories.append(category)
            listOfCodes.append(code)
            cat1 = Category(category,code)
            print("For ", cat1.GetCategory()," enter", cat1.GetCode())
            listOfCatClasses.append(cat1)
            code +=1
            
print("Please choose ticket category")
for cat in listOfCatClasses:
    print("For", cat.GetCategory(),"enter",cat.GetCode())
choice = int(input("Please enter choice"))
print(lines['category_title'],"contains",lines['category_description'])
    #print(data.getCode(),"",data.getDescription())
    
    

 
