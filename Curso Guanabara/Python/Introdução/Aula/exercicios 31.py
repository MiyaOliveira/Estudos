n1 = int(input('digite um valor'))
n2 = int(input('digite um valor'))
n3 = int(input('digite um valor'))

if n1 > n2:
    if n1 > n3:
        s1 = n1
        if n2 > n3:
            s2 = n2
            s3 = n3
        else:
            s2 = n3
            s3 = n2
    else:
        s1 = n3
        s2 = n1
        s3 = n2
elif n1 < n2:
    if n2 > n3:
        s1 = n2
        if n1 > n3:
            s2 = n1
            s3 = n3
        else:
            s2 = n3
            s3 = n1
    else:
        s1 = n3
        s2 = n2
        s3 = n1
elif n2 > n3:
    if n2 > n1:
        s1 = n2
        if n3 > n1:
            s2 = n3
            s3 = n1
        else:
            s2 = n1
            s3 = n3
    else:
        s1 = n1
        s2 = n2
        s3 = n3
else:
    print('alguns de seus numeros estao repetidos')

print('o maior valor é {}, o menor é {} e o numero entre eles é {}'.format(s1, s3, s2))