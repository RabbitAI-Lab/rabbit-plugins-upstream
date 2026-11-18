---
name: jusou-search
description: 用聚搜GO（Jusou）给 Agent 联网搜索：一个 Key 调 8 个搜索引擎（Exa / Tavily / Serper / SerpApi / Brave / 博查 / 百度 / AnySearch），按积分计费、失败不扣分。用户要求联网搜索、查最新信息、找资料、核实事实、多引擎对比，或提到 Tavily/Exa/Serper 替代、聚合搜索时使用。
---

# 聚搜GO 联网搜索

## 什么时候用

- 需要实时/最新信息（新闻、价格、版本、赛程、政策）或训练数据之外的事实
- 找资料、找同类网页、查文档与官网
- 想让多家搜索引擎对比着搜（国内外覆盖互补）

## 准备

环境变量 `JUSOU_API_KEY` = 用户在 https://jusouai.cn 控制台的 Key（形如 `jsk_...`）。
没有 Key 时，提示用户去 jusouai.cn 注册/兑换后把 Key 配到环境变量，不要让用户把 Key 贴在聊天里。

## 怎么搜

优先用随附脚本（零依赖 Python 3）：

```bash
python3 scripts/jusou_search.py "杭州天气"
python3 scripts/jusou_search.py "GPT-5 review" --engine exa --num 5
python3 scripts/jusou_search.py "新能源汽车销量" --engines baidu,bocha,exa --merge
python3 scripts/jusou_search.py "财报" --engine tavily --depth advanced
```

也可以直接调统一接口 `POST https://jusouai.cn/v1/search`（Bearer 鉴权），参数同脚本。

## 选引擎

| 场景 | 引擎 |
|---|---|
| 英文/语义找资料、找相似网页 | `exa` |
| 给模型喂结构化结果 | `tavily` |
| Google 网页/新闻/学术/购物 | `serper` |
| 与 SerpApi 官方同形的 Google 结果 | `serpapi` |
| 独立索引 | `brave` |
| 中文网页（国内站覆盖） | `bocha`、`baidu`（要 AI 生成答案用 baidu 的 advanced 深度） |
| 免费兜底 | `anysearch` |

不指定 engine 用默认引擎；要对比就 `--engines a,b,c`（各自扣分）。

## 计费（心里有数，别乱烧）

- basic 档多为 1 积分/次（serpapi 4、brave 2）；advanced/deep 更高（exa deep 4、tavily advanced 2、baidu AI 搜索 3）。
- 失败不扣分；每次返回都带本次扣分与剩余积分，余额不足会明确报错——这时停下来告诉用户去续费，不要反复重试。
- Exa 超过 10 条结果每多 10 条加收积分，大批量抓取前先小样试。

## 出错怎么办

- 401：Key 无效或没配，让用户检查环境变量。
- 402：积分不足，提示兑换卡密续费（同一 Key 自动叠加）。
- 429：引擎繁忙或限流，换一家引擎重试一次，或稍后再试。
- 400：参数问题（如 query 为空），修正参数，不要原样重试。
