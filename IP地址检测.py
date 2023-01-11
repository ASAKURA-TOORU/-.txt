import requests
import json
import re

print("-" * 80)
print("|" * 80 + "\n")
print(" IP地址检测 | Python 爬虫 | By ASAKURA_TOORU")
print("\n" + "|" * 80)
print("-" * 80)

# 查询请求链接
url = "https://whois.pconline.com.cn/ipJson.jsp?callback=parent.hello"
# 简单反爬, 输入用户信息
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}
# 获取IP地址
ip_address = requests.get(url, headers=headers)
# 截取关键信息
match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_address.text)
start = ip_address.text.find("addr\":\"") + 7
end = ip_address.text.find("\",",start)
if match:
    ip = match.group()
    print(ip)
    print(ip_address.text[start:end])