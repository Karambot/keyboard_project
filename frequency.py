import re
import json
import copy
text_list = ['eng','cano','crime','gatsby','selfish','ggs','hunger']
freqObj = {
    "total":0
}

letterObj = {
    'total' : 0
}

for t in text_list:
    with open(f'D:/sci/freq_doc/{t}.txt',encoding='utf-8') as doc:
        
        for i in doc:
            reg = re.compile('[^a-zA-Z ]+')
            i = re.sub(reg, '',i.strip())
            i = re.sub(' ', '@', i).lower() #문서 정리 - \n 제거, 띄어쓰기 치환
            for j in range(len(i)):
                letterObj['total'] +=1
                if i[j] in letterObj.keys():
                    letterObj[i[j]]+=1
                else:
                    letterObj[i[j]]=1


           
            for j in range(len(i) - 1):
                #J : 0 ~ len - 2, len - 1개의 단어
                str2 = i[j:j+2] #ap pp pl le e 식
                if str2 in freqObj.keys():
                    freqObj[str2] += 1
                else: 
                    freqObj[str2] = 1
                freqObj['total'] += 1
        print(t)
        


 
saveObj = dict(reversed(sorted(freqObj.items(), key=lambda item: item[1])))
p1 = {}
p2 = {}
for i in saveObj.keys():
    p1[i] = round( 100 * (saveObj[i] / saveObj['total']), 3)


json_object1 = json.dumps(saveObj, indent=4)
# Writing to sample.json
with open("D:/sci/freq_doc/stat_with_space.json", "w") as outfile:
    outfile.write(json_object1)
removedObj = copy.copy(saveObj)
regex = re.compile('[ a-z]')

'''
for k in saveObj.keys() :
    if len(regex.findall(k)) < 2:
        removedObj['total'] -= removedObj[k]
        del removedObj[k]

for i in removedObj.keys():
    p2[i] = round( 100 * (removedObj[i]/removedObj['total']),3)

json_object2 = json.dumps(removedObj, indent=4)
# Writing to sample.json
with open("D:/sci/freq_doc/stat_without_stupid.json", "w") as outfile:
    outfile.write(json_object2) #띄어쓰기를 배제한 2자리 문자열의 빈도수


json_object3 = json.dumps(p1, indent=4)
# Writing to sample.json
with open("D:/sci/freq_doc/stat_space_percent.json", "w") as outfile:
    outfile.write(json_object3)

json_object4 = json.dumps(p2, indent=4)
# Writing to sample.json
with open("D:/sci/freq_doc/stat_without_stupid_space_percent.json", "w") as outfile:
    outfile.write(json_object4)#띄어쓰기를 배제한 2자리 문자열의 빈도수(%)

letterObj = dict(reversed(sorted(letterObj.items(), key=lambda item: item[1])))
json_object5 = json.dumps(letterObj, indent=4)
# Writing to sample.json
with open("D:/sci/freq_doc/letter.json", "w") as outfile:
    outfile.write(json_object5)#알파벳/띄어쓰기의 빈도수'''