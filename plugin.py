import re
import outCall
# s = "饿了么拼手气，第8个领取的人得大红包https://url.cn/52rZ3Hk来自:饿了么"
# # s = "China's Legend Holdings will split its several business arms to go public on stock markets, the group's president Zhu Linan said on Tuesday.该集团总裁朱利安周二表示，中国联想控股将分拆其多个业务部门在股市上市。"
# result = "".join(i for i in s if ord(i) < 256)
# print(result)
def isUrlInfo(content):
	isShort = re.search("url.cn",content)
	isLong = re.search("h5.ele.me/hongbao/",content)
	return (isShort != None or isLong != None)

def getURL(content):
	return content

def onQQMessage(bot, contact, member, content):
	phone = "15925650514"
	if (isUrlInfo(content)):
		print("检测到链接")
		bot.SendTo(contact, '检测到红包链接')
		# 调用抢红包程序
		url = getURL(content)
		msg = outCall.start(url, phone)
		bot.SendTo(contact, msg)


# content = "饿了么拼手气，第7个领取的人得大红包https://url.cn/5pIuuOC来自:饿了么"
# print(isUrlInfo(content))