# skill-improver

Turn a skill review's remediation list into executed changes — and refuse the ones that would only raise the score.

把一个技能包的评测整改清单，变成真的执行了的改动——并且拒绝那些只会让分数变高、不会让包变好的项。

## Why this exists

Every review tool tells you what is wrong. None of them performs the fix.

现有的评测工具都只告诉你哪里不对，没有谁真的去改。这一环一直是人在做：读完整改清单，手工补 LICENSE、补 tags、补触发词、补互链，再复测一遍。

skill-improver 就是这一环，并且**明确划出自动化停手的地方**。

## What it does

| 自动补 | 拒绝（必须人工） |
|---|---|
| LICENSE 文件 | 测试用例 |
| `ai-index.json` | 测试执行器 |
| tags（≥3） | demo |
| Triggers 段 | 安全边界声明 |
| 同系列互链 | 声明了但未实现的参数（可 `--fix-doc-drift` 移除示例行） |

拒绝不是遗漏，是设计：**自动生成的空 runner 能让 reproducible 拿分，但包依然没验过。** 理由逐条写在 [`references/limits.md`](references/limits.md)。

## Quick start

```bash
# 只诊断，不写任何文件
python scripts/improve.py scan path/to/skill

# 执行改造并复测
python scripts/improve.py apply path/to/skill

# 连带处理文档漂移（会改动既有内容，需显式开启）
python scripts/improve.py apply path/to/skill --fix-doc-drift

# 指定评测器与同系列兄弟
python scripts/improve.py apply path/to/skill --reviewer path/to/review.py --siblings a,b
```

无子命令时默认走 `scan`，所以 `python scripts/improve.py path/to/skill` 仍然可用。

## Verify it yourself

```bash
python tests/run_golden.py     # 9/9 PASS
python demo/run_demo.py        # 造差包 → 改造 → 复测
```

本包用同系列评测器 `lgd-skill-review` 自测：

```
结构制 100/100 PASS
语义制 120/120 A
自检   9/9 PASS
```

## Design rules

1. 每个写操作前重读文件——串联修复器共享旧快照会互相覆盖（实测 54 → 50）。
2. 拒绝项逐条列出并给原因，不假装全修好了。
3. 自动化停手的位置写在文档里，不停在实现里。
4. 判定标准只有一句：**改完之后，这个包真的变好了，还是只是分数变高了？**

## Not for

- 从零创建技能包
- 只想要分数、不想要改动
- 伪造测试或 demo 通过评审

## License

MIT © 2026 Zhao Xinghua
