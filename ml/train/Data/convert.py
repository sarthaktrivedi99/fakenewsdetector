import json
import os
label=[0,1]
json_list = os.listdir()
j=0
final_dic = {}
final_list = []
file = open("fake.txt",'w')
for i in json_list:
    item_dic={}
    item_dic["file"] = i
    try:
    	item_dic['label'] = label
    	item_dic['text'] = json.loads(open(i, 'r').read())['text']
    	final_list.append(item_dic)
    except:
        continue
    j=j+1
file.write(json.dumps(final_list))
file.close()
