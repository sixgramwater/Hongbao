import requests
import json
import re

class HttpInfo:
	amountList = []
	headers = {'Host':'h5.ele.me','connection':'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080','Content-Type':'text/plain;charset=UTF-8','Referer':'https://h5.ele.me/hongbao/'}
	predata = {"method": "phone","group_sn": sn,"sign": sign,"phone": "","device_id": "","hardware_id": "","platform": 4,"track_id": "undefined","weixin_avatar": "http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40","weixin_username": "TEST","unionid": "fuck"}
	
	def __init__(self, url, cookies):
		self.cookies = cookies
		self.sn = re.findall(r"sn=(.+?)&",url)[0]
		coo_str = str(cookies)
		self.sign = re.findall(r"%22eleme_key%22%3A%22(.+?)%22%", coo_str)[0]
		self.openid = re.findall(r"%22openid%22%3A%22(.+?)%22%", coo_str)[0]
		self.snsid = re.findall(r"snsInfo\[(.+?)\]", coo_str)[0]
		self.post_url = 'https://h5.ele.me/restapi/marketing/promotion/weixin/' + openid
		self.jsonData = json.dumps(HttpInfo.predata)
		#self.backInfo = ""
		#self.amountList = []

	def makePost(self):
		r = requests.post(self.post_url, data = jsonData, cookies=self.cookies, headers=HttpInfo.headers)
		self.jsonInfo = r.json()

	def getAmountList(self):
		amountList = re.findall(r'"amount":(.+?),"', self.backInfo)
		return amountList

	def getAmount(self):
		return self.amountList[0]

	def getNum(self):
		if (len(self.amountList) == 0):
			print("Sorry! The call has not been sent! Please makePost before getNum!")
			return
		return len(self.amountList)-1







