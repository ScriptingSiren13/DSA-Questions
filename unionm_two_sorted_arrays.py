def unionarrays(arr1,arr2,m,n):
    i=0
    j=0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            print(arr1[i],end=", ")
            i+=1
        elif arr1[i]>arr2[j]:
            print(arr2[j],end=", ")
            j+=1
        else:
            print(arr1[i],end=", ")
            i+=1
            j+=1

    while i<m:
        print(arr1[i],end=", ")
        i+=1
    while j<n:
     print(arr2[j],end=", ")
     j+=1





arr1=[1,3,4,67]
arr2=[3,5,7,8,9,34,56,68]
m=len(arr1)
n=len(arr2)
unionarrays(arr1, arr2, m,n)
