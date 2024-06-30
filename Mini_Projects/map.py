list1 = [" "," "," "]
list2 = [" "," "," "]
list3 = [" "," "," "]

game_map = [list1, list2, list3]

print(f"Enter your location,\n{list1}\n{list2}\n{list3}")
user_input = input("Here:").lower()
abc = ['a','b','c']

position1 = abc.index(user_input[0])
game_map[position1][int(user_input[1])-1] = 'X'


print(game_map)

