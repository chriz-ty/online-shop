prod={}  #creating a dictionary

#adding a product details

def addProduct():
    print()
    print("ADD A PRODUCT".center(50,"-")) #.center alings the string in a center
    while True:  #loop works until 'return' executes
        Book_code=int(input("\nEnter Book Code: "))
        Book_cat=input("Enter Book Category: ")
        Book_title=input("Enter Book Title: ")
        Book_price=int(input("Enter Book Price:"))
        Book_qty=int(input("Enter Book Quantity: "))
        prod[Book_code]=[Book_code,Book_cat,Book_title,Book_price,Book_qty]  #stores data as,key-value pairs in a dictionary,(key->book code , value-> list of details of book)
        print("The record entered successfully!")
        ch=input("\nDo you want to insert more records? (y/n):")
        if ch=='n':
            return
    

#checking the availability of a product


def checkProduct(Book_code):
    for key in prod.keys():
        if key==Book_code:
            return True
        else:
            continue
        
        
#Searching/viewing the details of a product        
        
        
def searchProduct():
    print()
    print("SEARCH A PRODUCT".center(50,"-"))
    while True:
        Book_code=int(input("\nPlease enter code:"))
        if checkProduct(Book_code)==True:
            lst=prod[Book_code]
            print("\nBook Details:")
            print("Code: ",Book_code)
            print("Category: ",lst[1])
            print("Title: ",lst[2])
            print("Price: ",lst[3])
            print("Quantity: ",lst[4])
        else:
            print("Enter a valid book code!")
        ch=input("\nDo you want to search more records? (y/n):")
        if ch=='n':
            return
        
        
#updating the already existing records      
        
        
def updateProduct():
    print()
    print("UPDATE A PRODUCT".center(50,"-"))
    while True:
        Book_code=int(input("\nPlease enter code:"))
        if checkProduct(Book_code)==True:
            lst=prod[Book_code]
            print("\nBook Details:")
            print("Code: ",Book_code)
            print("Category: ",lst[1])
            print("Title: ",lst[2])
            print("Price: ",lst[3])
            print("Quantity: ",lst[4])
            ch=input("Do you want to update product category? (y/n): ")
            if ch.lower()=='y':
                new_cat=input("Please enter the new category: ")
                lst[1]=new_cat
            ch=input("Do you want to update product title? (y/n): ")
            if ch.lower()=='y':
                new_title=input("Please enter the new title: ")
                lst[2]=new_title
            ch=input("Do you want to update price? (y/n): ")
            if ch.lower()=='y':
                new_price=input("Please enter the new price: ")
                lst[3]=new_price
            ch=input("Do you want to update quantity? (y/n): ")
            if ch.lower()=='y':
                new_qty=input("Please enter the quantity: ")
                lst[4]=new_qty
        else:
            print("Enter a valid book code!")       
        ch=input("\nDo you want to update more records? (y/n):")
        if ch.lower()=='n':
            return
        
        
#buying the product
        
def buyProduct():
    print()
    print("BUY A PRODUCT".center(50,"-"))
    while True:
        Book_code=int(input("\nPlease enter the book code which you want to buy:"))
        if checkProduct(Book_code)==True:
            lst=prod[Book_code]
            Book_qty=int(input("Please enter the quantity of the product: "))
            if Book_qty>lst[4]:
                print("There are only '{}' quantities of the book '{}' available for sale.".format(lst[4],lst[2]))
            Book_qty=int(input("Please enter the quantity of the product: "))
            if Book_qty>=10 and Book_qty<20:
                d_price=lst[3]/10
                t_price=lst[3]-d_price
                print("The total price to pay is $",t_price)
            elif Book_qty>=20 and Book_qty<30:
                d_price=lst[3]*0.2
                t_price=lst[3]-d_price
                print("The total price to pay is $",t_price)
            elif Book_qty>=30:
                d_price=lst[3]*0.3
                t_price=lst[3]-d_price
                print("The total price to pay is $",t_price)
            else:
                print("The total price to pay is $",lst[3])
        else:
            print("\nPlease enter a valid book code.")
        ch1=input("\nDo you want to buy more? (y/n):")
        if ch1=='n':
            return


#main menu
while True:
    print("\nPlease select one of the following options:")
    print("1.Add Product\n2.Search product\n3.Update Product\n4.Buy Product\n5.Exit")
    choice=int(input("\nPlease enter your choice (1,2,3,4 or 5):"))
    if choice==1:
        addProduct()
    elif choice==2:
        searchProduct()
    elif choice==3:
        updateProduct()
    elif choice==4:
        buyProduct()
    elif choice==5:
        print("\n\nEXITING...\n")
        exit()
    else:
        print("\nplease Enter a valid choice!")
    if choice==5:
        break


  



