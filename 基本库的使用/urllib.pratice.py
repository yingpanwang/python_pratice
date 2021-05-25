# urllib包含四个模块
#
# request  用于模拟请求
# error 处理异常
# parse 工具模块，拆分，解析，合并
# robotparser 识别爬虫文件

import urllib.request
import urllib.parse
import socket
import urllib.error

# 通过urlopen 方法获取 HttpResponse对象
# HttpResponse对象 主要包含 read,readinto,getheader等方法 和 一些属性
response = urllib.request.urlopen("https://www.python.org")
print(f'消息:{response.msg},状态:{response.status},是否关闭:{response.closed}')
# 读取 解码
result = response.read().decode('utf-8')

print(result)


# 使用data 传递 参数
# 使用timeout 设置超时,使用try catch捕获异常

data = {
    'word': 'hello'
}
try:
    response = urllib.request.urlopen(
        'http://httpbin.org/post', data=bytes(urllib.parse.urlencode(data), encoding='utf-8'), timeout=0.1)

    print(response.read())

except Exception as e:
    if isinstance(e.reason, socket.timeout):
        print('连接超时')


# 使用 Request 构建请求信息

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'python urllib',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'China'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
req = urllib.request.Request(url, data, headers, method='POST')

response = urllib.request.urlopen(req)
print(response.read())
