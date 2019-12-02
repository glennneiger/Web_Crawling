Id_list=[1,2,3,4,5,6,7]

Contents_list=['a','b','c','d','e','f','g']

A=10

for i in Id_list[0::2]:
    i=A
    A=A+10
    print(i)

print(Id_list)





# Range=len(Contents_list)*2
# Cd=[0 for i in range(Range)]



# for i in range(0,len(Id_list)):
#     a=i*2
#     Cd[a]=Id_list[i]

# for i in range(1,len(Contents_list)+1):
#     a=i*2-1
#     Cd[a]=Contents_list[i-1]

# # for i in range(1,len(Contents_list)):
# #     Cd[2*i-1].append(Contents_list[i])


# print(Cd)

