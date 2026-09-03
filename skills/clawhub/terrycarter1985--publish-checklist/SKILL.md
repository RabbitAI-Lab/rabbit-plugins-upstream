---
name: publish-checklist
description: ClawHub 技能发布前检查清单 - 确保技能元数据完整、内容安全、可被检索和正确安装
author: terrycarter1985
created: "2026-08-29"
version: "1.0.0"
license: MIT
tags:
  - clawhub
  - publish
  - checklist
  - quality
  - workflow
source: ""
dependencies: []
related:
  - digital-resource-ingest-demo
  - taskflow
lastReviewed: "2026-08-29"
---

# ClawHub 技能发布检查清单

发布技能到 ClawHub 资源中心前，逐项检查以下内容，确保技能可被发现、安装和安全使用。

## 1. 元数据检查

- [ ] `name` 使用小写连字符 slug 格式
- [ ] `description` 10-200 字，清晰说明用途和适用场景
- [ ] `author` 已填写
- [ ] `created` 使用 ISO 日期格式 (YYYY-MM-DD)
- [ ] `version` 符合 SemVer 规范
- [ ] `tags` 3-8 个，覆盖核心功能和适用场景
- [ ] `license` 已声明
- [ ] 可选字段（source, dependencies, related, lastReviewed）按需填写

## 2. 内容质量检查

- [ ] SKILL.md 正文包含"何时使用"说明
- [ ] 提供了至少一个可执行的基本步骤或命令示例
- [ ] 前置条件和依赖已说明
- [ ] 无占位符或 TODO 残留
- [ ] 文件结构清晰，references/ 目录存放辅助文档

## 3. 安全检查

- [ ] 无硬编码密钥、token 或敏感凭证
- [ ] 无 prompt injection 风险的外部内容引用
- [ ] 危险操作（删除、覆盖、外部发送）有明确提示
- [ ] 不包含与描述不符的隐藏功能

## 4. 可发现性检查

- [ ] name 和 description 中包含核心关键词
- [ ] tags 覆盖用户可能搜索的词汇
- [ ] 与相关技能建立 related 链接

## 5. 发布验证

- [ ] 本地 `clawhub inspect <skill>` 可正确读取元数据
- [ ] `clawhub search` 可搜索到已发布技能
- [ ] 安装后技能可正常调用

## 快速验证命令

```bash
# 检查技能目录结构
ls -la skills/<your-skill>/

# 本地预览元数据
clawhub inspect <your-skill>

# 发布
clawhub publish skills/<your-skill>

# 验证搜索
clawhub search "<核心关键词>"
```

## 引用

- [metadata-template.yaml](references/metadata-template.yaml) - 元数据填写模板
