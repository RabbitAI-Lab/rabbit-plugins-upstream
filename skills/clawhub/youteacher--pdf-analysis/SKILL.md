---
name: pdf-analysis
description: "使用场景: 用户需要分析带文字层的电子 PDF、提取摘要与关键观点、根据原文问答、对比多份文档，或导出带文件名和页码证据的结果时；不用于扫描件 OCR。"
metadata:
    {
        "packageVersion": "1.1.0",
        "openclaw":
            {
                "emoji": "📄",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "PDF_ANALYSIS_API_KEY",
                "requires": { "env": ["PDF_ANALYSIS_API_KEY"] },
            },
    }
---

# PDF 分析

## Skill 简介

PDF 分析 Skill 读取带文字层的电子 PDF，生成摘要、关键观点、结论、文档问答和多文档对比。每条原文证据都包含文件名、真实页码和原文片段，分析结果还可以导出为 Markdown 和 JSON。当前版本不支持 OCR，也不支持扫描件、图片 PDF 或加密 PDF。

长文档会由平台自动分段分析后综合，用户无需手工拆分；只有超过文件、页数或字符上限时才需要先拆分 PDF。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建并复制 API 密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.PDF_ANALYSIS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

确认 Python 环境可导入 `pymupdf`；缺少时在独立虚拟环境安装 `PyMuPDF`。

## Skill 使用

1. 先确认用户指定了 PDF 文件和目标：完整分析、快速摘要、关键观点、问答或多文档对比。
2. 使用随包脚本逐页提取文字。原始 PDF 保留在本机；仅将提取出的文件名、页码和文字提交给平台。
3. 如果脚本报告无文字层、加密、损坏、超过 50 页或超过字符限制，停止任务并向用户说明原因；不得自动改用 OCR。
4. 分析一份文档调用 `pdf.analyze`（PDF 内容分析），问答调用 `pdf.question`（PDF 内容问答），对比 2 至 3 份文档调用 `pdf.compare`（PDF 多文档对比）。
5. 展示结果时保留证据的文件名、页码和原文，不把模型结论写成未经证实的事实。
6. 用户明确需要文件时，使用成功任务 ID 调用 `pdf.export`（导出 PDF 分析结果），不得导出其他用户或其他 Skill 的任务。

## 参考资料

- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/API-KEY.md)
- [本地 PDF 文字提取](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/LOCAL-EXTRACTION.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/HTTP-REQUESTS.md)
- [操作与数据结构](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/OPERATIONS.md)
- [证据与安全规则](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/BEHAVIOR-RULES.md)
