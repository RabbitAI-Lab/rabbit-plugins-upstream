# 我好牛开放接口(供本 skill 调用)

Base URL:`https://ai.wohaoniu.com`。鉴权:`Authorization: Bearer whn_…`。全局限流 10 次/分钟/钥匙。

## POST /api/open/geo-check
体:`{ "brand": "品牌名(≤40字)", "category": "品类,可选" }`
回:`{ ok, brand, metrics: { model, total, mentionRate, firstRate, interceptRate, avgRank, sentiment, competitorShare }, reportUrl }`
限:5 次/天/钥匙。免费。约 30-60 秒。

## POST /api/open/ad-hooks
体:`{ "product": "产品与人群描述(5-1500字)" }`
回:`{ ok, text }` —— text 含 10 条钩子与钩子库文件全文。消耗 1 次数,失败自动退还。

## POST /api/open/ad-script
体:`{ "brief": "素材需求(5-2000字)" }`
回:`{ ok, text }` —— text 含分镜表、合规提示、AI 成片管线命令。消耗 1 次数,失败自动退还。

## GET /api/open/credits
回:`{ ok, balance, buyUrl }`。免费。

## 错误码
- 401 密钥无效/已吊销
- 402 次数不足(响应带 buyUrl)
- 429 限流(分钟级或 geo 的天级)
- 400 参数/内容安全未通过(error 为中文原因)
