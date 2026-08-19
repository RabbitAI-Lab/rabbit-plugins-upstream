---
name: memory-recall
description: |
  个人记忆与笔记检索助手。对本地 Markdown/纯文本笔记做全文+时间加权检索，支持按关键词、标签、日期范围召回，并给出相关片段。当用户需要"从我之前的笔记里找""搜索我的记忆""回忆一下之前讨论过"时调用。
agent_created: true
visibility: "public"
---

# 记忆与笔记检索助手

帮用户在本地积累的笔记/记忆（Markdown、txt、记忆文件）中快速找回所需信息。核心：**检索是可观测、可排序、可回溯来源的**。

## 适用场景
- 从过往对话/笔记中找回某个决定、某个链接、某段代码
- 跨多文件按主题聚合相关片段
- 按时间线回顾某件事的演进

## 检索模型
- **全文匹配**：对文件名 + 正文做大小写不敏感匹配。
- **时间加权**：越近的笔记权重越高（半衰期可配）。
- **标签/路径过滤**：支持 `--tag`、`--after`、`--before`、`--path`。
- **片段召回**：返回命中行上下文（前后 N 行），而非整文件。

## 标准工作流
使用 `scripts/memory_search.py`：
```bash
python scripts/memory_search.py "RAR 阅读" \
  --root "C:/Users/小江/.workbuddy/skills" \
  --tag archive --after 2026-07-01 --top 10 --ctx 2
```
- 支持多关键词（空格分隔，默认 AND；加 `--or` 转 OR）。
- 输出：文件路径、命中行号、相关片段、综合得分。

## 质量门禁
- [ ] 检索根目录是否过于宽泛（限定到相关域更快更准）
- [ ] 结果是否给出来源路径（便于回看原文）
- [ ] 大目录是否先用 `--path` 收窄

## 自进化学习系统
```bash
python scripts/learner.py record . --capability "记忆检索" [--fail --error <类型> --note <说明>]
python scripts/learner.py insight .
python scripts/learner.py reflect .
```
- 某关键词长期 0 命中 → 记录，reflect 提示"扩大检索根/换同义词"
- 用户常用某根目录 → `prefer` 记录默认 --root

## 安全边界
- 仅检索用户指定目录，不越权读取桌面/下载等个人敏感区，除非用户显式授权
- 不在返回中暴露凭据类内容
