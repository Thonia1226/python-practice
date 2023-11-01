# This show cases my knowledge of lopp in python identifying and printing out an item in a loop

listfruit=["orange","apple","banana","pineapple","mango","pawpaw","groundnut"]

for i in listfruit:
    if i=="apple":
        print(i)
        listfruit.remove(i)
        
print(listfruit)        
        
        
