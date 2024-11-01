# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(temperatures)
#     print(data)
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas

#data =  pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(type(data))
# print(data["temp"])
#data_dict = data.to_dict()
# print(data_dict)

#Gray_list = data["Gray"].to_list()
#Red_list = data["Red"].to_list()
#Black_list = data["Black"].to_list()
#graysq = data[data.Color == "Gray"].to_dict
#print(graysq)
#Gray_list = data["Gray"].to_list()`

#print(Gray_list)

# print(temp_list)

# avg =  sum(temp_list) / len(temp_list)
# print(avg)

# avg = print(data["temp"].mean())
# max = print(data["temp"].max())
# print(max)
# print(avg)

# print(data["condition"])
# print(data.condition)

#get data in the data frame rows

# print(data[data.temp == max ])
# print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
# print(monday.condition)

#monday_temp_F = monday.temp[0] * 9/5 + 32
# print(monday_temp_F)

#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores":[76,56,65]
#}

#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")


data =  pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count =  len(data[data["Color"] == "Gray"])
black_squirrels_count =  len(data[data["Color"] == "Black"])
red_squirrels_count =  len(data[data["Color"] == "Cinnamon"])
print(grey_squirrels_count)
print(black_squirrels_count)
print(red_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")