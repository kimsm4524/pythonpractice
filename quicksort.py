def quicksort(arr):
	if len(arr) <= 1:
		return arr
	
	half = int(len(arr)/2)
	pivot = arr[half]
	left = [x for x in arr if x< pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left)+ middle + quicksort(right)
	

print (quicksort([3,1,5,9,2]))
