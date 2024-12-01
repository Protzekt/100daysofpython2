#File not Found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#     file.read()
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("Wtf why troll")



#Key error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)


height = float(input("Height: "))
weight = int(input("Weight: "))

if height >3:
    raise ValueError("You're not a 4 story building brav.")

bmi = weight / height ** 2
print(bmi)