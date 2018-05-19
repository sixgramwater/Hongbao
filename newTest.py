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
		self.__read_count()
		self.url = url
		self.lucky_num = int(re.findall(r"lucky_number=(.+?)&", url)[0])
		self.cookies_list = []
		self.__import_cookies()
		self.num_of_cookies = len(self.cookies_list)

	def __read_count(self):
		fp = open('num.txt','r')
		self.count = fp.readlines()[0].split('\n')[0]
		fp.close()

	def __import_cookies(self):
		fp = open('cookies.txt','r')
		# each line in the file is a cookie
		# initialize the cookie_list
		for oneCookie in fp.readlines():
			self.__append_cookie_list(oneCookie)  
		fp.close()


	def __append_cookie_list(self, cookies_str):
		cook_dict = {}
		lines = cookies_str.split('; ')
		for line in lines:
			key_and_value = line.split('=')
			if(key_and_value[0] != 'track_id'):
				cook_dict[key_and_value[0]] = key_and_value[1].split('\n')[0]
		self.cookies_list.append(cook_dict)

	def __update_count(self, newCount):
		fp = open('num.txt','w')
		fp.write(str(newCount))
		fp.close()


	# start from 0: with no check of number
	def pureRun(self):
		for i in range(self.lucky_num-1):
			# mod 
			index = (int(i)+int(self.count)) % self.num_of_cookies
			hi = newSim.HttpInfo(self.url, self.cookies_list[index])
			hi.makePost()
			self.count = int(self.count) + 1
		hi = newSim.HttpInfo(self.url, self.my_cookies)
		hi.makePost()
		amount = hi.getAmount()
		print("Amount: "+str(amount))
		self.__update_count(self.count)

	def autoRun(self):
		index = (int(self.count)) % self.num_of_cookies
		print(index)
		self.count = int(self.count) + 1

		hi = newSim.HttpInfo(self.url, self.cookies_list[index])
		hi.makePost()
		used_num = hi.getNum()
		print(used_num)
		if(int(used_num) >= int(self.lucky_num)):
			print("Oops, No chance.")
			self.__update_count(self.count)
			return used_num

		rest_num = self.lucky_num - used_num

		for i in range(rest_num-1):
			index = (int(i)+int(self.count)) % self.num_of_cookies
			hi = newSim.HttpInfo(self.url, self.cookies_list[index])
			hi.makePost()
			self.count = int(self.count) + 1

		hi = newSim.HttpInfo(self.url, self.my_cookies)
		hi.makePost()
		amount = hi.getAmount()
		print("Amount: "+str(amount))
		self.__update_count(int(self.count))

	def test(self):
		index = (int(self.count)) % self.num_of_cookies
		self.count = int(self.count) + 1

		hi = newSim.HttpInfo(self.url, self.cookies_list[index])
		hi.makePost()
		used_num = hi.getNum()
		print("used_num:"+str(used_num))

		if(used_num >= self.lucky_num):
			print("Oops, No chance.")
			self.__update_count(self.count)

		rest_num = self.lucky_num - used_num
		print("rest_num:"+str(rest_num))

		for i in range(rest_num-1):
			print(str(i))

		print("the last one")

		#hi = newSim.HttpInfo(self.url, self.my_cookies)
		#hi.makePost()
		#amount = hi.getAmount()
		#print("Amount: "+str(amount))
		self.__update_count(int(self.count))



	def advanceRun(self, phone="13651516277"):
		index = (int(self.count)) % self.num_of_cookies
		self.count = int(self.count) + 1

		hi = newSim.HttpInfo(self.url, self.cookies_list[index])
		hi.makePost()
		used_num = hi.getNum()

		if(used_num >= self.lucky_num):
			print("Oops, No chance.")
			self.__update_count(self.count)
			return used_num

		rest_num = self.lucky_num - used_num

		for i in range(rest_num-1):
			index = (int(i)+int(self.count)) % self.num_of_cookies
			hi = newSim.HttpInfo(self.url, self.cookies_list[index])
			hi.makePost()
			self.count = int(self.count) + 1

		hi = newSim.HttpInfo(self.url, self.my_cookies)
		hi.makePost()
		amount = hi.getAmount()
		print("Amount: "+str(amount))
		self.__update_count(int(self.count))

#url = sys.argv[1]
url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=9&track_id=&platform=4&sn=29f5766e5aadf0fe&theme_id=1881&device_id=&refer_user_id=141201950'
ti = testInfo(url)
#ti.test()
ti.autoRun()
#ti.pureRun()

#http = newSim.HttpInfo(url, cookies)