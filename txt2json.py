# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2021-05-09 14:55:12
# @Last Modified by:   cyang
# @Last Modified time: 2021-05-09 16:30:22

import json

in_file = open("microsoft.txt", 'r', encoding='utf-8')
lines = in_file.readlines()
out_file = open('young-1.json', 'w', encoding='utf-8')

jsonList = []

for line in lines:
	word, description = line.split('	')
	out_dic = {}
	out_list = []
	out_dic['name'] = word
	out_list.append(description.split('\n')[0])
	out_dic['trans'] = out_list
	jsonList.append(out_dic)

print(len(jsonList))	
print(jsonList)	
out_json = json.dumps(jsonList, indent = 4, ensure_ascii = False)	
out_file.write(out_json)
in_file.close()
out_file.close()




