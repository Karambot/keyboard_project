import numpy
from itertools import permutations
import json

keyboard = {
    #키보드 json (layout으로부터 ㄱㄱ), 형식: left[...], right[...], 각 알파벳의 좌표(array)
    "left" : {
        "sign":-1,
        "y" : [["t","e","n"],[2,1,0]], #좌표 index. for문에서 섞어서 1대1대응 시킬 것
        "g": [["l","u","m","c"],[3, 1, 2, 0]],
        "b": [["f","w","p"],[2, 1, 0]],
        "p" : [["k"],[0]],
        "n": [['z'],[0]]
    },
    
    "right":{
        "sign":1,
        "y" : [["i","a","o"],[0, 1, 2]],
        "g": [["d","h","r","s"],[3, 2, 1, 0]],
        "b": [["g","b","y"],[1, 2, 0]],
        "p" : [["x"],[0]],
        "n": [['q'],[0]]
    },
    "axis": {
        #경우의 수를 따질 좌표들: y, g, b그룹 
        "y" : [[2, 6], [4, 6], [6, 6]],
        "g": [[2, 3],[4, 3],[3,9],[5,9]],
        "b": [[7, 9],[8,6],[6,3]],
        "p" : [[1, 9]],
        "n" : [[9, 9]]
    }
    }
r = ["i","a","o","right", "d","h","r","s", "g","b","y",'placeholder', "x",'placeholder','placeholder','placeholder', 'q']
l = ["t","e","n","left","l","u","m","c","f","w","p",'placeholder',"k",'placeholder','placeholder','placeholder','z']#'placeholder': index를 4의배수로 맞추기 위해 넣음
q = ['y','g','b','p','n'] #몫과 나머지를 이용해 문자의 위치 정의

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

permut_3 = list(permutations([0, 1, 2])) #[(0,1,2),(0,2,1),...]
permut_4 = list(permutations([0, 1, 2, 3]))

'''
for i in range(len(permut_3)):
    permut_3[i] = list(permut_3)

for i in range(len(permut_4)):
    permut_4[i] = list(permut_4)
'''

with open("D:/sci/freq_doc/stat_with_space.json", "r") as c:
    dataObj = json.load(c)
    char_list = dataObj.keys()
minimum = [0] * 6
min_value = 10000000000000000 #super large number
count = 0
value = 0

for ly in range(len(permut_3)):
    
    #왼손 배열 후, 오른손 배열 시작
    keyboard["left"]["y"][1] = permut_3[ly]
    for lg in range(len(permut_4)):
        keyboard["left"]['g'][1] = permut_4[lg]
        for lb in range(len(permut_3)):
            keyboard["left"]['b'][1] = permut_3[lb]
            #왼손 세팅 완료
            for ry in range(len(permut_3)):
                #오른손 배열 시작
                keyboard["right"]["y"][1] = permut_3[ry]
                for rg in range(len(permut_4)):
                    keyboard["right"]['g'][1] = permut_4[rg]
                    for rb in range(len(permut_3)):
                        keyboard["right"]['b'][1] = permut_3[rb]
                        #오른손 세팅 완료
                        count += 1
                        value = 0
                        for char in char_list: #입력시간 * 확률 구간 = 기댓값
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
                                    
                        
                            #print("E")
                        if ( value > 0 ) and (value < min_value ):
                            
                            minimum[0] = keyboard["left"]["y"][1]
                            minimum[1] = keyboard["left"]["g"][1]
                            minimum[2] = keyboard["left"]["b"][1]
                            minimum[3] = keyboard["right"]["y"][1]
                            minimum[4] = keyboard["right"]["g"][1]
                            minimum[5] = keyboard["right"]["b"][1]
                            print(minimum)
                            min_value = value
                        if count % 1000 == 0:
                            print(minimum)
                            print(count)
                            print(min_value)



print(f"Done: {count}")
with open("D:/sci/freq_doc/keyboard.json", "w") as c:
    json_object1 = json.dumps(minimum, indent=4)
    c.write(json_object1)

#최고 효율 [[2,1,0],[3,1,2,0],[2,1,0],[0,1,2],[3,2,1,0],[1,2,0]] 19585386.378527626 -1, 1