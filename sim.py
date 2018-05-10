# encoding=utf8  
import requests
import json
import re

# 红包url => sn => 组装 => post时的data
# cookies => 一串数字 => 组装 => post时的url
# 
# url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=7&track_id=&platform=4&sn=29f28217452ea89b&theme_id=2393&device_id=&refer_user_id=22591556'
# test='https://h5.ele.me/restapi/marketing/promotion/weixin/F790812CAA27B55E343812C0BFEFD29D'

def url_to_sn(url):
	snList = re.findall(r"sn=(.+?)&",url) # 使用正则表达式提取出sn的值
	return snList[0]

def cookie_to_sign(cookies):
	coo_str = str(cookies)
	signList = re.findall(r"%22eleme_key%22%3A%22(.+?)%22%", coo_str)
	return signList[0]

def cookie_to_openid(cookies):
	coo_str = str(cookies)
	signList = re.findall(r"%22openid%22%3A%22(.+?)%22%", coo_str)
	return signList[0]


def cookie_to_snsID(cookies):
	coo_str = str(cookies)
	snsIDList = re.findall(r"snsInfo\[(.+?)\]", coo_str)
	return snsIDList[0]


def makeUrl(openid):
	post_url = 'https://h5.ele.me/restapi/marketing/promotion/weixin/' + openid
	return post_url

def makeData_to_json(sn, sign):
	data = {
		"method": "phone",
		"group_sn": sn,
		"sign": sign,
		"phone": "",
		"device_id": "",
		"hardware_id": "",
		"platform": 4,
		"track_id": "undefined",
		"weixin_avatar": "http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40",
		"weixin_username": "TEST",
		"unionid": "fuck"
	}
	jsonData = json.dumps(data)
	return jsonData



def makePost(url, cookies):
	sn = url_to_sn(url)
	sign = cookie_to_sign(cookies)
	openid = cookie_to_openid(cookies)
	postUrl = makeUrl(openid)
	jsonData = makeData_to_json(sn, sign)
	headers = {'Host':'h5.ele.me','connection':'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080','Content-Type':'text/plain;charset=UTF-8','Referer':'https://h5.ele.me/hongbao/'}
	r = requests.post(postUrl, data = jsonData, cookies=cookies, headers=headers)
	print(r.content)


# url3 = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=5&track_id=&platform=4&sn=29efd165bf2fb082&theme_id=569&device_id=&refer_user_id=1461052906'
# headers = {
# 	'Host':'h5.ele.me',
# 	'connection':'keep-alive',
# 	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080',
# 	'Content-Type':'text/plain;charset=UTF-8',
# 	'Referer':'https://h5.ele.me/hongbao/',

# 	}
# cookies = {
# 	'_utrace':'488cbb1aae8098ff3e29c43ac2ff3736_2018-04-30',
# 	'snsInfo[101204453]':"%7B%22city%22%3A%22%22%2C%22eleme_key%22%3A%222801cacd91d87a664f74a87081bb5de0%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FF790812CAA27B55E343812C0BFEFD29D%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FF790812CAA27B55E343812C0BFEFD29D%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2FF790812CAA27B55E343812C0BFEFD29D%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FF790812CAA27B55E343812C0BFEFD29D%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FF790812CAA27B55E343812C0BFEFD29D%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22TEST%22%2C%22openid%22%3A%22F790812CAA27B55E343812C0BFEFD29D%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22TEST%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2FF790812CAA27B55E343812C0BFEFD29D%2F40%22%7D",
# 	'ubt_ssid':'manowd33glrjwke0906ksioq5aj2ivyl_2018-04-30',
# 	'perf_ssid':'8ylvf21owzfp51v710b14z3l8c9koj2w_2018-04-30'
# }

# data = {
# 	"method": "phone",
# 	"group_sn": "29f2867888adf0ba",
# 	"sign": "2801cacd91d87a664f74a87081bb5de0",
# 	"phone": "",
# 	"device_id": "",
# 	"hardware_id": "",
# 	"platform": 4,
# 	"track_id": "undefined",
# 	"weixin_avatar": "http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40",
# 	"weixin_username": "TEST",
# 	"unionid": "fuck"
# }

# data2={
# 	"method": "phone",
# 	"group_sn": "29efc115b52fb0ef",  
# 	"sign": "2801cacd91d87a664f74a87081bb5de0",   
# 	"phone": "",
# 	"device_id": "",
# 	"hardware_id": "",
# 	"platform": 4,
# 	"track_id": "undefined",
# 	"weixin_avatar": "http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40",
# 	"weixin_username": "TEST",
# 	"unionid": "fuck"
# }

# data3={
# 	"method": "phone",
# 	"group_sn": "29f28881d92fe8ef",  # 来自于URL
# 	"sign": "2801cacd91d87a664f74a87081bb5de0",   #来自于cookies->elem_key
# 	"phone": "",
# 	"device_id": "",
# 	"hardware_id": "",
# 	"platform": 4,
# 	"track_id": "undefined",
# 	"weixin_avatar": "http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40",
# 	"weixin_username": "TEST",
# 	"unionid": "fuck"
# }


# jsonData = json.dumps(data3)

# r = requests.post(test, data = jsonData, cookies=cookies, headers=headers)

# print(r.content)


# openid = cookie_to_openid(cookies)
# print(openid)


# {"city":"",
# "eleme_key":"2801cacd91d87a664f74a87081bb5de0",  
# "figureurl":"http://qzapp.qlogo.cn/qzapp/101204453/F790812CAA27B55E343812C0BFEFD29D/30",
# "figureurl_1":"http://qzapp.qlogo.cn/qzapp/101204453/F790812CAA27B55E343812C0BFEFD29D/50",
# "figureurl_2":"http://qzapp.qlogo.cn/qzapp/101204453/F790812CAA27B55E343812C0BFEFD29D/100",
# "figureurl_qq_1":"http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40",
# "figureurl_qq_2":"http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/100",
# "gender":"男",
# "is_lost":0,
# "is_yellow_vip":"0",
# "is_yellow_year_vip":"0",
# "level":"0",
# "msg":"",
# "nickname":"TEST",
# "openid":"F790812CAA27B55E343812C0BFEFD29D",
# "province":"",
# "ret":0,
# "vip":"0",
# "year":"0",
# "yellow_vip_level":"0",
# "name":"TEST",
# "avatar":"http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40"}

