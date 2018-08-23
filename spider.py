"""
简单的爬虫框架
"""
import requests
url = "www.baidu.com"
try:
	kv = {
		'user-agent':'Mozilla/5.0'	#修改请求头
	}
	r = requests.get(url,headers = kv)
	r.raise_for_status()			#当状态码不为200时产生异常
	r.encoding = r.apparent_encoding	#修改编码方式，编码方式由apparent_encoding分析内容后得出
	print(r.text[:1000])			#输出部分内容
except:
	print("爬取失败")
