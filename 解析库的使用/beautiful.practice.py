from lxml import etree
from bs4 import BeautifulSoup

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
soup = BeautifulSoup(html, 'lxml')
# 格式化美化
print(soup.prettify())

# 选择器
print(soup.a.string)

# 属性选择
print(soup.a.attrs['signer'])
print(soup.a['signer'])
# 标签内容 contents属性
print(soup.ul.contents)

# 子节点 children属性
# for i, child in enumerate(soup.ul.children):
#     print(i, child)

# 孙子节点 descendants
for i, child in enumerate(soup.ul.descendants):
    print('descendants')
    print(i, child)

# 父节点
print('parent \n')
print(soup.li.parent)

# 父节点及祖先节点
print('parents \n')
print(list(enumerate(soup.li.parents)))


# find_all
print('findall \n')
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))


# css 选择器
print('css \n')
for tag in soup.select('li'):
    print(tag)
