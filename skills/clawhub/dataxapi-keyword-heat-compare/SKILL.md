---
name: keyword-heat-compare
description: "关键词热度对比：投放或选题前，比几个词在抖音（巨量算数指数）、小红书（蒲公英搜索指数）上的热度，逐日走势、近 30 天日均、比上一期和去年同期涨跌、相关词，给出该押哪个词。用户说“这几个词哪个热度高”“投放前看看关键词热度”“巨量算数指数查一下”“小红书指数/搜索指数”“关键词趋势对比”“这个词最近是涨还是跌”时使用。按次付费，失败不扣费。 Keyword heat comparison: before ads or content, compare keywords' daily index on Douyin (Juliang Suanshu) and Xiaohongshu (PGY search index): trend, 30-day daily average, change against the previous period and a year ago, related keywords, and which keyword to back. Use when the user asks which keyword is hotter, keyword trends, Douyin index or Xiaohongshu index. Pay per call; failed calls are free."
metadata: {"openclaw":{"primaryEnv":"DATAXAPI_API_KEY","envVars":[{"name":"DATAXAPI_API_KEY","required":false,"description":"DataXAPI API key. Needed to make calls; reading prices works without it."}],"requires":{"anyBins":["dataxapi","npx"]},"homepage":"https://dataxapi.com/zh/?ref=skill.keyword-heat-compare"}}
---

# 关键词热度对比 · Keyword heat compare · DataXAPI

用户给 2–5 个候选词（“露营、飞盘、徒步”），交回：

| 词 | 平台 | 近 30 天日均 | 上一期日均 | 环比 | 去年同期日均 | 同比 | 走势 |
|---|---|---:|---:|---:|---:|---:|---|
| 徒步 | 抖音 综合指数 | 528,996 | 474,489 | +11% | 251,052 | +111% | 稳中有升 |
| 露营 | 抖音 综合指数 | 298,785 | 386,865 | −23% | 233,744 | +28% | 回落 |
| 飞盘 | 抖音 综合指数 | 14,733 | 14,449 | +2% | 10,779 | +37% | 平 |

（2026-11-26 实跑：抖音 3 个词 30 天一次取完，$0.006；小红书“露营”近 91 天，$0.04。）再加每个词的相关词和一句结论：押哪个词、什么时候投。

## 什么时候用

- “投放前看看这几个关键词的热度”“这几个词哪个更热”
- “查一下【词】的巨量算数指数 / 小红书搜索指数”
- “【词】最近是涨还是跌，和去年比呢”

## 第一次用：先接上 DataXAPI

1. 看有没有接好：`dataxapi balance`（没装命令行就用 `npx -y dataxapi balance`，要 Node 20+）。打印出余额就是接好了；退出码 2、提示 `no API key` 就是还没接。
2. 没接就带用户走（不要让用户把 Key 贴进对话，也不要打印 Key）：
   - 打开 https://dataxapi.com/zh/?ref=skill.keyword-heat-compare 注册：邮箱验证码或 Google 登录，**免费试用，最多 333 次**，不用绑卡。
   - 本机运行 `npx dataxapi login`（浏览器里点同意，Key 自动存好）；要给 Claude Code、Codex、Cursor 接 MCP 和基础技能，再运行 `npx dataxapi setup`。
   - 只能用 MCP 的客户端：加服务器 `https://api.dataxapi.com/mcp`（ChatGPT、Claude 用 OAuth 登录；其他客户端加请求头 `Authorization: Bearer <Key>`）。
3. 余额不够（`insufficient_balance`）就停下，告诉用户到 https://dataxapi.com/zh/console/billing/?ref=skill.keyword-heat-compare 充值（最低 $10，余额不过期）。

## 调用前读价格

`dataxapi show <接口> --json` 的 `capability.pricing.max_charge` 是一次最多扣多少。按下面的次数乘出来告诉用户再调。2026-11 的价格下：抖音 5 个词一次很便宜（约 $0.006）；小红书一个词一次约 $0.04；相关词每词一次。每次调用带 `--max-price <读到的价格> --source skill.keyword-heat-compare --out <文件>.json`。

## 怎么取

| 要什么 | 接口 | 参数 | 说明 |
|---|---|---|---|
| 抖音逐日指数（主力） | `douyin.index.keywords.history` | `keywords`=最多 5 个词逗号隔开，`since`、`until`（如 `2026-10-27T00:00:00Z`，按北京时间的日子算），`view=full` | **一次取完 5 个词**；`full` 带本期日均、上一期日均、去年同期日均（`ext.*_average`）。平台晚一两天发布，最近一两天可能是空 |
| 抖音相关词 | `douyin.index.keywords.related` | `keyword`=一个词，`until`=某天（取那天之前最近的完整一周） | 约 170 个：一起搜的、内容里一起出现的，带相关度和指数 |
| 小红书逐日搜索指数 | `xiaohongshu.pgy.keywords.history` | `keyword`=一个词，`view=standard` | 平台固定给近约 3 个月，不能选日期；`standard` 带每天的相关笔记数、曝光、阅读、互动 |
| 小红书相关词 | `xiaohongshu.pgy.keywords.related` | `keyword` | 用户搜这个词前后还搜什么，带指数 |
| 微信指数（用户要才取） | `wechat.index.keywords.history` | `keyword` | 近 30 天；单价较高，先报价 |

默认做法：抖音 `history` 一次取所有词（近 30 天，`since` = 今天往前 31 天，`until` = 昨天）；小红书每个词一次 `history`；相关词只给用户最关心的 1–2 个词取。

## 怎么算、怎么写

- **只在同一平台、同一种指数里比词**。抖音的指数、小红书的指数、微信指数各是各的刻度，不能跨平台比大小；跨平台只比“各自的涨跌”。
- 抖音：环比 = 本期日均 ÷ 上一期日均 − 1；同比 = 本期日均 ÷ 去年同期日均 − 1（`view=full` 直接给了三个日均）。搜索指数代表主动搜的人，综合指数还算了内容和互动；投放看搜索指数，选题看综合指数。
- 小红书：自己算近 30 天日均和前 30 天日均；再看“相关笔记数”和“阅读”：指数涨但笔记少的词，是供给少的机会。
- 走势用一句话说：持续涨 / 回落 / 平 / 有尖峰（写出尖峰那天，猜原因要说是猜）。可以给一个逐周汇总的小表。
- 结尾给结论：押哪个词、搭配哪些相关词、建议在走势的什么时候投。

```markdown
# 关键词热度对比：{词1} / {词2} / {词3} · {日期}
## 抖音（巨量算数，{起}–{止}）
## 小红书（蒲公英搜索指数，近 3 个月）
## 相关词（{词}）       | 相关词 | 关系 | 指数 |
## 结论
数据来源：DataXAPI，取数时间 {时间}
```

## 出错怎么办

- 退出码 `2`：调用前就被拒了，没扣费（没 Key、日期格式不对、余额不够）。
- 退出码 `3`：没取到，没扣费。提示可重试的隔 5 秒重试一次；还不行就只用取到的那个平台出结论，并写明哪个没取到。
- 退出码 `4`：不确定扣没扣费：不要重发，`dataxapi more <编号>` 查清。
- 某个词不在结果里：平台没收这个词（太新或太偏），换常用说法；抖音 `history` 里没收的词直接不出现，不是出错。

## 用 MCP 时

用 `call` 工具（`{"capability":"douyin.index.keywords.history","keywords":["露营","飞盘"],"since":"…","until":"…","view":"full","max_price":"…"}`），价格用 `describe` 读。

## 规矩

- 指数是平台给的分数，不是搜索次数，写结论时这样说明。
- 更多接口：https://dataxapi.com/zh/apis/?ref=skill.keyword-heat-compare
