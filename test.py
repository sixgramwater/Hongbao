import sim
import re
import sys

url = sys.argv[1]
# url = 'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=10&track_id=&platform=4&sn=29f2998d05adf0ba&theme_id=2441&device_id=&refer_user_id=141201950'
cookies_list = []
my_cookies = {
	'_utrace':'0d95f3a965e4bf8a1d852cd852b0e1e9_2018-05-01',
	'snsInfo[101204453]':"%7B%22city%22%3A%22%22%2C%22eleme_key%22%3A%229d75e8f3dd1eee495f1ff4b3398118ab%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22%2Blf%22%2C%22openid%22%3A%2291D6A122F4F5CA321EE90553C25A48DC%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22%2Blf%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%7D",
	'ubt_ssid':'sbwha5weklal1cs6qbfo2t49yfs3gl8m_2018-05-01',
	'perf_ssid':'4y2y59ew66xfgvqjlbufhq57axc2bo3k_2018-05-01'
}


def str_to_cookies(cookies_str):
	cook_dict = {}
	lines = cookies_str.split('; ')
	for line in lines:
		key_and_value = line.split('=')
		if(key_and_value[0] != 'track_id'):
			cook_dict[key_and_value[0]] = key_and_value[1].split('\n')[0]
	return cook_dict


def str_add_to_list(cookies_str):
	cook_dict = str_to_cookies(cookies_str)
	cookies_list.append(cook_dict)


def url_luckyNum(url):
	luck_list = re.findall(r"lucky_number=(.+?)&", url)
	return int(luck_list[0])

def init():
	f = open('cookies.txt','r')
	for line in f.readlines():
		str_add_to_list(line)
	f.close()


def readNum():
	fp = open('num.txt','r')
	num = fp.readlines()[0].split('\n')[0]
	fp.close()
	return num

def writeNum(num):
	fp = open('num.txt','w')
	fp.write(str(num))
	fp.close()

def start(url):
	init()
	num = readNum()
	lucky_number = url_luckyNum(url)
	for i in range(lucky_number-1):
		sim.makePost(url, cookies_list[(int(i)+int(num))%9])
	sim.makePost(url, my_cookies)
	writeNum(int(num) + int(lucky_number))
	print("Process Complete!")

def test(url):
	print(url)
	init()
	num = readNum()
	lucky_number = 7
	for i in range(lucky_number-1):
		print("read:"+str((int(i)+int(num))%9))
	writeNum(int(num)+ int(lucky_number)-1)
	print("test complete!")

def update_count():
	pass
	

def autorun(url,now):
	init()
	num = readNum()
	lucky_number = url_luckyNum(url)
	times = lucky_number - now
	for i in range(int(times)-1):
		sim.makePost(url, cookies_list[(int(i)+int(num))%9])
	sim.makePost(url, my_cookies)
	writeNum(int(num) + int(lucky_number))
	print("Process Complete!")

start(url)



