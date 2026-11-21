# evidence-anchor

Resolve every `file:line` anchor in a report against the real tree — and refuse to count an unresolvable one as evidence.

把报告里的每个 `文件:行号` 锚点回真实文件里点一遍；点不开的，一律不算证据。

## Why this exists

A conclusion written as "there is a problem here" can't be checked by anyone. Written as `scripts/review.py:157`, anyone can open it and see the same line.

Reviews, audits and appeals all depend on that. Yet anchors rot silently: files get renamed, documents get rewritten, and a citation that pointed at line 157 now points at a comment — or at nothing at all. Nobody notices, because nobody re-opens them.

## What it does

| 验证 | 拒绝 |
|---|---|
| 文件是否存在 | 判断那一行内容对不对 |
| 行号是否在范围内 | 替作者补锚点 |
| 支持正反斜杠路径 | 把"无锚点"判成错误 |
| `file.py:12:5` 只取行不取列 | 检索外部来源 |

拒绝理由逐条写在 [`references/limits.md`](references/limits.md)：**假验证比不验证更糟**。

## Quick start

```bash
# 查一份报告（tools: check）
python scripts/anchor.py check reports/review.md --root path/to/tree

# 只列锚点与状态（tools: list）
python scripts/anchor.py list reports/review.md --root path/to/tree

# 接进流水线
python scripts/anchor.py check docs/report.md --root . || exit 1
```

退出码：0 = 全 OK 或无锚点；1 = 有失效锚点；2 = 参数/根目录错误。

## Verify it yourself

```bash
python tests/run_golden.py     # 9/9 PASS
python demo/run_demo.py        # 造最小树 + 三类锚点，看判定
```

## Design rules

1. 只判事实，不判内容——机器判"对不对"会制造"已验证"的假象。
2. 报告必须打出文件总行数，让读者分清"1097 行里第 157 行"和"12 行里第 157 行"。
3. 无锚点是取舍，解析失败是错误，两者不混报。
4. 根目录不猜：猜错会给出看似确定的错误结论。

## Related

- `lgd-skill-review` — 每条整改项都带 `文件:行号`，本工具验证这些位置真的存在
- `skill-improver` — 改完复测，锚点不变才算没改坏

## License

MIT © 2026 Zhao Xinghua
