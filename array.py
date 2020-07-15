arr= [1,2,3]
arr.append('abc')
print (arr)
arr.pop()
print (arr)
arr.reverse()
print (arr)
print (arr.index(3)) #find position
arr.append([4,5])
print (arr[1:3])#slice array 1 to 3(without)
print (arr)
arr[1:3]=[9,10] #change slice
print (arr)
