"""
图片爬取
"""
import requests
import os
url = "xxx"				#图片地址，可在浏览器中右键获取
root = "F://pic//"			#图片目录
path = root + url.split('/')[-1]	#图片路径
try:
	if not os.path.exists(root):
		os.mkdir(root)		
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)	#.content表示内容的二进制形式
			f.close()
			print("文件保存成功")
	else:
	  print("文件已存在")
except:
	print("爬取失败")

