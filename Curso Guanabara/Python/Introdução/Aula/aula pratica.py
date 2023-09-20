n1 = int(input('digite um valor'))
n2 = int(input('digite um valor'))
n3 = int(input('digite um valor'))

if n1 > n2 and n2 > n3:
    s1 = n1
    s3 = n3
    s2 = n2
    print('seu maior valor é {}, seu menor é {} e numero entre eles é {}.'.format(s1, s2, s3))

elif n1 > n2 and n2 < n3:
    if n1 > n3:
        s1 = n1
        s3 = n3
        s2 = n2
        print('seu maior valor é {}, seu menor é {} e numero entre eles é {}.'.format(s1, s2, s3))
    else:
        s1 = n3
        s2 = n1
        s3 = n2
        print('seu maior valor é {}, seu menor é {} e numero entre eles é {}.'.format(s1, s2, s3))

elif n1 < n2 and n2 < n3:
    s1 = n2
    s3 = n1
    s2 = n3
    print('seu maior valor é {}, seu menor é {} e numero entre eles é {}.'.format(s1, s2, s3))

elif n1 < n2 and n2 > n3:
    if n1 > n3:
        s1 = n2
        s2 = n3
        s3 = n1
        print('seu maior valor é {}, seu menor é {} e numero entre eles é {}.'.format(s1, s2, s3))
    else:
        s1 = n2
        s2 = n1
        s3 = n3
        print('seu maior valor é {}, seu menor é {} e numero entre eles é {}.'.format(s1, s2, s3))

elif n1 == n2 and n1 != n3:
    print('seu primeiro e segundo valor sao iguais')

elif n1 == n3 and n1 != n2:
    print('seu primeiro e terceiro numero sao iguais')

elif n2 == n3 and n2 != n1:
    print('seu segundo e terceiro numero sao iguais')

elif n1 == n2 and n1 == n3:
    print('seus numeros saos iguais')

else:
    print('digite valores validos')

