# 各通道凭据与格式速查

notify-hub 统一三分离：Message（发什么）× Channel（通过什么发）× Target（发给谁）。
下表是各通道 adapter 的关键差异，供二次开发与排错参考。

## 凭据与端点

| 通道 | name | webhook/端点 | 凭据字段 | 签名 |
|------|------|-------------|---------|------|
| 飞书 | `feishu` | `https://open.feishu.cn/open-apis/bot/v2/hook/{id}` | `url`, `secret`(可选) | HMAC-SHA256，key=`timestamp\nsecret`，加密空字节，base64，加 `timestamp`+`sign` 字段 |
| 企业微信 | `wecom` | `https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}` | `url` | 无（key 在 URL） |
| 钉钉 | `dingtalk` | `https://oapi.dingtalk.com/robot/send?access_token={token}` | `url`, `secret`(可选) | 标准 HMAC-SHA256，key=secret，message=`timestamp\nsecret`，base64+urlencode 拼 `&timestamp=&sign=` |
| Slack | `slack` | `https://hooks.slack.com/services/{T}/{B}/{X}` | `url` | 无（URL 即鉴权） |
| Telegram | `telegram` | `https://api.telegram.org/bot{token}/{method}` | `token`, `chat_id` | 无（token 在 URL） |
| 邮件 | `email` | SMTP | `smtp_host`, `port`, `user`, `password`, `to`, `sender` | SMTP 登录 |

> 注意飞书与钉钉签名极易混淆：飞书把 `timestamp\nsecret` 当 **key**（加密空字节）；钉钉把 `secret` 当 key、`timestamp\nsecret` 当 **message**。代码已封装，勿手改。

## 卡片降级渲染矩阵

统一卡片 DSL 的 section 类型在各通道的渲染方式：

| section | 飞书 | 企业微信 | 钉钉 | Slack | Telegram | 邮件 |
|---------|------|---------|------|-------|----------|------|
| `markdown` | card markdown | markdown | markdown | mrkdwn block | HTML | HTML |
| `table` | markdown 表格 | **文本对齐降级** | **文本对齐降级** | code block 文本 | `<pre>` 文本 | `<table>` |
| `button` | card button | 文本链接降级 | 文本链接降级 | button block | inline keyboard | `<a>` 按钮 |
| `note` | 斜体 markdown | 灰色字体 | 引用降级 | context block | 斜体 | 灰色小字 |

各通道 markdown/表格能力差异：
- **飞书**：卡片 markdown 支持表格（最完整）。
- **企业微信**：markdown 不支持表格，仅 3 种 font color（`info`绿/`comment`灰/`warning`橙红）。
- **钉钉**：markdown 不支持表格。
- **Slack**：mrkdwn 不支持表格，用 code block 呈现对齐文本。
- **Telegram**：HTML parse_mode 支持 `<b>/<i>/<a>/<pre>/<code>`，不支持表格。

## 限流

| 通道 | 上限 |
|------|------|
| 飞书 | 100 次/分钟 |
| 企业微信 | 20 次/分钟 |
| 钉钉 | 20 次/分钟 |
| Slack | 60 次/分钟（保守） |
| Telegram | 30 次/分钟（保守） |
| 邮件 | 30 次/分钟（保守） |

基类 `Channel._throttle()` 已按 `rate_per_min` 内置节流，广播时自动间隔。

## 常见错误码

| 通道 | code | 含义 |
|------|------|------|
| 飞书 | 19021 | 签名失败/时间戳超时 |
| 飞书 | 19022 | IP 白名单拦截 |
| 飞书 | 19024 | 关键词校验失败 |
| 企业微信 | 45009 | 限流 |
| 企业微信 | 93000 | 参数格式错误 |
| 钉钉 | 310000 | 关键词不匹配 |
| 钉钉 | 300001 | token 无效 |

## 二次开发：新增通道

1. 在 `channels/` 新建 `mychannel.py`。
2. 继承 `base.Channel`，设置 `name`/`label`/`rate_per_min`。
3. 覆盖 `render_text` / `render_card`（/ `render_file`），返回该通道原生 payload。
4. 覆盖 `post(target, payload)`，用 `self.resolve_target(target)` 取凭据，调用 `self.http_json()` 或自定义发送。
5. 加 `@register` 装饰器；在 `core/registry.py` 的 `load_all()` 里加模块名。

核心 `message.py` 提供 `table_to_markdown()` 与 `table_to_text()` 两个降级辅助，直接复用。
