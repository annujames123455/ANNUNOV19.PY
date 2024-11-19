my_list=[1,2,3,4,2,4,6,7,6]
unique_list=[]
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
print("the original list is:",my_list)
print(unique_list)