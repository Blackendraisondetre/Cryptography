def hydrocefal(seq:list,number:int):
    govno = [i for i,val in enumerate(seq) if val==1]
    print(govno)

    for x in range (number):
        zaloopa = 0
        for y in govno:
            zaloopa ^= bol_fun[y]
        bol_fun.append(zaloopa)
        print(zaloopa)

        for z in range(len(govno)):
            govno[z] += 1

    print(f'The final sequence is = {bol_fun}')


bol_fun = [1,0,0,0,0,0,0,1,0,0,1]
hydrocefal(bol_fun,10)