def binarygap(a):
    s=str(bin(((1 << 16) - 1) & a))
    s=s[2:len(s)]
    count=0
    flag=0
    big=0
    for i in range(0,len(s)):
        if s[i]=='1':
            flag+=1
        else:
            count+=1
        if flag==2:
            count += 1
            flag=1
            if count>=big:
                big=count
            count=0
    print(big)


binarygap(0)
binarygap(55)
binarygap(-5)
binarygap(12354)
binarygap(6)
binarygap(256)