# 基于电影《雄狮少年》的网络舆情分析 


## 数据来源:爬虫

- 知乎
  - 问题的回答，基本上都爬了，一万个
- 豆瓣
  - 电影短评，4000+
- 百家号
  - 文章
- b站
  - 视频弹幕爬虫,现在有3万，可无限加
  - 视频评论信息，可无限加
- 微博
  - weibo.cn的关键词搜索接口已失效（2021.6.6）
- 小红书
  - 太难 只有app端
- 百度贴吧、虎扑
  - 结构复杂，难写
- 猫眼
  - 数据量少，不适合
- 知网
  - 数据量太少
- IMDb电影数据
  - 用来比较豆瓣上对雄狮少年的评分是否合理
  - 对两组数据做了个线性回归，是合理的

## 大数据算法

- wordcount（使用jieba做中文词频，然后做词云图)
- LDA（主题聚类）
- TF-IDF（关键词）
- K-means
- 线性回归

## 总结论

知乎等平台和豆瓣等平台之间对该电影的两极分化评价反映了当前网络环境难以达成共识，不同平台具有不同的用户画像及网络回声室等社会现象。

## 后续

还有很多没做的东西，时间有限就没做全，下次一定