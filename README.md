#通过scrapy 爬去豆瓣top250电影

1.爬取电影的中文名,导演演员和电影时间等信息

2.爬取评分,以及电影的简介

3.通过pipeline管道类,以及pymongo将爬取的数据存储到mongo数据库中

4.通过重写DownloadMiddlewares给爬虫编写随机User-Agent以及Proxy代理机制


#结合redis以及scrapy 进行分布式爬取新浪网新闻信息 , 爬取下来的信息保存本地文件在spider下的DATA文件夹中

1.爬取当前新闻的祖先连接,标题以及父连接,标题和当前新闻连接

2.爬取当前新闻的标题以及内容

3.根据祖先标题以及父标题创建本地文件夹,并将当前新闻放到对应的文件夹里

4.通过设置settings以及修改spider文件将其改为分布式爬取

5.并将爬取到的item信息存入mongodb中
