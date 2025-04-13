for x in '0123456789abcdefghijklmnopr':
    n1 = int ('42' + x + '731', 27)
    n2 = int ('5' + x + '98' + x + '3', 27)
    n3 = int ('94' + x+ '726', 27)
    r = n1 + n2 +n3
    if r %26==0:
        print(r //26)
