def search(arr, x):
    for i in range(0,len(arr),1):
        if arr[i] == x :
         return i
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 40
    result = search(arr,x)
    if result == -1 :
        print("element not found")
    else:
        print("element found")