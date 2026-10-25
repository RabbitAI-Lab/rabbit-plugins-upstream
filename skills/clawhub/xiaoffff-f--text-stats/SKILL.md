---
name: text-stats
description: 统计文本的字数、字符数、段落数、句子数和预计阅读时长。当用户问"这段文字多少字"、"统计字数"、"阅读要多久"、"word count"、"text statistics"，或提供文本/文件要求做基础文本统计时使用。
---

# Text Stats

对给定文本或文本文件做基础统计并给出简洁报告。

## 使用方法

运行 `scripts/text_stats.py`：

```bash
python scripts/text_stats.py <文件路径>
# 或从标准输入读取
echo "文本内容" | python scripts/text_stats.py
```

脚本输出 JSON，字段含义：

- `chars`：总字符数（含空白）
- `chars_no_space`：去除空白后的字符数（中文场景常用的"字数"）
- `cjk_chars`：中日韩字符数
- `latin_words`：英文单词数
- `sentences`：句子数（按 。！？.!? 切分）
- `paragraphs`：段落数
- `reading_minutes`：预计阅读时长（按中文 400 字/分钟、英文 200 词/分钟估算）

## 报告方式

用一张小表格呈现结果，并在末尾给一句简短解读（例如"约相当于一篇公众号短文"）。不要逐字段复述 JSON 字段名，用自然语言描述。

若用户没提供文本，先询问文本内容或文件路径。
