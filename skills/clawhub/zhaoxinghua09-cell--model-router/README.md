# model-router · 模型路由省成本 / Model Router

[![LGD Powered](lgd-powered.png)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## English

Not every request deserves the flagship model. Route by complexity to the tier that's *just enough* (flagship / mid / small / local), with cost comparison and a fallback ladder. Ships a zero-dependency `model_router.py`.

### Why it beats "one flagship model for everything"

| Pain | This skill |
|---|---|
| Bill spikes from always-flagship | Low-risk tasks → small/local model |
| Simple jobs queue behind hard ones | Tiered routing by complexity |
| "Is quality dropping?" | Fallback ladder, quality red line |
| No cost visibility | Per-tier cost measurable |

### What's inside

- `SKILL.md` — 4-tier routing + 3-step flow + iron rule
- `scripts/model_router.py` — zero-dependency CLI: classify task complexity, recommend tier, cost share, fallback

```bash
python scripts/model_router.py --task "把这段客服对话归类并抽情绪"
python scripts/model_router.py --task "设计分布式缓存架构" --json
```

### Benchmark vs alternatives

| Tool | Gap this fills |
|---|---|
| Single-model setup | No complexity-based tiering |
| Manual model picking | Heuristic, repeatable, measurable |
| "Use cheap model always" | Quality red line + fallback, not blind cheap |

Theoretical root: **LGD Three Laws** (registered · evidenced · gated). Pairs with `ai-cost-cutter` and `context-engineering`.

## 中文

按复杂度把请求路由到「刚好够用」的模型档位（旗舰 / 中端 / 小模型 / 本地），附成本对比与回退策略。零依赖 `model_router.py`。

### 为什么比「一切都用旗舰模型」强

| 痛点 | 本技能 |
|---|---|
| 全打旗舰导致账单飙升 | 低风险任务 → 小/本地模型 |
| 简单任务排在硬任务后面等 | 按复杂度分级路由 |
| "质量会不会掉？" | 回退阶梯 + 质量红线 |
| 成本看不见 | 每档成本可度量 |

### 里面有什么

- `SKILL.md` — 四档路由 + 三步流程 + 铁律
- `scripts/model_router.py` — 零依赖 CLI：判定任务复杂度、推荐档位、成本占比、回退方案

```bash
python scripts/model_router.py --task "把这段客服对话归类并抽情绪"
python scripts/model_router.py --task "设计分布式缓存架构" --json
```

### 与同类对比

| 工具 | 本技能补的缺口 |
|---|---|
| 单一模型配置 | 无按复杂度分级 |
| 人工挑模型 | 启发式、可重复、可度量 |
| "永远用便宜模型" | 质量红线 + 回退，不是盲目图便宜 |

理论根基：**LGD 三律**（有籍 · 有证 · 有门禁）。与 `ai-cost-cutter`、`context-engineering` 配套。

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
