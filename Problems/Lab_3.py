def Hemming(seq):
    print(f'--------------------------')
    table = []
    num_1, num_2, num_3,num_4 = '','','',''
    seq_num = ''.join([str(i) for i in seq])
    # table
    if len(seq_num) == 2**3:
        for x in range (8):
            bin_num = [i for i in '{0:03b}'.format(x)]
            if bin_num[0] == '1':
                num_1 = '00001111'
            else:
                num_1 = '00000000'
            if bin_num[1] == '1':
                num_2 = '00110011'
            else:
                num_2 = '00000000'
            if bin_num[2] == '1':
                num_3 = '01010101'
            else:
                num_3 = '00000000'
            hmmm = ''.join(str(x) for x in [(ord(a) ^ ord(b)) for a, b in zip(num_1, num_2)])
            again = ''.join(str(x) for x in [(ord(a) ^ ord(b)) for a, b in zip(hmmm, num_3)])
            table.append(again)
        for y in range(8):
            table.append(''.join(['1' if x == '0' else '0' for x in table[y]]))
        for x in range(len(table)):
            print (f'-------  {table[x]}  -------')
    if len(seq_num) == 2 ** 4:
        for x in range(16):
            bin_num = [i for i in '{0:04b}'.format(x)]

            if bin_num[0] == '1':
                num_1 = '0000000011111111'
            else:
                num_1 = '0000000000000000'

            if bin_num[1] == '1':
                num_2 = '0000111100001111'
            else:
                num_2 = '0000000000000000'

            if bin_num[2] == '1':
                num_3 = '0011001100110011'
            else:
                num_3 = '0000000000000000'

            if bin_num[3] == '1':
                num_4 = '0101010101010101'
            else:
                num_4 = '0000000000000000'

            hmmm = ''.join(str(x) for x in [(ord(a) ^ ord(b)) for a, b in zip(num_1, num_2)])
            again = ''.join(str(x) for x in [(ord(a) ^ ord(b)) for a, b in zip(num_3, num_4)])
            not_again = ''.join(str(x) for x in [(ord(a) ^ ord(b)) for a, b in zip(hmmm, again)])
            table.append(not_again)
        for y in range(16):
            table.append(''.join(['1' if x == '0' else '0' for x in table[y]]))
        for x in range(len(table)):
            print(f'-------  {table[x]}  -------')

    #matching
    print(f'--------------------------')
    print (f'-------  {seq_num}  -------')
    print(f'--------------------------')
    min = 8
    for x in table:
        num = ''.join(str(x) for x in [(ord(a) ^ ord(b)) for a, b in zip(x, seq_num)]).count('1')
        print(num)
        if min > num:
            min = num
    print(f'Відстань нелінійності = {min}')

#seq = [1,0,0,1,1,0,0,1]
seq = [1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0]

Hemming(seq)