#通过scrapy 爬去豆瓣top250电影

1.爬取电影的中文名,导演演员和电影时间等信息

2.爬取评分,以及电影的简介

3.通过pipeline管道类将爬取的数据存储到mango数据库中

4.通过重写DownloadMiddlewares给爬虫编写随机User-Agent以及Proxy代理机制
