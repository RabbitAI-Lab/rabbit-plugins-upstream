---
name: yijing-divination
description: "东方智慧占卦：铜钱起卦、时间起卦、数字起卦、随机起卦，DeepSeek AI解卦。一行代码定义给Agent注入东方智慧。"
homepage: "https://skill.aiepco.com/tools/yijing/"
metadata:
  openclaw:
    emoji: "☯️"
    category: "entertainment"
    tags: ["yijing", "divination", "iching", "占卦", "易经", "八卦", "东方智慧"]
    api_base: "https://skill.aiepco.com"
    pricing:
      cast: 10
      read: 20
    signup_bonus: 20
---

# 天玑八卦盘 ☯️

千年东方智慧 × 现代 AI。为用户提供四种起卦方式，DeepSeek AI 深度解卦。

## 触发词

用户说以下任一词时激活本技能：`占卦` `起卦` `算卦` `八卦` `易经` `卜卦` `求签` `占卜` `铜钱起卦` `yijing` `divination` `iching`

## 产品形态

天玑八卦盘是**产品型技能**——用户需要交互式 UI 完成起卦操作，而非简单的一问一答。

### UI 呈现方式

1. **首选：Canvas 嵌入**（支持 HTML 渲染的通道）
   - 将 `tools/yijing.html` 部署到 OpenClaw Canvas 目录
   - 路径：`~/.openclaw/canvas/tools/yijing/index.html`
   - 呈现：`canvas present /__openclaw__/canvas/tools/yijing/index.html`

2. **备选：直接链接**（纯文本通道）
   - 链接到托管页面：`https://skill.aiepco.com/tools/yijing/`
   - 回复格式：`🔮 [打开天玑八卦盘](https://skill.aiepco.com/tools/yijing/)`

### 自动注册

首次使用自动创建账号（调用 `POST /api/tools/auto-register`），无需用户手动注册。
返回用户名、密码、API Key，20 Token 体验额度自动到账。

## API 端点

所有端点使用 Bearer Token 认证：`Authorization: Bearer sk-xxx`

| 端点 | 方法 | Token | 说明 |
|:---|:---|:---|:---|
| `/api/yijing/cast` | POST | 10T | 起卦（coins/time/number/random） |
| `/api/yijing/read` | POST | 20T | AI 深度解卦（需传 question） |
| `/api/tools/auto-register` | POST | 免费 | 一键注册账号 + 获取 API Key |
| `/api/tools/profile` | GET/PUT | 免费 | 查/改用户资料 |

详见 `references/api.md`

## 起卦方式

| 方法 | 参数 | 说明 |
|:---|:---|:---|
| `coins` | 无 | 铜钱起卦（六爻法），模拟三枚铜钱抛六次 |
| `time` | 无 | 时间起卦（梅花易数），取年月日时 |
| `number` | `{ n1, n2, n3 }` | 数字起卦，用户自选三个数字（1-999） |
| `random` | 无 | 完全随机起卦 |

## 返回数据

起卦返回：卦名、卦号、上下卦 Unicode、卦辞、六爻（含动爻标记）、变卦信息。

## 用户交互流程

```
用户说"帮我占一卦"
       ↓
Agent 呈现 Canvas UI（或发送链接）
       ↓
用户在 UI 中选择起卦方式 + 输入问题
       ↓
UI 自动调用 API 起卦 + 解卦
       ↓
展示卦象可视化 + AI 解读
```

## 安装后使用

安装本 Skill 后，Agent 自动获得以下能力：

1. **识别占卦意图** — 从触发词中识别用户想占卦
2. **呈现交互界面** — 打开 Canvas 或发送链接
3. **无需手动配置** — 首次使用自动注册获取 API Key
