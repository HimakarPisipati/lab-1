def hoc(s):
    t = {}
    for char in s:
        if char.isalpha():  
            char = char.lower()  
            if char in t:
                t[char] += 1
            else:
                t[char] = 1
    mchar = ''
    mcount = 0
    for char, count in t.items():
        if count > mcount:
            mcount = count
            mchar = char
    return mchar, mcount
input_str = "hippopotamus"
char, count = hoc(input_str)
print(f"The maximally occurring character is '{char}' and the count is {count}.")
