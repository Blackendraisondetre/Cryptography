d = 50
dd = d - 10
bol_fun = [0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0]
cipher = [1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0]
lists = [[1,1,0,1,0,0,0],[1,1,0,0,1,0,0],[1,1,1,1,0,1,0],[1,1,0,0,0,0,1]]

def ones(length: int) -> list:
    return [1 for x in range (length)]
def matrification(seq:list, size:int) -> str:
    ans = ''
    for x in range(int(len(seq)/size)):
        ans += converter(seq[x*size:(x+1)*size])
    return ans
def converter(word:list) -> chr:
    return chr(int(''.join(map(str, word)), 2)+1040)
def gf(polynom:list):
    container = []
    for iter in polynom:
        iv = ones(d)
        a = [x for x in range (len(iter)) if iter[x] == 1]
        for x in range (dd):
            nonce = 0
            for y in a[:-1]:
                nonce ^= iv[y+x]
            iv[a[-1] + x] = nonce
        container.append(iv)

    truth_table = [bol_fun[int(str(container[3][x]) + str(container[2][x]) + str(container[1][x]) + str(container[0][x]), 2)] for x in range(d)]
    answer = [cipher[x] ^ truth_table[x] for x in range(len(cipher))]

    print(matrification(answer, 5))

gf(lists)