import newSim
import re
import sys

class testInfo():
	my_cookies = {
		'_utrace':'0d95f3a965e4bf8a1d852cd852b0e1e9_2018-05-01',
		'snsInfo[101204453]':"%7B%22city%22%3A%22%22%2C%22eleme_key%22%3A%229d75e8f3dd1eee495f1ff4b3398118ab%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22%2Blf%22%2C%22openid%22%3A%2291D6A122F4F5CA321EE90553C25A48DC%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22%2Blf%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%7D",
		'ubt_ssid':'sbwha5weklal1cs6qbfo2t49yfs3gl8m_2018-05-01',
		'perf_ssid':'4y2y59ew66xfgvqjlbufhq57axc2bo3k_2018-05-01'
	}

	def __init__(self,url):
		fp = open('num.txt','r')
		self.url = url
		self.count = fp.readlines()[0].split('\n')[0]
		fp.close()
		self.lucky_num = re.findall(r"lucky_number=(.+?)&", url)
		self.cookies_list = []
		self.__init_other_cookies()


	def __init_other_cookies(self):
		fc = open('cookies.txt','r')
		for line in f.readlines():
			self.__init_cookies_list(line)
		fc.close()


	def __init_cookies_list(self, cookies_str):
		cook_dict = {}
		lines = cookies_str.split('; ')
		for line in lines:
			key_and_value = line.split('=')
			if(key_and_value[0] != 'track_id'):
				cook_dict[key_and_value[0]] = key_and_value[1].split('\n')[0]
		self.cookies_list.append(cook_dict)

	def update_count(self, count):
		fp = open('num.txt','w')
		fp.write(str(count))
		fp.close()

	def pureRun(self):
		for i in range(lucky_number-1):
			index = (int(i)+int(num))%9
			oneRequest = newSim.HttpInfo(url, cookies)
			oneRequest.makePost(self.url, cookies_list[index])
		oneRequest = newSim.HttpInfo(self.url, self.my_cookies)

		update_count(self.count)

	def autoRun():
		
		pass



#http = newSim.HttpInfo(url, cookies)