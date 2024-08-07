from art import logo

print(logo)

print("Welcome to the secret auction program")
from replit import clear
auction_dict = {}
name_list = []
def auction(name,bid):
  auction_dict[name] = bid
  name_list.append(name)
 
should_end = False
while not should_end:
  name_inp = input("What is your name?")
  bid_inp = input("what's your bid? : $")
  
  other = input("Are there any other bidders? Type 'yes' or 'no'.")
  clear()
  auction(name= name_inp, bid= bid_inp)
  
  if other == "no":
    should_end = True
    value=[]
    for value_list in auction_dict:
      value.append(auction_dict[value_list])
    # print(value)
    highest = 0
    highest = value[0]
    for i in value:
      if i > highest:
        highest = i
        winner = name_list[value.index(highest)]
    
    #print(name_list)
    print(f"The winner is {winner} with a bid of ${highest}")
        
#print(auction_dict)
    