# Denote Top Ads

[EN](README.md) · ZH · [JA](README.ja.md) · [KO](README.ko.md) · [ES](README.es.md) · [NL](README.nl.md) · [DE](README.de.md) · [FR](README.fr.md)

想为下一轮投放找值得研究的广告素材？Denote 跟踪超过 1,000 万条广告，每周更新榜单。免费账号即可获取游戏或应用在上一个完整自然周的三个榜单，每榜最多 10 条。 [了解 Denote 热门广告](https://denote.net/top-ads)。

![从左侧热门广告导航进入三个周榜。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/top-ads-navigation.jpg)

*从左侧热门广告导航进入三个周榜。*

| 免费榜单 | 能帮你发现什么 |
| --- | --- |
| 热门广告 | 看上周哪些素材最受关注，为创意复盘挑选参考。 |
| 飙升广告 | 看哪些素材的热度比前一周增长最多，及早发现正在起势的创意。 |
| 新晋广告 | 看最近首次出现的素材，并按初期热度挑选新鲜案例。 |

![热门广告：2026 年 11 月 9 至 15 日的游戏广告，按当周热度排序。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/trending-ads.jpg)

*热门广告：2026 年 11 月 9 至 15 日的游戏广告，按当周热度排序。*

![飙升广告：查看哪些游戏广告的热度比前一周增长最多。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/rising-ads.jpg)

*飙升广告：查看哪些游戏广告的热度比前一周增长最多。*

![新晋广告：查看本周新发现的游戏广告及其初期热度排名。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/new-ads.jpg)

*新晋广告：查看本周新发现的游戏广告及其初期热度排名。*

## 获取你的第一份周榜

在 OpenClaw 工作区运行以下命令。此技能需要 Python 3。

```sh
git clone https://github.com/Denote-Business/denote-top-ads.git skills/denote-top-ads
```

1. 开启新会话，问「Denote 能帮我找到哪些值得研究的广告？」
2. [注册免费 Denote 账号](https://denote.net/user/register)。已有账号可直接登录。创建具有 `top_ads:read` 权限的 Denote API 密钥，或为现有密钥添加该权限。
3. 在智能体的密钥设置中将它保存为 `DENOTE_API_KEY`，然后说「给我看看上周的应用广告榜」。智能体会直接展示三个榜单。未指定类别时默认展示游戏广告。

**排名 · 广告标题 · 广告主 · 形式 · 投放平台 · 预览**

## 深入了解一条广告

试着问「打开飙升广告榜的第 2 条」。Top Ads Pro 或 Business 账号可查看该素材已有的表现和受众等详情。三个周榜均可免费查看。

![素材概览：查看 Vita Mahjong 的广告形式和预估展示量。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/overview.jpg)

*素材概览：查看 Vita Mahjong 的广告形式和预估展示量。*

![数据趋势：将 Vita Mahjong 的每日创意得分与参考线对照。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/data-trend.jpg)

*数据趋势：将 Vita Mahjong 的每日创意得分与参考线对照。*

![相关广告：比较使用同一素材的广告主和投放日期。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/related-ads.jpg)

*相关广告：比较使用同一素材的广告主和投放日期。*

![受众分布：按国家或地区、年龄和性别查看 Vita Mahjong 的覆盖人群。](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/audience.jpg)

*受众分布：按国家或地区、年龄和性别查看 Vita Mahjong 的覆盖人群。*
