def add(a, b): #sk3395 26-02-23 (Adds the two numbers or ANS and number)
    z = int(a) + int(b)
    global ans
    ans = z
    print("Result:", ans)


def sub(a, b):#sk3395 26-02-23 (Substracts the two numbers or ANS and number)
    z = int(a) - int(b)
    global ans
    ans = z
    print("Result:", ans)


def mul(a, b):#sk3395 26-02-23 (Multiplys the two numbers or ANS and number)
    z = int(a) * int(b)
    global ans
    ans = z
    print("Result:", ans)


def div(a, b):#sk3395 26-02-23 (Divide the two numbers or ANS and number)
    try:
        z = int(a) / int(b)
        global ans
        ans = z
        print("Result:", ans)
    except:
        print("Enter a valid value, division by 0 error")


ans = 0
while True: #sk3395 26-02-23
    l = input("Enter num(opr)num | ans(opr)num [No spaces in between the num or opr] :").strip()
    br = 0
    flag = 0
    num1, num2, opr = 0, 0, 0
    if "ans" == l[:3]: #sk3395 26-02-23 (if ans(opr)num testcase typed, the code in the IF case runs)
        br = ord(l[3])
        l = l[4:]
        for i in range(len(l)):
            if 48 <= ord(l[i]) <= 57:
                pass
            else:
                print("Enter Valid String eg:( 2+2 or num(opr)num or ans(opr)num)")
                break
        else:
            num1 = ans
            opr = br
            num2 = l
            flag = 1
    else: #sk3395 26-02-23 (if num(opr)num testcase typed, the code in the ELSE case runs)
        for i in range(len(l)):
            if ord(l[i]) in [43, 45, 42, 47] and br != 0:
                print("Enter Valid String eg:( 2+2 or num(opr)num or ans(opr)num)")
                break
            if ord(l[i]) in [43, 45, 42, 47] and br == 0:
                br = i
            else:
                if 48 <= ord(l[i]) <= 57:
                    pass
                else:
                    print("Enter Valid String eg:( 2+2 or num(opr)num or ans(opr)num)")
                    break
        else:
            num1 = int(l[:br])
            opr = ord(l[br])
            num2 = int(l[br + 1:])
            flag = 1
    if flag == 1:
        if opr == 43:
            add(num1, num2)

        if opr == 45:
            sub(num1, num2)

        if opr == 42:
            mul(num1, num2)

        if opr == 47:
            div(num1, num2)
    val = input("Do you want to continue yes/No enter (Y/N or y/n):")
    while True:
        if val in ["Y", 'y', "N", 'n']:
            break
        else:
            val = input("Do you want to continue yes/No enter valid response(Y/N or y/n):")
    if val in ["N", 'n']:
        break
