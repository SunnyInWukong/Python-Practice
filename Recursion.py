#simple binary search algorithm practice

def binarySearch(low, high, target, array):  # assuming an ordered array of integers
    mid = int((low + high) /2)
    if(low > high):
        print("the array isn't in order")
    elif(array[mid] == target):
        return True
    elif(target > array[mid]):
        print("a")
        return binarySearch(mid + 1, high, target, array)
    elif(target < array[mid]):
        #print("b")
        return binarySearch(low, mid - 1, target, array)
    elif(low == high):
        return False #the item isnt present in the array

#defining a simple ordered array to search through
n = int(input("enter the size of the array to use"))
arr = []
for i in range(n):  # need to use range() to make it work like a normal for loop
    arr.append(i)
   # print(arr[i])
goal = int(input("define the value you want to determine is present in the array")) # getting the target value
print(binarySearch(arr[0], arr[len(arr)-1], goal, arr)) #test implimentation