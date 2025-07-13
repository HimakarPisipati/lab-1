def calrange(numr):
    if len(numr)<3:
        return "the range is invalid"
    max1=max(numr)
    min1=min(numr)
    therange=max1-min1
    return therange
listnum=[2,1,3,4,8,9]
res=calrange(listnum)
print(f"the range of numbers is {res}")