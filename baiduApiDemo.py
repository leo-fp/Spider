"""
百度/360搜索关键词提交
百度的关键词接口：
	http://www.baidu.com/s?wd=keyword
360的关键词接口：
	http:www.so.com/s?q=keyword
该实例以百度为例
"""
import requests
keyword = "python"
url = "http://www.baidu.com/s"			#注意最后要加上"/s"
try:
	kv = {'wd':keyword}			
	r = requests.get(url,params = kv)	#构造url
	print(r.request.url)			#查看构造的url
	r.raise_for_status()			#当状态码不为200时产生异常
	r.encoding = r.apparent_encoding	#修改编码方式，编码方式由apparent_encoding分析内容后得出
	print(len(r.text))			#输出返回结果长度
except:
	print("爬取失败")
