# tuple_4 = (1, 2, 3, 4, 5, [10, 20, 30], "hello")
# print(tuple_4[5])
# # a = [10, 20, 30]
# # b = a
# # print(a)
# # print(b)
# # b[1]= 40
# # print(a)
# # print(b)



tuple_4 = (1, 2, 3, 4, 5, [10, 20, 30], "hello")
print(tuple_4[5])
tuple_4[5].append(50)
print(tuple_4)

# tuple_4[2] = 50
# print(tuple_4)

tuple_1 = (1, 2, 3, 4, 5, 6)
list_1 = [1, 2, 3, 4, 5, 6]
print(tuple_1, type(tuple_1), tuple_1.__sizeof__())
print(list_1, type(list_1), list_1.__sizeof__())

new_tuple = list(tuple_1)
print(type(new_tuple))
new_tuple.append(7)
new_tuple = tuple(new_tuple)
print(new_tuple)
print(type(new_tuple))

for i in new_tuple:
    print(i)

