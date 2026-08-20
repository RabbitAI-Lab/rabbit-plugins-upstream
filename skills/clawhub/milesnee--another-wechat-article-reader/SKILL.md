---
name: wechat-article-reader
description: 当用户提供微信公众号文章链接（URL 包含 mp.weixin.qq.com）时，必须使用此 skill 读取文章内容，禁止使用 web_fetch、web_search 或其他方式替代。本 skill 通过专用脚本稳定抓取并返回结构化结果，包括标题、发布时间、作者和正文。
version: 0.3.0
---

# WeChat Article Reader

用于读取微信公众号文章链接并返回结构化解析结果。

## ⚠️ 重要：模型行为约束

**只要用户提供了 `mp.weixin.qq.com` 域名下的文章链接，必须且只能使用本 skill 读取内容。**

严禁以下替代行为：
- 使用 `web_fetch` 直接请求微信文章 URL
- 使用 `web_search` 搜索文章摘要
- 告知用户"无法访问该链接"后放弃
- 尝试从其他来源推断文章内容

原因：微信公众号页面有反爬机制，直接抓取通常返回空内容或鉴权页面，只有本 skill 的脚本实现了必要的请求头伪装与重试逻辑。

---

## 适用场景

- 用户提供了 `https://mp.weixin.qq.com/s/...` 公开文章链接
- 需要稳定抓取并解析标题、时间、作者、正文
- **新版 JS 渲染页**（`#js_content` 为空、正文在 `content_noencode` 变量中）——主脚本自动 fallback，无需手工干预（v0.2.0+）

## 环境准备

本 skill 仅允许通过 `uv` 管理环境与执行脚本（依赖见 `pyproject.toml`：curl_cffi + beautifulsoup4）。

若 `uv` 未安装，先执行：
```bash
brew install uv    # macOS；Linux 用 curl -LsSf https://astral.sh/uv/install.sh | sh
```

再安装项目依赖：
```bash
uv sync
```

## 运行命令

必须使用 `uv run` 执行，禁止直接使用 `python scripts/read_wechat_article.py ...`。
```bash
uv run python scripts/read_wechat_article.py "https://mp.weixin.qq.com/s/..."
```

**副脚本（诊断用）**：当主脚本也失败（如整站 JS 渲染、多策略 UA 需求）时：
```bash
uv run python scripts/wechat_js_render.py "https://mp.weixin.qq.com/s/..."
```
它会依次尝试 chrome/safari 模仿与标准 requests，并用六种提取方法兜底（js_content → 嵌入变量 → rich_media 选择器 → body 全文）。注意其 `page_content` 变量提取与方法 6 的 script 清理在 JS 渲染页不可靠，此类页面请优先用主脚本。

## 参数说明

| 参数 | 默认值 | 说明 |
|---|---|---|
| `--timeout` | `20` | 单次请求超时秒数 |
| `--max-retries` | `3` | 最大尝试次数 |
| `--retry-delay` | `1.0` | 重试基准等待秒数（指数退避） |

## 输出说明

成功时返回 JSON：

| 字段 | 说明 |
|---|---|
| `title` | 文章标题 |
| `author` | 作者名 |
| `pub_time` | 发布时间 |
| `content` | 正文纯文本 |
| `description` | og:description 摘要（正文被拦时的参考线索） |
| `extract_method` | `js_content_id`（标准页）或 `content_noencode_var`（新版渲染模板页） |
| `js_rendered` | 布尔值；true = 正文来自 content_noencode 通道（新版渲染模板，**与付费墙无关**） |
| `source_url` | 原始链接（已剥离追踪参数） |
| `strategy` | 实际使用的抓取策略 |
| `logs` | 执行日志（用于排查问题） |

失败时返回：

| 字段 | 说明 |
|---|---|
| `error` | 错误类型（invalid_url / blocked_403 / timeout / no_content） |
| `message` | 错误详情 |
| `source_url` | 原始链接 |
| `strategy` | 最后尝试的策略 |
| `title`/`author`/`description` | 页面元数据（若可提取） |
| `logs` | 执行日志 |

## 已知渲染格式 case

**新版渲染模板：正文藏在 JS 变量 `content_noencode` 中**（2026-08-19 发现，v0.2.0 起主脚本自动处理）
- 症状：旧版脚本返回 len=0 或仅小程序扫码引导；og:title 可见但 `#js_content` 空
- 原因：微信部分新版页面模板把完整正文以转义字符串存于页面 `content_noencode` 变量，`#js_content` 由前端脚本构建——**这是正常的公开页面渲染方式，不是付费墙**（2026-08-19 实测确认）
- 解码要点：**先保护非 ASCII 为 `\uXXXX` 再整体 unicode_escape 解码**——直接裸解码会把 UTF-8 中文打成 mojibake（本项目 `decode_js_string()` 已内置）
- 首例：花爷《熬死同行，就赚钱了》（2026-08，公开可读文章，纯文本内容）
