import re

# **********************************************************************************

content = 'Hello 123 4567 World_This is a Regex Demo'

# ^xxx 匹配xxx开头的字符
# \s 匹配空格
# \w 匹配字母，数字，下划线
# \d 匹配数字
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)

# **********************************************************************************

# 使用group 获取（）分组数据
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld(.*)', content)

print(result)
print(result.group(1))
print(result.group(2))

# **********************************************************************************

# 通用匹配
# .表示匹配任意字符
# *表示前面字符匹配无限次
result = re.match('^Hello.*Demo$', content)
print(result)

# **********************************************************************************

# 贪婪非贪婪

result = re.match('^He.*(\d+).*Demo$', content)
print(result)
# 会发现只有7，因为 He后的.*会尽可能匹配多的字符 且 \d+ 表示至少一个 所以 会查找到123456 而保留一个7
print(result.group(1))
# .*?表示非贪婪模式
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.span())
# 会发现只有7，因为 He后的.*会尽可能匹配多的字符 且 \d+ 表示至少一个 所以 会查找到123456 而保留一个7
print(result.group(1))


# **********************************************************************************

# 使用修饰符控制匹配模式
# re.S使.匹配包括换行在内的字符
content = '''Hello 1234567 World_This 
is a Regex Demo'''

result = re.match('^He.*?(\d+).*Demo$', content, re.S)
print(result.group(1))

# **********************************************************************************

# 转义

content = '(百度)www.baidu.com'

result = re.match('\(百度\)www\.baidu\.com', content, re.S)
print(result.group())

# **********************************************************************************

# search

content = '我要看百度'

result = re.search('百度', content)
print(result)

# **********************************************************************************
# 查找html

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introducation">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" signer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" signer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" signer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" signer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" signer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>
'''

result = re.search('<li.*?active.*?signer="(.*?)">(.*?)</a>', html, re.S)
print(result.group(1), result.group(2))

# findall

results = re.findall(
    '<li.*?href="(.*?)".*?signer="(.*?)">(.*?)</a>', html, re.S)
print(results)
for result in results:
    print(type(result))
    print(result[0], result[1], result[2])
