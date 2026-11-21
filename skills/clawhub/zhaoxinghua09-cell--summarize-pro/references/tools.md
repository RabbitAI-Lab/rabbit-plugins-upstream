# 三条命令上手（复制即用）

## 三条命令上手（复制即用）

```bash
# 1) 从原文抽事实并生成纪要骨架（产出 X.minutes.md + X.facts.json）
python scripts/summarize_pro.py extract --file transcript.md --format minutes

# 2) 核对你的成稿是否每句都有出处（列出不可溯源句）
python scripts/summarize_pro.py citecheck --file out.md --source transcript.md

# 3) 用 facts.json 确定性渲染，导出可打印 HTML
python scripts/summarize_pro.py render --facts transcript.facts.json --view receipt --format html
```

```bash
python scripts/summarize_pro.py extract  --file demo/sample_transcript.md --format minutes --out out
python scripts/summarize_pro.py selfcheck --file out/sample_transcript.minutes.md --format minutes
python scripts/summarize_pro.py citecheck --file demo/expected_minutes.md --source demo/sample_transcript.md
```

提示词场景**不需要**装 Python：规则包本身可直接用；工具是给「要批量跑、要留证据」的场景用的。
`--json` 输出固定四字段 `ok / error_id / data`；错误码 S001 文件不存在、S002 编码不可读、S003 空内容、S004 未知格式、S005 输出目录不可写、S006 原文过短（<50 字不套格式族）。

一键自证：`python demo/run_demo.py`（抽取 → 自检 → 溯源，并把数字故意改错，验证能抓出来）；`python tests/run_golden.py`（10 条黄金集，当前 10/10 PASS）。

## 三条命令上手

scan / apply 两个子命令与最小可用示例见 `references/tools.md`。

## 意图路由

按意图而不是关键词路由，完整路由表与关键词见 `references/routing.md`。

## 第一步：选格式族（三问答）
