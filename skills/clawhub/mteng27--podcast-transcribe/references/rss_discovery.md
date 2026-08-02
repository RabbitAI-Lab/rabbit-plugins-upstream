# 播客 RSS Feed 发现方法

## 概述

大多数播客平台都提供 RSS Feed，这是获取播客全部集数信息（标题、音频直链、Show Notes）最可靠的方式。以下是发现 RSS Feed 的几种方法。

## 方法 1: Apple iTunes Search API（推荐）

通过 Apple Podcasts 的搜索接口发现播客的 RSS Feed URL。

### 搜索播客

```
GET https://itunes.apple.com/search?term=播客名称&media=podcast&limit=5
```

示例（Python）：
```python
import requests

resp = requests.get(
    "https://itunes.apple.com/search",
    params={"term": "纵横四海 携隐", "media": "podcast", "limit": 5},
    timeout=15,
)
results = resp.json().get("results", [])
for r in results:
    print(f"名称: {r.get('collectionName')}")
    print(f"作者: {r.get('artistName')}")
    print(f"RSS Feed: {r.get('feedUrl')}")
    print(f"封面: {r.get('artworkUrl600')}")
    print()
```

### 返回字段

| 字段 | 说明 |
|------|------|
| `collectionName` | 播客名称 |
| `artistName` | 作者/主播 |
| `feedUrl` | RSS Feed URL（关键字段） |
| `artworkUrl600` | 封面图片 URL |
| `trackCount` | 总集数 |

## 方法 2: 平台直接查找

### 小宇宙播客
1. 在小宇宙 App 或网页版找到播客
2. 小宇宙播客通常同步到喜马拉雅、Apple Podcasts
3. 使用 iTunes Search API 搜索播客名称，找到对应的 feedUrl

### 喜马拉雅
- 喜马拉雅专辑页面的 RSS Feed 格式: `https://www.ximalaya.com/album/{album_id}.xml`
- album_id 可从专辑页面 URL 获取

### 其他平台
- 大多数播客平台在页面源码中会包含 `<link rel="alternate" type="application/rss+xml" href="...">` 标签
- 使用 WebFetch 抓取播客页面，查找 RSS Feed 链接

## 方法 3: 用户直接提供

用户可能已经知道 RSS Feed URL，直接使用即可。

## RSS Feed 验证

获取到 RSS Feed URL 后，验证其可用性：

```python
import requests
import xml.etree.ElementTree as ET

resp = requests.get(rss_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
root = ET.fromstring(resp.text)
channel = root.find("channel")
items = channel.findall("item")
print(f"播客名称: {channel.findtext('title')}")
print(f"总集数: {len(items)}")
```

## 常见问题

1. **RSS Feed 不可访问**: 某些平台可能限制访问，尝试添加 User-Agent header
2. **音频 URL 需要认证**: 测试音频 URL 是否公开可访问（HEAD 请求）
3. **集数不完整**: RSS Feed 通常包含最近 50-300 集，老集数可能不在 Feed 中
4. **小宇宙特殊性**: 小宇宙 API 需要登录 token，但其内容通常同步到喜马拉雅等平台，可通过这些平台的 RSS Feed 获取
