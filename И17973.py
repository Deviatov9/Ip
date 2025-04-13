for x in '0123456789abcdefghijklmn':
    n1 = int('12'+ x + '734',24)
    n2 = int('8'+ x + '95'+x+'3',24)
    n3 = int('24'+x+'796', 24)
    r = n1 + n2 +n3
    if r %23==0:
        print (r//23)
