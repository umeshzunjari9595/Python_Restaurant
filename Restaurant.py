#MenuCardkuka
Menu = {"Coffee":80,"Kuka":100,"Sandwich":140,"Tea":40,"Pasta":100}
print("WELCOME TO PYTHON RESTAURANT")
Bill_total=0
print("Please select your order from menu",Menu.keys())
Item1 = input("Please select your choice  ")
if Item1 in Menu:
    print (Item1,"has added ")
    Bill_total +=Menu[Item1]
else:
    print ("please select from menu")
  
Item_2= input("Do you want something else?  Yes/ NO   ")
if Item_2 == "Yes":
    print("Please select your order from menu",Menu.keys())
    item2name = input("Please select your choice  ")
    if Item1 in Menu:
        print (item2name,"has added ")
        Bill_total += Menu[item2name]
        print ("Your Billing amount is ",Bill_total)
    else:
          print ("please select from menu")
else:
    print("Your Billing amount is ",Bill_total)
