from prettytable import PrettyTable

table = PrettyTable()

# table.add_column("City Name", ["Ahmedabad", "Rajkot", "Bhavnagar"])
# table.add_column("population", [120001, 590014, 798452])
# table.add_column("famous food", ["Dhokla", "Khakhra", "sandwich"])
#
# print(table)

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Thunder", "Water", "Fire"])

table.align = "l"
print(table.align)

print(table)
