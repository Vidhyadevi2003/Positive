def Positive(num):
    if num>0:
        return True
num=[12,-7,5,64,-14]
result=filter(Positive,num)
print(list(result))
