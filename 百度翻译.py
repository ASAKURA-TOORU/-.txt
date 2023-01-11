# Python 激动爬虫

import requests
from colorama import Fore
from operator import itemgetter

print("-" * 80)
print("|" * 80 + "\n")
print(" 百度单词翻译 | Python 爬虫 | By ASAKURA_TOORU")
print("\n" + "|" * 80)
print("-" * 80)

# 单词翻译请求链接
url = "https://fanyi.baidu.com/sug"

# 简单反爬, 输入用户信息
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}

# 获取响应的状态, 注入信息
ping_words = requests.get(url, headers=headers)

# 检查响应状态
if ping_words.status_code == 200:
    print(Fore.GREEN + f"百度翻译当前响应为: {ping_words.status_code} OK")
    print(Fore.RESET)
else:
    print(Fore.RED + f"百度翻译当前状态为: {ping_words.status_code} ERROR")
    print("开始退出程序 ... ")
    exit()

while True:
    try:
        # 变量注入
        keys = input("请输入想要翻译的关键词: ")

        # 发送post请求, 发送的数据必须存放在字典中, 通过data参数传递
        response_words = requests.post(url, data={"kw": keys}, headers=headers)

        # 检查响应状态
        if response_words.status_code == 200:
            # 将服务器返回数据处理为json, 并提取出汉化后的结果
            result = response_words.json()
            # 进行关键词的排序
            sorted_data = sorted(result["data"], key=itemgetter("k", "v"))
            print("以下为单词翻译: ")
            # 在数组中打印出排序后的结果
            for item in sorted_data:
                print(item["v"])
        else:
            print(Fore.RED + f"请求异常, 状态码: {ping_words.status_code}")
            print(Fore.RESET)

        print("\n" + "|" * 80)
        # 继续或退出循环判断
        choice = input("是否继续翻译(y/n)?")
        if choice.lower() != "y":
            break
    except KeyboardInterrupt:
        break