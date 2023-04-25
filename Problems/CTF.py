import requests
import re
import hashlib
import itertools

def Task_1():
    r = requests.get('https://cc.attacking.systems/?command=list')
    amogus = r.text.split('\n')
    for x in amogus:
        print(x)
        r = requests.get(f'https://cc.attacking.systems/?command=run {x} ls')
        if '.txt' in r.text:
            res = r.text.split('\n')[2:]
            print(f'The flag is {res}')
            r = requests.get(f'https://cc.attacking.systems/?command=run {x} cat flag.txt')
            print(r.text)
            break
def Task_2():
    pattern = re.compile("^(aa.*|.*ee)$")
    ans = ''
    for i, line in enumerate(open('sort_1.txt')):
        for match in re.finditer(pattern, line):
            print('Found on line %s: %s' % (i+1, match.group()))
            ans +=match.group()
    result = hashlib.md5(ans.encode())
    print(result.hexdigest())
def Task_3():
    given_hash = 'fd8b6b5944fcede476bd62989044bd0fa36400e8'
    given_digits = '36979765629224074726367327745686243'
    characters = '0123456789'
    combinations = itertools.product(characters, repeat=5)
    for combination in combinations:
        combination_str = ''.join(combination)
        new = given_digits+combination_str
        result = hashlib.sha1(new.encode()).hexdigest()
        if  given_hash == result:
            print(f'PEREMOHA {new}')
def Task_4():
    s = requests.Session()
    r = s.get(f'https://level03:h4ck3r@tasks.workshop.saarsec.rocks/ws03-python/level05.php')
    soup = r.text

    print(soup)
    secret = soup.find('&')
    formula = soup.find('Please solve for us:')
    secret_1 = soup[secret:formula].rstrip()
    formula_1 = str(eval(soup[formula+20:].rstrip()))

    print(secret_1)
    print(formula_1)

    # Send the POST request
    url = 'https://level03:h4ck3r@tasks.workshop.saarsec.rocks/ws03-python/level05.php'  # Replace with the actual URL
    response = s.post(url, data={'secret': secret_1,'result': formula_1})
    print(response.text)
def Task_5():
    s = requests.Session()
    url = 'https://level03:h4ck3r@tasks.workshop.saarsec.rocks/ws03-python/level06.php'
    r_1 = s.get(url)
    r_2 = s.get(url)
    soup = r_1.text
    soul = r_2.text
    strings_1 = re.findall(r'\b\w{32}\b', soup)
    strings_2 = re.findall(r'\b\w{32}\b', soul)

    for x in strings_2:
        print(x)
        if x not in strings_1:
            print(f'Aeeee, here you are {x}')
            r_3 = s.post(url, data={'new_value': x})
            print(r_3.text)