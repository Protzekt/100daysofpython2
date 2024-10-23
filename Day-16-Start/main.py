from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Pokemon Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtlu","Water"])
table.add_row(["Voltorb","Electric"])
table.add_row(["Charizard","Fire"])
table.align = "l"
print(table)