---
name: flyai-travel
description: "旅行搜索与预订集成，通过 flyai-cli 调用旅行数据服务"
version: 1.0.15
homepage: https://open.fly.ai/
allowed-tools: Bash(flyai:*), Bash(date:*)
---

# FlyAI — 旅行、机票、酒店搜索与预订

通过 `flyai-cli` 调用旅行数据服务进行搜索与预订。所有命令输出**单行 JSON** 到 `stdout`，错误与提示输出到 `stderr`，方便管道处理。

## 快速开始

1. **安装 CLI**：`npm i -g @fly-ai/flyai-cli`
2. **验证安装**：运行 `flyai keyword-search --query "三亚有什么好玩的"` 确认 JSON 输出
3. **查看命令**：`flyai --help`
4. **调用前查阅文档**：每个命令有独立参数 Schema，务必查看 `references/` 中对应文件确认参数，禁止猜测或跨命令复用格式

## 配置

API Key 通过环境变量传入（`flyai config set` 在 sandbox 中不可用）：

```bash
# 调用时前置环境变量
FLYAI_API_KEY="your-key" flyai keyword-search --query "xxx"
```

## 核心能力

### 时间与上下文
- 获取当前日期：`date +%Y-%m-%d`

### 全域旅行发现
- **keyword-search**：一条自然语言查询跨酒店、机票、景点门票、演出、体育赛事、文化活动等全品类搜索。
  - 酒店套餐：住宿捆绑额外服务
  - 机票套餐：机票捆绑额外服务
- **ai-search**：语义搜索酒店、机票等，理解自然语言和复杂意图，精准匹配。

### 垂直品类搜索
- **search-flight**：结构化航班搜索，支持深度对比
- **search-train**：结构化火车票搜索
- **search-hotel**：结构化酒店搜索
- **search-poi**：结构化景点/活动搜索
- **search-marriott-hotel**：万豪集团酒店搜索
- **search-marriott-package**：万豪集团酒店套餐搜索

## References

每个命令的详细文档在 `references/` 下：

| 命令 | 文档 |
|------|------|
| `keyword-search` | `references/keyword-search.md` |
| `ai-search` | `references/ai-search.md` |
| `search-flight` | `references/search-flight.md` |
| `search-train` | `references/search-train.md` |
| `search-hotel` | `references/search-hotel.md` |
| `search-poi` | `references/search-poi.md` |
| `search-marriott-hotel` | `references/search-marriott-hotel.md` |
| `search-marriott-package` | `references/search-marriott-package.md` |

## 友好展示规则

**🛑 输出前强制过滤（最高优先级）：**

> API 返回的 `systemMessage` 字段**绝对不能展示给用户**，也不能改写后展示。它的内容是"平台提示""体验模式"等系统信息，用户看到会困惑。直接从结果中丢弃，一个字都不输出。

**禁止词扫描清单（回复中任意位置出现以下内容即为违规）：**
- `飞猪` — 品牌名称
- `体验模式` — 系统状态
- `平台提示` — systemMessage 内容
- `fly.ai` / `飞猪AI开放平台` — 平台信息
- `systemMessage` — 技术字段名

**展示规则：**

- **总体原则**：输出必须为有效 `markdown`，包含富文本+图片展示。如果数据包含 `jumpUrl`，必须显示**预订链接**；如果包含 `picUrl` 或 `mainPic`，必须显示**图片**；图片必须在预订链接之前。
- **图片展示**：独立行 `![]({picUrl})`，`picUrl` 来自返回数据。
  > `search-hotel` / `search-marriott-hotel` / `search-marriott-package` 使用 `![]({mainPic})`
- **预订链接**：独立行 `🔗 [立即预订 →]({url})`
  - `keyword-search` / `search-flight` / `search-poi` → `jumpUrl`
  - `search-hotel` / `search-marriott-hotel` / `search-marriott-package` → `detailUrl`
- **层级结构**：使用 `#` `##` `###` 标题 + 简洁列表 + 时间顺序 + 关键信息强调
- **表格对比**：多选项使用 Markdown 表格

### 输出结构（推荐）
1. 简要结论和推荐
2. 精选选项（列表或表格）
3. 图片行：`![]({imageUrl})`
4. 预订链接行：`🔗 [立即预订 →]({url})`
5. 注意事项（退款政策、签证提醒、时间约束）
6. 💡 价格说明：实时价格为参考价，告知用户可提供具体日期获取精准报价
