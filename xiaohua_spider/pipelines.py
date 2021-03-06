# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests

class XiaohuaSpiderPipeline(object):
    def process_item(self, item, spider):
        # 一个大型项目中可能有多个spider和多个pipeline，判断一下确保item进入对应的pipeline中
        if spider.name == 'xiaohua':
            # print(item['folder_name'], item['img_name'], item['img_url'])
            # 创建文件夹
            base_dir = os.path.join(os.path.dirname(__file__), 'IMG')       # D:/xiaohua_spider/IMG
            img_dir = os.path.join(base_dir, item['folder_name'])           # D:/xiaohua_spider/IMG/xxx校花
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)
            img_path = os.path.join(img_dir, item['img_name'])              # D:/xiaohua_spider/IMG/xxx校花/xxx.jpg

            # TODO 先用同步请求方式。scrapy自带异步方式作为作业。
            # 请求
            img_url = item['img_url']
            resp = requests.get(img_url)
            if resp.status_code == 200:
                img_bytes = resp.content
            else:
                print('{}下载失败'.format(img_url))

            # 保存图片
            with open(img_path, mode='wb') as f:
                f.write(img_bytes)
            print('{}保存成功'.format(img_path))

            return item

# class xxxSpiderPipeline():
#     pass