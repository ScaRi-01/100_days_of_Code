from clear_terminal import clear
data_dict = {}
def add_data(new_name, amount):
    data_dict[name] = bid
    return data_dict

game_end = True
while game_end:
    name = input("Who is the bidder: ")
    bid = int(input("Amount of bid: "))
    other_bidders = input("Are there any other bidders?").lower()
    if other_bidders == 'no':
        game_end = False
    
    add_data(new_name=name, amount=bid)
    clear()
max_value = 0
for value in data_dict.values():
    if value > max_value:
        max_value = value
print(max_value)
