---
slug: cn-file-batch-rename
name: 批量文件重命名
version: "1.0.0"
author: 千策
---

# 批量文件重命名

按规则批量重命名目录下的文件：加前缀/后缀、查找替换、序号编号。纯标准库，先预览后执行。

## 功能

- 前缀 / 后缀追加
- 查找替换（支持正则）
- 按修改时间 / 名称顺序加序号（001_, 002_...）
- `--dry-run` 预览，确认后再执行

## 依赖

无（Python 标准库）

## 使用方法

```bash
# 预览（不实际改名）
python3 scripts/batch_rename.py ./照片 --prefix "2026_" --dry-run

# 查找替换
python3 scripts/batch_rename.py ./文档 --replace "旧名:新名"

# 加序号前缀
python3 scripts/batch_rename.py ./截图 --sequence
```

## 适用场景

- 整理导出的一批截图 / 照片
- 项目文件统一命名规范
- 批量去空格 / 改扩展名
