#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入相应的库文件
from bs4 import BeautifulSoup
import requests
import csv
import time

# 加入请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


# 定义获取网页信息的函数
def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    tittles = soup.select('._3_JaaUmGUCjKZIdiLhqtfr')
    dates = soup.select('._3TzAhzBA-XQQruZs-bwWjE')
    # 阅读数
    uvs = soup.select('._2gvAnxa4Xc7IT14d5w8MI1')

    #图片链接
    imgs = soup.select('._2ahG-zumH-g0nsl6xhsF0s')
    imgs=imgs[12:-1]
    imgs=imgs[::3]


    for tittle, date, uv, img in zip(tittles, dates, uvs, imgs):
        print(tittle.get_text().strip())
        print(date.get_text().strip())
        print(uv.get_text().strip())

        print(img.select('img')[0].get('src'))

        data = [
            img.select('img')[0].get('src'),
            tittle.get_text().strip(),
            date.get_text().strip(),
            uv.get_text().strip()
        ]
        csv_writer.writerow(data)


# 为程序的主入口
if __name__ == '__main__':

    f = open('spider.csv','w',newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(["图片链接", "标题", "日期","阅读数"])


    urls = ['https://www.aquanliang.com/blog/page/{}'.format(number) for number in range(1, 59)]  # 构造多页URL
    for single_url in urls:
      get_info(single_url)  # 循环调用get_links()函数
      time.sleep(1)  # 睡眠2秒
