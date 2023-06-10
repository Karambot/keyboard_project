import numpy
from itertools import permutations
import json

keyboard = {
    #키보드 json (layout으로부터 ㄱㄱ), 형식: left[...], right[...], 각 알파벳의 좌표(array)
    "left" : {
        "sign":1,
        "y" : [["t","e","n"],(0, 1, 2)], #좌표 index. for문에서 섞어서 1대1대응 시킬 것
        "g": [["l","u","m","c"],(2, 1, 3, 0)],
        "b": [["f","w","p"],(2, 1, 0)],
        "p" : [["k"],[0]],
        "n": [['z'],[0]]
    },
    "right":{
        "sign":-1,
        "y" : [["i","a","o"],(0, 1, 2)],
        "g": [["d","h","r","s"],[3, 2, 1, 0]],
        "b": [["g","b","y"],(1, 2, 0)],
        "p" : [["x"],[0]],
        "n": [['q'],[0]]
    },
    "axis": {
        #경우의 수를 따질 좌표들: y, g, b그룹 
        "y" : [[2, 6], [4, 6], [6, 6]],
        "g": [[2, 3],[4, 3],[3,9],[5,9]],
        "b": [[7, 9],[6,10],[6,3]],
        "p" : [[1, 9]],
        "n" : [[9, 9]]
    }
    }
r = ["i","a","o","right", "d","h","r","s", "g","b","y",'placeholder', "x",'placeholder','placeholder','placeholder', 'q']
l = ["t","e","n","left","l","u","m","c","f","w","p",'placeholder',"k",'placeholder','placeholder','placeholder','z']#'placeholder': index를 4의배수로 맞추기 위해 넣음
q = ['y','g','b','p','n'] #몫과 나머지를 이용해 문자의 위치 정의

with open("D:/sci/freq_doc/stat_with_space.json", "r") as c:
    dataObj = json.load(c)
    char_list = dataObj.keys()
minimum = {}
min_value = 10000000000000000 #super large number
count = 0
value = 0

def fitts(a, b):
    #a, b: 글자 (같은 손)
   # print(a, b)
    charlist = [a, b]
    hand = []
    if a in l:
        hand = l
    else:
        hand = r
    j = []
    #print(hand[3])
    for i in charlist:
        quotient = q[hand.index(i) // 4]
        remainder = (hand.index(i) % 4) #r, l의 4번째를 left, right로함 
        
        j.append(numpy.array(keyboard["axis"][quotient][ keyboard[hand[3]] [quotient] [1] [remainder] ]))


    return numpy.linalg.norm(j[0] - j[1])

def isSameHand(a, b):
    #a, b: char, a와 b는 v/j가 아님
    if a in l:
        a = -1
    else: a = 1
    if b in l:
        b = -1
    else: b = 1
    return a * b

def fitts_sbar(char):
    #스페이스바까지의 거리 계산; 글자를 받음
    if char in l:
        hand = l
    else:
        hand = r
    
    quotient = q[hand.index(char) // 4]
    remainder = (hand.index(char) % 4) - 1 #r, l의 4번째를 left, right로함 
    array = numpy.array(keyboard["axis"][quotient][keyboard[hand[3]][quotient] [1] [remainder]])
    if abs(array[0]) <= 5 :
        return array[1]
    else: 
        array[0] = abs(array[0])
        return numpy.linalg.norm(array - numpy.array([5, 0]))
        
for char in char_list:
    if char == "total": continue
    if not ("v" in char or "j" in char) and char[0] != char[1]:
        #v, j 제외 / 동일입력 제외
        if "@" in char:
            remain = char.replace("@",'')
            value += fitts_sbar(remain) * dataObj[char]
        else:
        #서로 같은 손인 경우에만 value에 추가
            if isSameHand(char[0], char[1]) == 1:
                value += fitts(char[0], char[1]) * dataObj[char]

print(value)