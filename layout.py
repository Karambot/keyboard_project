import json

alphabet = {
	'a': ['y', -1],
	'b': ['b', -1],
	'c': ['g', 1],
	'd': ['g', -1],
	'e': ['y', 1],
	'f': ['b', 1],
	'g': ['b', -1],
	'h': ['g', -1],
	'i': ['y', -1],
	'j': ['p', 1],
	'k': ['p', 1],
	'l': ['g', 1],
	'm': ['g', 1],
	'n': ['y', 1],
	'o': ['y', -1],
	'p': ['b', 1],
	'q': ['n', -1],
	'r': ['g', -1],
	's': ['g',- 1],
	't': ['y', 1],
	'u': ['g', 1],
	'v': ['p', -1],
	'w': ['b', 1],
	'x': ['p', -1],
	'y': ['b', -1],
	'z': ['n', 1]
}
#눈물의 똥꼬쑈
crossed = {
    'sum':0,
    'list':[]
}

same_hand = {
    'sum':0,
    'list':[]
}
with open('D:/sci/freq_doc/stat_without_stupid.json','r') as doc:
    docJson = json.load(doc)
    key = docJson.keys()
    for i in key:
        f = i[0]
        s = i[1]
        if alphabet[f][1] * alphabet[s][1] == -1:
            crossed['sum'] += docJson[i]
            crossed['list'].append(i)
        elif alphabet[f][1] * alphabet[s][1] == 1:
            same_hand['sum'] += docJson[i]
            same_hand['list'].append(i)
        else:
            #곱 = 0; 미등록된 케이스
            if alphabet[f][1] != 0:
                alphabet[s][1] = -1 / alphabet[f][1]
            elif alphabet[s][1] != 0:
                alphabet[f][1] = -1 / alphabet[s][1]
            else:
                print(f"stuck at {i}: \nneed input of 2 characters(a b)")
                l = input().split(' ')
                alphabet[f][1] = l[0]
                alphabet[s][1] = l[1]


print(f"Done:")

with open("D:/sci/freq_doc/crossed.json",'r') as c:
    tempObj = json.load(c)

with open('D:/sci/freq_doc/stat_without_stupid.json','r') as doc:
    docJson = json.load(doc)
    key = docJson.keys()
'''
while True:
    test = input()
    cross = 0
    onehand = 0
    alphabet = tempObj['alphabet']

    for i in docJson.keys():
        if test in i and i != 'total':
            r = i.replace(test,'')
            if r == '':
                continue
            if alphabet[r][1] * alphabet[test][1] == -1:
                cross += docJson[i]
            else:
                onehand += docJson[i]

    print(cross - onehand)
'''