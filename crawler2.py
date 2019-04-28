import time
import requests
import json


def gettime():
    return int(round(time.time() * 1000))

def request():
    # 用来自定义头部的
    headers = {}
    # 用来传递参数的s
    keyvalue = {}
    # 目标网址(问号前面的东西)
    url = 'http://data.stats.gov.cn/easyquery.htm'

    # 头部的填充
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /' \
                            'Chrome/73.0.3683.103 Safari/537.36'
    # 按网页进行参数的填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0201"}]'
    keyvalue['k1'] = str(gettime())

    # 发出请求，使用get方法，这里使用我们自定义的头部和参数
    # 建立session
    s = requests.session()
    # 在session基础上进行请求
    r = s.post(url, headers=headers, params=keyvalue)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 此时我们就能获取到过去20年的数据
    # 防止出现乱码
    r.encoding = r.apparent_encoding
    # 将结果转化为json
    res = json.loads(r.text)
    print(res)
    return res


if __name__ == '__main__':
    request()
