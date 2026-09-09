# 爱搜 GEO API 参考

本参考整理自用户提供的《爱搜GEOAPI文档》压缩包（2026-08-25）。价格页可能变化；提交前优先核对 `https://geo.aidso.com/question` 的实时列表。

## 目录

- 密钥与端点
- 平台、终端、模式与积分
- 原子任务和计费
- 提交对话
- 查询结果
- 结果字段
- 卡片标记
- 状态码

## 密钥与端点

- API 密钥管理：`https://geo.aidso.com/setting?type=apiKeyManage`
- 提交：`POST https://openapi.aidso.com/geo_api/task_commit`
- 查询：`GET https://openapi.aidso.com/geo_api/get_result?reqId=<REQ_ID>`
- 认证头：`aidso-token`

用户选择在对话中绑定密钥。只在当前会话使用；不得把密钥写入文件、manifest、日志、报告、URL 或命令参数。脚本只允许从标准输入或 `AIDSO_TOKEN` 安全注入读取。

## 平台、终端、模式与积分

单位：积分/次。

| 编码 | 平台 | 终端 | 快速 | 思考/深度 | 模式标签 |
|---|---|---|---:|---:|---|
| `DB` | 豆包 | 网页 | 0.8 | 0.8 | 思考 |
| `DOUBA` | 豆包 | 手机 | 0.8 | 0.8 | 思考 |
| `DP` | DeepSeek | 网页 | 0.8 | 0.8 | 深度 |
| `DPA` | DeepSeek | 手机 | 1 | 1 | 深度 |
| `TXYB` | 元宝（腾讯元宝） | 网页 | 0.8 | 0.8 | 深度 |
| `TXYBA` | 元宝（腾讯元宝） | 手机 | 1 | 1 | 深度 |
| `TYQW` | 千问 | 网页 | 0.8 | 0.8 | 深度 |
| `TYQWA` | 千问 | 手机 | 1 | 1 | 深度 |
| `BDAI` | 百度 AI | 网页 | 0.8 | — | 仅快速 |
| `WXYY` | 文心 | 网页 | 0.8 | 0.8 | 深度 |
| `KIMI` | Kimi | 网页 | 0.8 | 0.8 | 思考 |
| `DYAI` | AI 抖音 | 网页 | 0.8 | 0.8 | 深度 |
| `XHSA` | 红书问一问 | 手机 | 3 | — | 仅快速 |

不推断表中没有的终端或模式。运行 `plan_diagnosis.py --list-platforms` 输出机器可读目录。

模式映射：

- 快速：`thinking_enabled = 0`
- 思考/深度：`thinking_enabled = 1`

## 原子任务和计费

一次原子对话由以下三项唯一确定：

```text
一个 prompt + 一个平台终端编码 name + 一个 thinking_enabled
```

品牌、产品和报告需求不是 API 参数，不得自动拼入 `prompt`。

用户口径：

```text
问题数 × 平台终端数 × 思考模式数 × 对话轮数
```

精确展开口径：

```text
原子对话数 = 问题数 × 已选平台终端模式组合数 × 对话轮数
总积分 = 问题数 × 对话轮数 × Σ(每个已选组合的单价)
```

当不同终端可选模式数不一致时，只使用精确展开口径。

## 提交对话

请求：

```http
POST /geo_api/task_commit
aidso-token: <当前会话密钥>
Content-Type: application/json

{
  "prompt": "面霜推荐",
  "name": "DB",
  "thinking_enabled": 0
}
```

成功响应中的 `data` 是原子 `reqId`：

```json
{
  "code": 200,
  "msg": "成功",
  "data": "8abcb01d-fff6-4ba0-9d11-d60d693d582d"
}
```

API 没有公开批量汇总 ID。Skill 生成本地诊断 ID 和任务名称，把全部 `reqId` 归组到 `.aidso-geo/tasks/` manifest。

提交请求发出但未得到明确 `reqId` 时，结果可能已受理并扣费；记录 `UNKNOWN`，不自动重试。

## 查询结果

请求：

```http
GET /geo_api/get_result?reqId=<REQ_ID>
aidso-token: <当前会话密钥>
```

处理中：

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "prompt": "面霜推荐",
    "status": "ING",
    "result": [],
    "fetch_time": 1720000000
  }
}
```

完成状态为 `SUCCESS`。每次用户查询只执行一次查询批次，不循环、不等待、不自动重试。单轮对话通常约需 10～30 分钟。

## 结果字段

完成后的 `data.result` 是对象数组，常见字段：

- `search_word`：JSON 字符串形式的扩展搜索词数组。
- `quote`：JSON 字符串形式的引用数组。
- `think`：思考字段；不进入报告，不分析隐藏思考。
- `context`：AI 回答正文，是品牌/产品提及、排名与情感分析的唯一正文来源。
- `suggestions`：建议字段。
- `rich_media_block`：富媒体字段。

`quote` 常见字段包括 `url`、`title`、`snippet`、`index`、`published_at`、`site_name`、`site_icon`、`task_id`、`platform`、`quto_id`。引用摘要 `snippet` 不计入正文提及。

## 卡片标记

卡片可能内嵌在 `context` 字符串中。规范化时先提取卡片，再从 `context_text` 删除整个标记块。

| 平台/类型 | 开始标记 | 结束标记 |
|---|---|---|
| 豆包商品 | `render_ecom_card_widget_product_start:` | `render_ecom_card_widget_product_end:` |
| 豆包本地生活 | `render_ecom_card_widget_poi_start:` | `render_ecom_card_widget_poi_end:` |
| 千问淘宝 | `render_ecom_card_widget_taobao_start:` | `render_ecom_card_widget_taobao_end:` |
| 千问大麦 | `render_ecom_card_widget_damai_start:` | `render_ecom_card_widget_damai_end:` |
| 千问高德 | `render_ecom_card_widget_gaode_start:` | `render_ecom_card_widget_gaode_end:` |
| 元宝小程序 | `render_ecom_card_widget_miniprogram_start:` | `render_ecom_card_widget_miniprogram_end:` |
| 元宝京东 | `render_ecom_card_widget_jd_start:` | `render_ecom_card_widget_jd_end:` |

商品卡常见字段：

- 豆包：`text`、`seller_name`、`image_url`、`pid`、`jump_url`
- 千问淘宝：`title`、`shop_name`、`pic_path`、`price`、`jump_url`、`auctionURL`、`item_id`
- 元宝京东：`sku`、`sku_name`、`query`、`image_url`、`price`、`shop_name`、`shop_id`、`pc_url`

本地生活、演出、地图和小程序卡片不混入商品卡指标，除非用户明确要求且诊断场景适用。

## 状态码

| code | 含义 | 处理 |
|---:|---|---|
| 200 | 请求成功 | 记录 `reqId` 或结果 |
| 400 | `reqId` 未提交 | 检查 ID，不重提付费任务 |
| 401 | 未授权 | 要求当前会话重新绑定密钥 |
| 405 | 参数错误 | 修正并重新规划、报价、确认 |
| 406 | 积分不足 | 停止剩余提交 |
| 429 | 请求频繁 | 停止，不自动重试 |
| 500 | 服务异常 | 保留不明确状态，不盲目重提 |
