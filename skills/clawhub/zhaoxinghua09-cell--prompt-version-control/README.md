# prompt-version-control · 提示版本管理 / Prompt Version Control

[![LGD Powered](lgd-powered.png)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## English

Prompts are *versionable assets*. Every edit keeps version + diff + bound eval score, so you can diff, roll back, and pick the best — no more copy-paste management. Ships a zero-dependency `prompt_vc.py`.

### Why it beats "edit in place"

| Pain | This skill |
|---|---|
| Broke prompt, can't revert | Versioned, one-key rollback |
| "Which change helped?" | Per-version diff recorded |
| Score not tied to prompt | Version ↔ eval score bound |
| Two people overwrite each other | Sequential commit, no clobber |

### What's inside

- `SKILL.md` — version+diff+score 3-piece + 3-step flow + iron rule
- `scripts/prompt_vc.py` — zero-dependency CLI: diff two prompt files, append a version record (JSON)

```bash
python scripts/prompt_vc.py --old v1.txt --new v2.txt --score 0.82
python scripts/prompt_vc.py --old v1.txt --new v2.txt --score 0.82 --json
```

### Benchmark vs alternatives

| Tool | Gap this fills |
|---|---|
| Copy-paste backups | Structured version+score, not loose files |
| Notebook experiments | Diff + rollback, repeatable |
| "Just remember v2 was better" | Bound eval score, not memory |

Theoretical root: **LGD Three Laws** (registered · evidenced · gated). Pairs with `context-engineering` and `skill-quality-gate`.

## 中文

把提示当可版本化资产：每版留版本+差异+效果分，可 diff/回滚/选优。零依赖 `prompt_vc.py`。

### 为什么比「就地改」强

| 痛点 | 本技能 |
|---|---|
| 提示改坏了回不去 | 有版本、一键回滚 |
| "哪次改动真有用？" | 每版差异留痕 |
| 分数没绑提示 | 版本 ↔ 评分绑定 |
| 两人互相覆盖 | 顺序提交、不踩塌 |

### 里面有什么

- `SKILL.md` — 版本+差异+评分三件套 + 三步流程 + 铁律
- `scripts/prompt_vc.py` — 零依赖 CLI：diff 两个提示文件、追加版本记录（JSON）

```bash
python scripts/prompt_vc.py --old v1.txt --new v2.txt --score 0.82
python scripts/prompt_vc.py --old v1.txt --new v2.txt --score 0.82 --json
```

### 与同类对比

| 工具 | 本技能补的缺口 |
|---|---|
| 复制粘贴备份 | 结构化版本+评分，不是散文件 |
| Notebook 实验 | diff + 回滚、可重复 |
| "记住 v2 更好" | 绑定评分，不靠记性 |

理论根基：**LGD 三律**（有籍 · 有证 · 有门禁）。与 `context-engineering`、`skill-quality-gate` 配套。

---

© 2026 SynomosAI. All rights reserved.

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

- **代码**（本包 `.py` 文件）：**MIT**
- **本 `README.md` / `SKILL.md` 及其中的理论文本、方法论与一切理论表述**：**不在 MIT 覆盖范围内**，保留所有权利（All rights reserved）

```
© 2026 SynomosAI. All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" — 未申请实体注册、未申请商标注册
                        (not a registered legal entity; no trademark registered)
生产参考部署 (production reference, self-reported) : 无（未声明外部生产参考部署）
                    ← 非认证、非背书、非监管认可（not a certification or endorsement）
代码许可 (code license) : 本包未附 LICENSE 文件（许可待定）
                    本文本与理论表述不在任何代码许可覆盖范围内
引用格式 (cite as)      : 本资产无 DOI
```
（上列为《LGD 对外表述规范》§3.2 统一块，**整体复制、未删改**；发布/重提前须照最新版本复核。）
