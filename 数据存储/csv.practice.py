import csv

# 普通写入
with open('practice.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', 'wyp', '15'])
    writer.writerow(['2', 'zlt', '16'])
    writer.writerow(['3', 'lc', '13'])


# 字典写入

with open('practice.csv', 'a') as f:
    # 传入 fields
    writer = csv.DictWriter(f, ['id', 'name', 'age'])
    writer.writeheader()

    wyp = {
        'id': '4',
        'name': 'wyp',
        'age': '15'
    }
    zlt = {
        'id': '5',
        'name': 'zlt',
        'age': '18'
    }
    lc = {
        'id': '6',
        'name': 'lc',
        'age': '32'
    }

    writer.writerow(wyp)
    writer.writerow(zlt)
    writer.writerow(lc)


# 读取csv文件

with open('practice.csv', 'r')as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
