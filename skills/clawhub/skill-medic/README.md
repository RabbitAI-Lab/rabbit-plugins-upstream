# SkillMedic — AI Skill 健康检查与冲突检测专家

> 装了一堆 Skill 不知道哪个好用？哪些功能重复？哪些会抢对话？SkillMedic 帮你扫一遍，告诉你该留谁、该合谁、该删谁。

[![version](https://img.shields.io/badge/version-0.5.0-blue)](./1-manifest/skill-manifest.yaml)
[![level](https://img.shields.io/badge/level-L3-success)](./CHANGELOG.md)
[![python](https://img.shields.io/badge/python-3.10%2B-green)](#依赖)
[![license](https://img.shields.io/badge/license-MIT-green)](#许可证)

---

## 这是什么

在 TRAE 等 AI IDE 里装了十几个甚至几十个 Skill 之后，常见这几类问题：

- **重复功能**：装了 3 个"写文档"的 Skill，不知道哪个才是最好的
- **意图冲突**：两个 Skill 都声称"我来处理代码审查"，AI 不知道该听谁的
- **上下文膨胀**：装得越多，AI 每次加载的上下文越大，速度越慢
- **不知道成熟度**：社区搜来的 Skill，看起来很牛但会不会是半成品？

**SkillMedic 就是来做这件事的——像老中医体检一样，把你所有的 Skill 从头到尾扫一遍，然后告诉你：谁健康、谁亚健康、谁该治、谁该删。**

---

## 核心能力

| 能力 | 说明 |
|------|------|
| **全量清单** | 扫描 workspace + 全局 Skill，产出统一清单（名称/版本/功能域） |
| **三维分类** | 按功能域 / 交互模型 / 生命周期状态自动分类 |
| **五类冲突检测** | C1 同质重复 / C2 意图抢占 / C3 上下文膨胀 / C4 依赖 / C5 资源竞争 |
| **八维成熟度评分** | 0-100 分，L0~L3 四档定级（放心用 / 基本能用 / 不太成熟 / 不建议用） |
| **综合处方** | 保留 / 合并 / 整改 / 移除 四档建议，附带理由 |
| **分档报告** | S1 精细(≤20) / S2 标准(21-80) / S3 摘要(81-300) / S4 极限(>300)，少则精多则省 |

---

## 快速开始（30 秒入门）

### 方式一：自然语言触发

直接对 AI 说：

> "帮我检查一下当前项目装了哪些 Skill，看看有没有冲突或重复的"

→ AI 自动启动全流程扫描，最终在 `.medic/` 下生成 `skill_audit_report_<时间戳>.md`。

### 方式二：CLI 命令

```bash
# ① 工具自检（确认 SkillMedic 本身没问题）
python .trae/skills/skill-medic/medic_tools/run.py ping <project_root>

# ② 生成报告骨架（扫描 + 冲突 + 评分表 + 处方候选，落盘 .medic/）
#    报告第 1/6/7 部分的结论与定级需 AI 在流程中回填，故完整成品请走方式一
python .trae/skills/skill-medic/medic_tools/run.py report <project_root>

# ③ 分步执行（中间产物落盘到 .medic/）
python .trae/skills/skill-medic/medic_tools/run.py scan <project_root> --save
python .trae/skills/skill-medic/medic_tools/run.py conflict <project_root> --save
python .trae/skills/skill-medic/medic_tools/run.py score <project_root> <skill_name> --save   # 逐个 Skill 打分
python .trae/skills/skill-medic/medic_tools/run.py prescribe <project_root> --save
```

### 输出示例

```markdown
# Skill 检查报告

## 1. 给你的结论
### 1.1 健康度总评
- 健康度分布：放心用（L3）｜基本能用（L2）｜不太成熟（L1）｜不建议用（L0）
- 本次检查范围：12 个 Skill

## 5. 冲突与问题
| A x B | 冲突类型 | 冲突点/资源 | 初判严重度 |
|-------|---------|------------|-----------|
| sz-writer x sz-writer-enjoy | 功能重复（C1） | 公文/写作/润色 | 待确认 |

## 7. 行动建议
### 7.1 使用建议（使用者看这里）
### 7.2 改造建议（维护者看这里）
```

> 注意：`run.py report` 产出的是**结构化骨架**——统计数据、清单、冲突矩阵、评分表由工具算出；
> 第 1 部分的结论、第 6 部分的定级、第 7 部分的精确操作需由 AI 在 MED_DEBRIEF 阶段回填才算完成。
> 骨架段落带 `<!-- AI 回填 -->` 注释，回填后删除注释。

---

## 适用场景 vs 不适用场景

| 适用 | 不适用 |
|---------|----------|
| Skill 装了一堆，想清理一下 | 只装了 2-3 个 Skill（没必要扫） |
| 团队想标准化 Skill 生态 | 写代码/改 bug（用 ReqPlan-v3 去） |
| 评估社区新 Skill 值不值得装 | 生成报表/看板（用 conspect 去） |
| Skill 突然开始打架，查原因 | 生成操作手册（用 ManualGen 去） |
| 定期体检，保持 Skill 生态健康 | — |

---

## 冲突检测五维

| 类型 | 代号 | 含义 | 示例 |
|------|------|------|------|
| **同质重复** | C1 | 两个 Skill 做几乎一样的事 | "生成文档"的 Skill 有 3 个 |
| **意图抢占** | C2 | 触发词重叠，AI 不知道选谁 | "分析"同时命中数据 Skill 和代码 Skill |
| **上下文膨胀** | C3 | 每个 Skill 都带一堆 chunk，加载变慢 | 装了 15 个 Skill，每次对话多 3000 token |
| **依赖冲突** | C4 | A Skill 依赖 B，但 B 又依赖 A 或版本不兼容 | 少见但致命 |
| **资源竞争** | C5 | 同时调用同一个 API/端口/数据库 | 两个 Skill 都想用 Chrome DevTools |

---

## 八维成熟度评分

| # | 维度 | 权重 | 考察内容 |
|---|------|------|---------|
| 1 | 触发契约 | 15 | description 是否说清何时用、何时不用 |
| 2 | 流程机制 | 15 | 是否有可执行的分阶段步骤与产物 |
| 3 | 异常与熔断 | 12 | 失败、缺料、异常输入是否有分支与回退 |
| 4 | 产出控制 | 13 | 产出物是否可验证、是否有完成判据 |
| 5 | 边界与上下文 | 12 | 是否限定范围、是否分层加载 |
| 6 | 内容价值密度 | 13 | 指令是否具体可执行、有无冗余说教 |
| 7 | 工程配套 | 10 | 校验脚本、单测、CLI 工具是否齐备 |
| 8 | 维护健康度 | 10 | 版本记录、变更痕迹是否完整 |

**四档定级（固定阈值）**：放心用（L3）≥80 · 基本能用（L2）55~79 · 不太成熟（L1）30~54 · 不建议用（L0）<30

> 评级衡量的是"可靠性/完成度"（能不能稳定达成它承诺的功能），不是"安全性"。
> 阈值与八维定义以 `SKILL.chunks/chunk-05-score.md` 与 `references/rubric-detail.md` 为准，本表为摘录。

---

## 项目结构

```
skill-medic/
├── SKILL.md                    # 主入口（触发契约 + 执行流程）
├── README.md                   # 本文件
├── CHANGELOG.md                # 版本变更
├── 1-manifest/
│   └── skill-manifest.yaml     # Skill 元数据
├── medic_tools/                # CLI 工具层（Python 纯标准库）
│   └── run.py                  # ping / scan / analyze / conflict / score / prescribe / report
├── agents/                     # 7 个 Agent 定义
│   ├── 00-master-controller.md
│   ├── 01-inventory-agent.md   # 清单扫描
│   ├── 02-classifier-agent.md  # 三维分类
│   ├── 03-conflict-agent.md    # 五维冲突检测
│   ├── 04-scorer-agent.md      # 八维评分
│   ├── 05-auditor-agent.md     # 交叉审核
│   ├── 06-synthesizer-agent.md # 处方综合
│   └── 07-reporter-agent.md    # 报告生成
├── protocols/
│   ├── baton-protocol.md       # 接力棒协议
│   └── phase-protocol.md       # 阶段流转协议
├── references/
│   ├── conflict-catalog.md     # 冲突类型详解
│   ├── rubric-detail.md        # 评分细则
│   ├── cli-guide.md            # CLI 使用指南
│   ├── examples.md             # 真实案例
│   └── faq-deep.md             # 进阶 FAQ（12 题）
├── SKILL.chunks/               # 分块按需加载
├── tests/                      # 单元测试（判据回归保护）
└── tools/
    └── check_consistency.py    # 版本一致性 + 零 emoji 自检
```

---

## 版本记录

| 版本 | 核心变化 |
|------|---------|
| v0.5.0 | 判定精度修复：关键词过滤纯数字与分词残片、C2 增加 Jaccard 下限（实测 24 组过报收敛为 2 组真候选）、补「演示文稿/写作编排」功能域、生命周期改用 mtime 兜底；补单测与一致性校验脚本；零 emoji 与 license 合规 |
| v0.4.18 | 四档规模分级策略：S1 精细(≤20) / S2 标准(21-80) / S3 摘要(81-300) / S4 极限(>300)，候选降噪、摘要报告+每域附录、处方聚合按档自动启用 |
| v0.4.17 | 候选降噪与摘要模式 |
| v0.4.x | 八维评分体系 + 五类冲突检测 |

---

## 依赖

- **Python 3.10+**
- **纯标准库**（零第三方依赖，开箱即用）

---

## 许可证

MIT
