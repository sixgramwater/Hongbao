import re
import sys
import requests
import json



class HttpInfo:
    headers = {
        'Host':
        'h5.ele.me',
        'connection':
        'keep-alive',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent':
        'Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080',
        'Content-Type':
        'text/plain;charset=UTF-8',
        'Referer':
        'https://h5.ele.me/hongbao/'
    }
    predata = {
        "method":
        "phone",
        "group_sn":
        "",
        "sign":
        "",
        "phone":
        "",
        "device_id":
        "",
        "hardware_id":
        "",
        "platform":
        4,
        "track_id":
        "undefined",
        "weixin_avatar":
        "http://thirdqq.qlogo.cn/qqapp/101204453/F790812CAA27B55E343812C0BFEFD29D/40",
        "weixin_username":
        "TEST",
        "unionid":
        "fuck"
    }

    def __init__(self, url, cookies):
        self.jsonInfo = {}
        self.hasPost = False
        self.cookies = cookies
        self.sn = re.findall(r"sn=(.+?)&", url)[0]
        coo_str = str(cookies)
        self.sign = re.findall(r"%22eleme_key%22%3A%22(.+?)%22%", coo_str)[0]
        self.openid = re.findall(r"%22openid%22%3A%22(.+?)%22%", coo_str)[0]
        self.snsid = re.findall(r"snsInfo\[(.+?)\]", coo_str)[0]
        self.post_url = 'https://h5.ele.me/restapi/marketing/promotion/weixin/' + self.openid
        self.predata['group_sn'] = self.sn
        self.predata['sign'] = self.sign
        self.jsonData = json.dumps(HttpInfo.predata)

    def makePost(self):
        r = requests.post(
            self.post_url,
            data=self.jsonData,
            cookies=self.cookies,
            headers=HttpInfo.headers)
        self.jsonInfo = r.json()
        self.hasPost = True

    def getAmount(self):
        if (self.hasPost == False):
            print("Error: You have to post before get amount!")
            return -1
        p_list = self.jsonInfo['promotion_items']
        user_dict = p_list[0]
        amount = user_dict['amount']
        return amount

    def getNum(self):
        if (self.hasPost == False):
            print("Error: You have to post before get num!")
            return -1
        p_list = self.jsonInfo['promotion_records']
        return (len(p_list))

    def updatePhone(self, phone):
        put_url = "https://h5.ele.me/restapi/v1/weixin/" + self.openid + "/phone"
        data = {"sign": self.sign, "phone": phone}
        put_data = json.dumps(data)
        #print(put_data)
        requests.put(put_url, data=put_data, cookies=self.cookies)



class testInfo():
    my_cookies = {
        '_utrace':
        '0d95f3a965e4bf8a1d852cd852b0e1e9_2018-05-01',
        'snsInfo[101204453]':
        "%7B%22city%22%3A%22%22%2C%22eleme_key%22%3A%229d75e8f3dd1eee495f1ff4b3398118ab%22%2C%22figureurl%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F30%22%2C%22figureurl_1%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F50%22%2C%22figureurl_2%22%3A%22http%3A%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22figureurl_qq_1%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%2C%22figureurl_qq_2%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F100%22%2C%22gender%22%3A%22%E7%94%B7%22%2C%22is_lost%22%3A0%2C%22is_yellow_vip%22%3A%220%22%2C%22is_yellow_year_vip%22%3A%220%22%2C%22level%22%3A%220%22%2C%22msg%22%3A%22%22%2C%22nickname%22%3A%22%2Blf%22%2C%22openid%22%3A%2291D6A122F4F5CA321EE90553C25A48DC%22%2C%22province%22%3A%22%22%2C%22ret%22%3A0%2C%22vip%22%3A%220%22%2C%22year%22%3A%220%22%2C%22yellow_vip_level%22%3A%220%22%2C%22name%22%3A%22%2Blf%22%2C%22avatar%22%3A%22http%3A%2F%2Fthirdqq.qlogo.cn%2Fqqapp%2F101204453%2F91D6A122F4F5CA321EE90553C25A48DC%2F40%22%7D",
        'ubt_ssid':
        'sbwha5weklal1cs6qbfo2t49yfs3gl8m_2018-05-01',
        'perf_ssid':
        '4y2y59ew66xfgvqjlbufhq57axc2bo3k_2018-05-01'
    }

    def short2long(self, url):
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
        }
        s = requests.session()
        r = s.get(url, headers=headers, allow_redirects=True)
        pre_req = r.request
        return pre_req.url

    def isShortUrl(self, url):
        return (re.search("url.cn", url) != None)

    def checkAndModify(self, url):
        if (self.isShortUrl(url) == True):
            new_url = self.short2long(url)
        else:
            new_url = url
        return new_url

    def __init__(self, url):
        self.__read_count()
        self.url = self.checkAndModify(url)
        #print(self.url)
        self.lucky_num = int(re.findall(r"lucky_number=(.+?)&", self.url)[0])
        self.cookies_list = []
        self.__import_cookies()
        self.num_of_cookies = len(self.cookies_list)

    def __read_count(self):
        fp = open('data/num.txt', 'r')
        self.count = fp.readlines()[0].split('\n')[0]
        fp.close()

    def __import_cookies(self):
        fp = open('data/cookies.txt', 'r')
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
            if (key_and_value[0] != 'track_id'):
                cook_dict[key_and_value[0]] = key_and_value[1].split('\n')[0]
        self.cookies_list.append(cook_dict)

    def __update_count(self, newCount):
        fp = open('data/num.txt', 'w')
        fp.write(str(newCount))
        fp.close()

    # start from 0: with no check of number
    def pureRun(self):
        for i in range(self.lucky_num - 1):
            # mod
            index = (int(i) + int(self.count)) % self.num_of_cookies
            hi = HttpInfo(self.url, self.cookies_list[index])
            hi.makePost()
            self.count = int(self.count) + 1
        hi = HttpInfo(self.url, self.my_cookies)
        hi.makePost()
        amount = hi.getAmount()
        print("Amount: " + str(amount))
        self.__update_count(self.count)

    def autoRun(self):
        index = (int(self.count)) % self.num_of_cookies
        print(index)
        self.count = int(self.count) + 1

        hi = HttpInfo(self.url, self.cookies_list[index])
        hi.makePost()
        used_num = hi.getNum()
        print("used:" + str(used_num))
        print("sum:" + str(self.lucky_num))
        if (int(used_num) >= int(self.lucky_num)):
            print("Sorry, None Left!")
            self.__update_count(self.count)
            return used_num
        rest_num = self.lucky_num - used_num
        print("rest:" + str(rest_num))

        for i in range(rest_num - 1):
            index = (int(self.count)) % self.num_of_cookies
            hi = HttpInfo(self.url, self.cookies_list[index])
            print("This is the " + str(i + 1) + "try. [index: " + str(index) +
                  "]")
            hi.makePost()
            self.count = int(self.count) + 1

        hi = HttpInfo(self.url, self.my_cookies)
        hi.makePost()
        print("This is the last try.")
        amount = hi.getAmount()
        print("Amount: " + str(amount))
        self.__update_count(int(self.count))

    def advanceRun(self, phone):
        index = (int(self.count)) % self.num_of_cookies
        print(index)
        self.count = int(self.count) + 1

        hi = HttpInfo(self.url, self.cookies_list[index])
        hi.makePost()
        used_num = hi.getNum()
        print("used:" + str(used_num))
        print("sum:" + str(self.lucky_num))
        if (int(used_num) >= int(self.lucky_num)):
            msg = "Used: " + str(used_num) + ", Sum: " + str(
                self.lucky_num) + ", Sorry, None left."
            print("Sorry, None Left!")
            self.__update_count(self.count)
            return msg
        rest_num = self.lucky_num - used_num
        print("rest:" + str(rest_num))

        for i in range(rest_num - 1):
            index = (int(self.count)) % self.num_of_cookies
            hi = HttpInfo(self.url, self.cookies_list[index])
            print("This is the No." + str(i + 1) + " try. [index: " +
                  str(index) + "]")
            hi.makePost()
            self.count = int(self.count) + 1

        hi = HttpInfo(self.url, self.my_cookies)
        hi.updatePhone(phone)
        print("Now updating phone to : " + phone)
        hi.makePost()
        print("This is the last try.")
        amount = hi.getAmount()
        print("Amount: " + str(amount))
        msg = "User: " + str(phone) + ", You get $" + str(amount)
        self.__update_count(int(self.count))
        return msg
