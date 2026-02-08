def get_user_total():
 price=0.0
 total=0.0
 price_list=[]
 print("enter all prices- once all prices are entered type F- if there is a mistake and you would like to restart enter R")
 print("")
 while price != "F":
  price=(input("You may continue- please enter your prices one at a time: "))

total, price_list=get_user_total()
