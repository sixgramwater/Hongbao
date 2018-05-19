import requests
import json
import re

class HttpInfo:
	headers = {'Host':'h5.ele.me','connection':'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080','Content-Type':'text/plain;charset=UTF-8','Referer':'https://h5.ele.me/hongbao/'}
	predata = {"method": "phone","group_sn": "","sign": "","phone": "","device_id": "","hardware_id": "","platform": 4,"track_id": "undefined","weixin_avatar": "http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40","weixin_username": "TEST","unionid": "fuck"}
	
	def __init__(self, url, cookies):
		self.jsonInfo = {}
		self.hasPost = False
		self.cookies = cookies
		self.sn = re.findall(r"sn=(.+?)&",url)[0]
		coo_str = str(cookies)
		self.sign = re.findall(r"%22eleme_key%22%3A%22(.+?)%22%", coo_str)[0]
		self.openid = re.findall(r"%22openid%22%3A%22(.+?)%22%", coo_str)[0]
		self.snsid = re.findall(r"snsInfo\[(.+?)\]", coo_str)[0]
		self.post_url = 'https://h5.ele.me/restapi/marketing/promotion/weixin/' + self.openid
		self.predata['group_sn'] = self.sn
		self.predata['sign'] = self.sign
		self.jsonData = json.dumps(HttpInfo.predata)

	def makePost(self):
		r = requests.post(self.post_url, data = self.jsonData, cookies=self.cookies, headers=HttpInfo.headers)
		self.jsonInfo = r.json()
		self.hasPost = True


	def getAmount(self):
		if(self.hasPost == False):
			print("Error: You have to post before get amount!")
			return -1
		p_list = self.jsonInfo['promotion_items']
		user_dict = p_list[0]
		amount = user_dict['amount']
		return amount

	def getNum(self):
		if(self.hasPost == False):
			print("Error: You have to post before get num!")
			return -1
		p_list = self.jsonInfo['promotion_records']
		return(len(p_list))

	def updatePhone(self, phone):
		put_url = "https://h5.ele.me/restapi/v1/weixin/" + self.openid + "/phone"
		data = {"sign": self.sign,"phone": phone}
		put_data = json.dumps(data)
		#print(put_data)
		requests.put(put_url, data=put_data, cookies=self.cookies)


#test code
# my_cookies = {
# 	'_utrace':'0d95f3a965e4bf8a1d852cd852b0e1e9_2018-05-01',
# 	'snsInfo[101204453]':"%7B%22city%22%3A%22%22%2C%22eleme_key%22%3A%229d75e8f3dd1eee495f1ff4b3398118ab%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22%2Blf%22%2C%22openid%22%3A%2291D6A122F4F5CA321EE90553C25A48DC%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22%2Blf%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%7D",
# 	'ubt_ssid':'sbwha5weklal1cs6qbfo2t49yfs3gl8m_2018-05-01',
# 	'perf_ssid':'4y2y59ew66xfgvqjlbufhq57axc2bo3k_2018-05-01'
# }
# url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=9&track_id=&platform=4&sn=29f3cfb57fadf0ef&theme_id=2473&device_id=&refer_user_id=141201950'

# hi = HttpInfo(url, my_cookies)
# hi.updatePhone("13651516277")
#hi.makePost()
#print(hi.getAmount())
#print(hi.getNum())



