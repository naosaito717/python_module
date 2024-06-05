list = [5,1,4,6,2]

# for i in range(len(list)):
#     for j in range(len(list)-1):
#         if list[j] > list[j + 1]:
#             list[j], list[j + 1] = list[j + 1],list[j]
            
# for i in range(len(list)):
#     for j in range(len(list) - 1):
#         if list[j] > list[j + 1]:
#             temp = list[j]
#             list[j]=list[j+1]
#             list[j+1]= temp

list = [5,1,4,6,2]

search = 8
search_index = None
for index in range(len(list)):
    data = list[index]
    if data == search:
        search_index = index
        break

if search_index == None:
    print("Not Found")
else:
    print(search_index)




# line = "{name}さんは{age}歳で、{prefecture}出身です。".format(name="佐川",age=20,prefecture="北海道")
# print(line)


# data = "080-5638-4169"
# data = data.replace("-","")
# print(data)