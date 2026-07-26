---
slug: cn-line-sorter
name: 文本行排序工具
version: "1.0.0"
author: 千策
---

# 文本行排序工具

对文本文件的行进行排序、去重、反转、乱序。纯标准库，本地运行。

## 功能

- 按字典序 / 数字序排序
- 去重（保留首次出现）
- 反转行序
- 随机乱序
- 按行长度排序

## 依赖

无（Python 标准库）

## 使用方法

```bash
python3 scripts/line_sorter.py 列表.txt --sort
python3 scripts/line_sorter.py 列表.txt --unique -o 去重后.txt
python3 scripts/line_sorter.py 列表.txt --numeric --reverse
python3 scripts/line_sorter.py 列表.txt --shuffle
python3 scripts/line_sorter.py 列表.txt --by-length
```

## 适用场景

- 整理关键词 / 待办 / 名单
- 清洗重复数据
- 给列表随机排序做抽样
