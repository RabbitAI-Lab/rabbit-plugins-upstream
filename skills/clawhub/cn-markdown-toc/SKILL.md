---
slug: cn-markdown-toc
name: Markdown目录生成器
version: "1.0.0"
author: 千策
---

# Markdown 目录生成器

为 Markdown 文档自动生成带锚点链接的目录（TOC）。纯标准库，本地运行。

## 功能

- 扫描 `#`~`######` 标题，按层级生成目录
- 自动生成 GitHub 风格锚点（英文/数字/连字符，忽略标点）
- 支持指定最大层级（如只取到 `###`）
- 可插入到文档顶部，或单独输出

## 依赖

无（Python 标准库）

## 使用方法

```bash
# 生成目录并预览
python3 scripts/md_toc.py 文章.md

# 插入到文件顶部（带占位符 <!-- TOC -->）
python3 scripts/md_toc.py 文章.md --insert

# 只取到三级标题
python3 scripts/md_toc.py 文章.md --max 3
```

## 适用场景

- 长文 / 文档 / 知识库自动生成导航
- 公众号 / 博客文章加目录
- 飞书文档 Markdown 导入前处理
