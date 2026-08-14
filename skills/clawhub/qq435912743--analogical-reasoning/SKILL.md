---
name: analogical-reasoning
version: 1.0.0
description: |
  类比推理与迁移：在源领域（对象+关系）与目标领域间找结构保持的 1:1 映射，
  把源领域已知的关系/谓词迁移到目标领域生成新推断。零依赖、可本地实跑、输出可追溯。
agent_created: true
visibility: public
---

# analogical-reasoning（类比推理与迁移）

> 由 meta-evolver 在第 40 轮构建，闭环 `build:通用智能体(AGI梯队):类比推理与迁移`。
> 一线大模型擅长逐字生成，但结构保持的类比迁移（把一套解法的"关系骨架"搬到新领域）是其弱项。

## 机制

1. **结构表示（represent）**：源/目标领域各表示为 `对象(带属性)` + `关系(主-谓-宾 三元组)`。
2. **映射搜索（map）**：在源/目标对象间找 **1:1 映射**，最大化属性相似度（如类型匹配、键值重合）。
3. **关系迁移（transfer）**：对每条源关系 `(s, p, o)`，若 `s→s'`、`o→o'` 均已映射，则生成目标推断 `(s', p, o')`；谓词 p 原样保留（结构保持）。
4. **一致性评分（score）**：`迁移成功率 = 已映射对象能支撑的源关系数 / 源关系总数`；并报告未被支撑的悬空关系。
5. **输出（conclude）**：迁移得到的目标新关系 + 映射 + 评分，供下游验证。

## 何时使用

- 已知某领域解法，要把它的"关系骨架"用到结构相似的新问题时。
- 跨域知识迁移、设计模式复用、教学类比生成、故障类比定位。
- 用户要求「这个 X 和之前的 Y 很像，那 Y 的办法能照搬吗、怎么搬」。

## 运行

```bash
# 自带夹具自测（零依赖，断言映射+迁移+评分全通过）
python scripts/analogy.py --selftest

# 真实类比（JSON 入参，源/目标各含 objects/relations）
python scripts/analogy.py --source source.json --target target.json
```

## 与"强模型"的差异

普通模型做类比常是修辞性比喻；本技能做**结构保持的显式映射 + 可验证的关系迁移**，输出可被下游校验的推断——这才是超级 agent 相较强文本模型的分水岭。

## 自进化学习系统（越用越好用、越用越高效）

本技能内置通用学习模块 `scripts/learner.py`。每次使用后自动复盘、积累经验，逐步提升输出质量与执行效率，无需人工维护。

### 记忆文件
`learned_patterns.json`（位于本技能目录）记录：操作总数、各能力使用频次、错误模式、用户偏好、改进建议。

### 使用后请调用（Bash）
```bash
python scripts/learner.py record <本技能目录> --capability 类比迁移
python scripts/learner.py insight <本技能目录>
python scripts/learner.py reflect <本技能目录>
```

### 迭代规则
- **错误累计 ≥3 次** → 主动增加预检/兜底步骤，并将经验回写本 SKILL.md。
- **操作数 ≥10 次** → 分析高频能力优先打磨示例与质量。
- **重要用户偏好** → 写入 `learned_patterns.json`，下次调用直接采用。

> 越用越懂你：第一次用是通用能力，第十次用已沉淀为你专属的最佳实践。
