def countpair(num,tar):
    count=0
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i]+num[j]==tar:
                count=count+1
    return count
numlist=[2,7,4,1,3,6]
target=int(input("enter your target number: "))
nooftimes=countpair(numlist,target)
print(f"the target of the list is {target}")
print(f"the number of times taken to count {target}:{nooftimes}")
