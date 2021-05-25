
import os
import re
import requests
import json
import time


def get_page(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }
    try:
        response = requests.get(url, headers=headers)
        print(response.text)
        if(response.status_code == 200):
            # with open('maoyan.txt', "w") as f:
            #     f.write(response.text)

            return response.text
    except Exception as e:
        print('网络异常!')
        return None

    return None


def parse_page(html):

    pattern = '<i.*?board-index.*?>(.*?)</i>.*?<img.*?data-src="(.*?)".*?/>.*?name.*?<a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>'

    results = re.findall(pattern, html, re.S)
    for item in results:
        yield {
            '排名': item[0],
            '图片': item[1],
            '片名': item[2],
            '主演': item[3],
            '上映时间': item[4],
            '评分': item[5]+item[6]
        }


def save(content, offset):
    filename = 'maoyan_offset_' + str(offset) + '.txt'
    if os.path.exists(filename):
        print('文件已存在')
        return

    with open(filename, 'a', encoding='utf-8') as f:
        for row in content:
            f.write(json.dumps(row, ensure_ascii=False)+'\n')


def isvalid_page(html):
    # content="猫眼验证中心">
    result = re.search('.*?content="(猫眼验证中心)".*?', html, re.S)

    return result == None or result.group(1) == None


def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset*10)
    html = get_page(url)

    # 模拟数据
    # with open('maoyan.txt') as f:
    #     html = f.read()

    # 是否被反爬虫了
    if not isvalid_page(html):
        print('反爬')
        return
    # 获取分析后的数据
    data = parse_page(html)

    if(data == None):
        print('获取信息失败')
        return

    # 保存
    save(data, offset+1)


if __name__ == '__main__':
    for i in range(10):
        main(i)
        time.sleep(5)
