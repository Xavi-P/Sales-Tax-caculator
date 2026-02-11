

def get_user_total():
 price=0.0
 total=0.0
 price_list=[]
 print("enter all prices- once all prices are entered type F- if there is a mistake and you would like to restart enter R")
 print("")
 while price != "F":
  price=(input("You may continue- please enter your prices one at a time: "))
  
  if price=='R':
    total=0.0
    price=0.0
  if price != "F" and price != "R":
    try:
      price=float(price)
    except ValueError:
      print("please enter a valid number ")
    else:
      total=total+price
      price_list.append(price)
 
 
 return total, price_list
  
def get_user_state():
  state_list=list = [
  "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
  "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
  "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
  "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
  "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
  ]
  user_state=input("Please enter the intials of the state in captial letters (i.e NJ): ")
  while user_state not in state_list:
    user_state=input("invalid state-Please enter proper initials of your states in captial letters: ").upper().strip()
  return user_state

def get_state_tax(user_state):
  state_tax_dict = {
  "AL": "0","AK": "6.5","AZ": "5.6","AR": "6.5","CA": "7.25","CO": "2.9","CT": "6.35","DE": "0",
  "FL": "6","GA": "4","HI": "4","ID": "6","IL": "6.25","IN": "7","IA": "6",
  "KS": "6.5","KY": "6","LA": "5","ME": "5.5","MD": "6","MA": "6.25","MI": "6",
  "MN": "6.88","MS": "7","MO": "4.23","MT": "0","NE": "5.5","NV": "6.85","NH": "0",
  "NJ": "6.63","NM": "4.88","NY": "4","NC": "4.75","ND": "5","OH": "5.75","OK": "4.5",
  "OR": "0","PA": "6","RI": "7","SC": "6","SD": "4.2","TN": "7","TX": "",
  "UT": "6.1","VT": "6","VA": "5.3","WA": "6.5","WV": "6","WI": "5","WY": "4"
  }
  state_tax=state_tax_dict[user_state]
  state_tax=float(state_tax)
  return state_tax

def caculate(state_tax,total):
  
  cart_total= total+ total*(state_tax*0.01)
  tax_collected= total*(state_tax*0.01)
  return cart_total, tax_collected

def reciept(tax_collected, cart_total,price_list,state_tax):
  print("RECEIPT")
  print("=======")
  for price in price_list:
    print("$"+str(price))
  print("")
  print("Total Tax Collected")
  
  print("$"+str(round(tax_collected,2)))
  print("")
  print("Cart Total")
  print("$"+str(round(cart_total,2)))

def reciept_file(tax_collected, cart_total,price_list,state_tax):
  with open("receipt.txt") as f:
    print("RECEIPT",file=f)
    print("=======",file=f)
    for price in price_list:
      print("$"+str(price),file=f)
    print("",file=f)
    print("Total Tax Collected",file=f)
    
    print("$"+str(round(tax_collected,2)),file=f)
    print("",file=f)
    print("Cart Total",file=f)
    print("$"+str(round(cart_total,2)),file=f)

total, price_list=get_user_total()
user_state=get_user_state()
state_tax=get_state_tax(user_state)
cart_total, tax_collected=caculate(state_tax,total)
print("your total is " + str(cart_total))
reciept(tax_collected, cart_total,price_list,state_tax)
reciept_file(tax_collected, cart_total,price_list,state_tax)
