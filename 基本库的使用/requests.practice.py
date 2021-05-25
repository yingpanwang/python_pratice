# 使用requests 进行请求
from typing import Pattern
import requests
import re

# 利用 requests 发起 get,post,delete,put 等请求
req = requests.get('http://httpbin.org/get', params={'name': 'China'})
print(req.json())

req = requests.post('http://httpbin.org/post')
print(req.text)

# 抓取知乎-发现页面网页内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
req = requests.get('https://www.zhihu.com/explore', headers=headers)
print(req.text)

# 使用表达式获取需要的内容
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, req.text)

print(titles)

# 抓取二进制数据

# req = requests.get('https://github.com/favicon.ico',
#                    headers=headers, timeout=30)
# with open('favicon2.ico', 'wb') as f:
#     f.write(req.content)

# 文件上传
files = {
    'file': open('favicon.ico', 'rb')
}
req = requests.post('http://httpbin.org/post', files=files)
print(req.text)

# 不在同一会话
# req = requests.get('http://httpbin.org/cookies/set/number/123456')
# num = requests.get('http://httpbin.org/cookies')
# print(req.text)
# print(num.text)

# 使用session

s = requests.Session()
req = s.get('http://httpbin.org/cookies/set/number/123456')
num = s.get('http://httpbin.org/cookies')
print(req.text)
print(num.text)
