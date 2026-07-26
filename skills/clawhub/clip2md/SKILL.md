---
name: clip2md
description: 剪藏网页链接到 clip2md，查询剩余额度
version: 1.0.0
metadata:
  openclaw:
    requires:
      bins:
        - node
    emoji: "✂️"
---

# clip2md - 网页剪藏

## 何时使用

- 用户想剪藏/保存一个网页链接为 Markdown
- 用户想查询剪藏剩余额度
- 用户提到 clip2md、剪藏、clip

## 首次使用

运行以下命令配置 token（token 从 clip2md 网页端个人资料页获取）：

```bash
node scripts/clip2md.js config <your_token>
```

## 命令

### 剪藏链接

```bash
node scripts/clip2md.js clip "https://example.com/article"
```

提交链接到 clip2md 进行解析，返回任务状态和剩余额度。

### 查询额度

```bash
node scripts/clip2md.js quota
```

显示每日剩余额度和永久剩余额度。

## 配置

Token 存储在 `~/.clip2md/config.json`。
API 地址固定为 `https://clip2.md/api/v1`。
