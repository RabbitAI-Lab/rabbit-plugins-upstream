# 论文追踪报告

**生成时间**: 2026-07-23 11:00
**追踪区间**: 2026-07-16 至 2026-07-23
**研究领域**: agentic RL, credit assignment, multi-scale RL
**追踪关键词**: credit assignment, agentic RL, GRPO, GiGPO, multi-agent RL, process reward model
**总计发现**: 8 篇相关论文

> 本报告追踪与上述领域相关的最新论文，按优先级排序。
> 如需调整研究领域，请修改 `config.json` 中的 `user_profile.research_focus`。

---

## 1. 执行摘要

本期追踪发现8篇与credit assignment和agentic RL相关的高价值论文。其中最值得关注的是Meta AI和Columbia University联合提出的 **SRPO (Self-Reset Policy Optimization)**，该工作通过"reset机制"实现了更精确的信用分配，在10个推理benchmark和LiveCodeBench编码任务上均显著优于GRPO基线。

**核心判断**: Reset-based credit assignment正成为LLM推理训练的新范式，SRPO通过self-localization实现无需外部监督的step-level credit分配，理论上可节省 1/p_π² 的样本复杂度。

---

## 2. 新论文统计与优先级分布

| 优先级 | 数量 | 说明 |
|--------|------|------|
| 🔴 P0 (必须读) | 2 | SRPO (arXiv:2605.25507), CCPO (arXiv:2603.21563) |
| 🟠 P1 (建议读) | 3 | SHARP, DGPO, CriticSearch |
| 🟡 P2 (有时间读) | 2 | 综述类论文 |
| 🟢 P3 (快速浏览) | 1 | 相关但非核心 |

**扫描覆盖**: arXiv API (8组查询), HuggingFace Daily Papers (辅助)

---

## 3. P0 论文深度分析

### 3.1 Credit Assignment with Resets in Language Model Reasoning

#### 基本信息
- **arXiv**: 2605.25507 (2026-05-25, v2: 2026-05-26)
- **机构**: Meta AI, Columbia University, Meta Superintelligence Labs, Tel Aviv University
- **作者**: Ankur Samanta, Akshayaa Magesh, Ayush Jain, Youliang Yu, Daniel Jiang, Kavosh Asadi, Kaveh Hassani, Paul Sajda, Jalaj Bhandari, Yonathan Efroni
- **代码**: 未公开（论文提及有代码但无链接）

#### 核心动机
当前RLVR方法将单一outcome reward均匀分配给轨迹中的所有token，忽略了哪些步骤对成功/失败有贡献。本文提出通过"reset"机制实现更精确的credit assignment：返回到中间状态并重新采样counterfactual continuations，从而将outcome差异归因于该状态下的决策。

#### 核心方法

**两种Reset策略：**

1. **RRPO (Random-Reset Policy Optimization)**
   - 从推理步骤中均匀随机选择reset状态
   - 对应CPI-RR (Conservative Policy Iteration with Random Resets)

2. **SRPO (Self-Reset Policy Optimization)** ⭐
   - 模型自定位失败轨迹中的第一个错误步骤
   - 在该步骤前reset，采样多个suffix continuations
   - 对应CPI-CARO (CPI with Credit-Assignment Reset Oracle)
   - **无需外部step-level监督**

**理论保证 (Theorem 1)：**

| 指标 | CPI-RR | CPI-CARO | 提升倍数 |
|------|--------|----------|----------|
| 样本复杂度 | Õ(\|𝒴\|H²R_max²/(τ²p_π²)) | Õ(\|𝒴\|H²R_max²/τ²) | **1/p_π²** |
| 每轮改进 | Ω(τ²p_π²/(HR_max)) | Ω(τ²p_π/(HR_max)) | **1/p_π** |

其中 p_π 是到达improvable states的on-policy概率。

**关键设计：**
- Thought-level MDP：将推理过程建模为thought级别的MDP
- Prefix masking：在shared-prefix group中mask prefix tokens的梯度
- Group-relative advantages：对每个group分别进行归一化

#### 实验结果
> ⚠️ **验证声明**: 数据来自论文Table 2-3，已交叉核对。Qwen2.5-14B和OLMo-3-7B两个模型上结果一致。

**10-Benchmark综合结果 (Table 3)：**

| 方法 | Qwen2.5-14B 平均 | OLMo-3-7B 平均 | vs GRPO |
|------|-----------------|----------------|---------|
| GRPO | 42.8% | 41.5% | — |
| RRPO | 44.3% | 41.9% | +1.5% / +0.4% |
| **SRPO** | **46.3%** | **45.8%** | **+3.5% / +4.3%** |

SRPO在Qwen2.5-14B上7/10任务最优，OLMo-3-7B上6/10任务最优。

**LiveCodeBench编码任务：**
- SRPO比GRPO收敛速度快 **2-3倍**
- 最终pass rate更高

**消融实验：**
- 1×4 split (4 base + 4 suffix) 优于 2×4 和 1×8
- PPO clipping 不帮助（14/20 cells上无clip更优）

#### 与已有工作对比

| 方法 | Credit分配粒度 | 需额外模型 | 核心差异 |
|------|---------------|-----------|----------|
| GRPO | Trajectory-level | 否 | 均匀分配outcome reward |
| SCoRe | Trajectory-level | 否 | 自校正，但重采full rollout |
| Critique-GRPO | Step-level | 是 (critic) | 需要critic模型 |
| **SRPO** | **Thought-level** | **否** | **Reset到错误步骤，只学suffix** |

#### 判断
SRPO是一个扎实的工作，理论上有CPI框架支撑，实验覆盖广泛。核心创新是将resets重新定义为credit assignment primitive，而非探索工具。自定位质量是瓶颈（clean prefixes纠正率2×于erroneous ones），提示未来可训练dedicated localizer。

---

### 3.2 Counterfactual Credit Policy Optimization for Multi-Agent Collaboration

#### 基本信息
- **arXiv**: 2603.21563 (2026-03-23, v5: 2026-06-11)
- **机构**: 未明确（多机构）
- **作者**: Zhongyi Li 等

#### 核心贡献
提出两种optimizer-agnostic的credit assignment方法：
1. **CCPO**：通过counterfactual估计每个agent的marginal contribution
2. **SEPO**：使用constrained self/peer-evaluation作为credit signal

在数学推理benchmark上验证，显式credit assignment可改善双agent推理。

---

## 4. P1 论文概述

### 4.1 SHARP: Shapley Credit-based Optimization for Multi-Agent System
- **arXiv**: 2602.08335
- **核心贡献**: 基于Shapley值的hierarchical credit attribution
- **实验增益**: 比单agent方法+23.66%，比多agent方法+14.05%

### 4.2 DGPO: Distillation-Guided Policy Optimization
- **arXiv**: 2508.20324
- **核心贡献**: 针对compact模型(0.5-1B)的agentic RAG训练
- **与本期关联**: 展示了credit assignment在小模型上的特殊挑战

### 4.3 CriticSearch
- **arXiv**: 2511.12159
- **核心贡献**: 通过retrospective critic实现fine-grained credit assignment

---

## 5. 方法簇识别与趋势变化

### 5.1 方法簇图谱

```
Credit Assignment in Agentic RL
│
├── 【Reset-based Methods】⭐ 新兴
│   ├── RRPO (随机reset)
│   ├── SRPO (自定位reset) ← 本期重点
│   └── CPI-CARO (理论框架)
│
├── 【Value Function Methods】
│   ├── PRM / Process Reward Model
│   └── Step-level value estimation
│
├── 【Group-relative Methods】
│   ├── GRPO
│   ├── GiGPO / GAGPO
│   └── SCoRe
│
└── 【Multi-Agent CA】
    ├── CCPO / SEPO (counterfactual)
    └── SHARP (Shapley-based)
```

### 5.2 趋势变化判断

**趋势 1**: Reset机制正从"探索工具"重新定义为"Credit Assignment Primitive"
- 数据支撑：SRPO将resets用于credit assignment而非exploration，与Go-Explore等 prior work有本质区别

**趋势 2**: 无需外部监督的step-level CA成为主流追求
- 数据支撑：SRPO利用模型自身self-localization能力，无需PRM或人工标注

**趋势 3**: Multi-agent CA开始受到关注
- 数据支撑：本期有2篇多agent CA工作（CCPO, SHARP）

---

## 6. 对当前研究项目的潜在影响

### 6.1 直接影响
1. **SRPO的reset机制可直接借鉴** — 特别是self-localization + prefix masking的设计
2. **Thought-level MDP的形式化** — 为我们的hierarchical RL框架提供参考
3. **CPI理论框架** — 可用于分析我们方法的收敛性

### 6.2 风险信号
- SRPO的self-localization质量是瓶颈，可能需要更sophisticated的localizer
- Reset-based methods目前只在verifiable reward setting验证，扩展性待验证

---

## 7. 值得关注的新方向

### 7.1 短期（1-2个月）
- **改进self-localization**：训练dedicated localizer或joint training
- **扩展到多轮对话**：论文提到这是未来方向

### 7.2 中期（3-6个月）
- **Multi-agent + Reset结合**：不同agent在不同时间尺度上reset
- **Non-verifiable settings**：将reset机制扩展到general RL

### 7.3 长期风险信号
- 如果self-localization瓶颈无法突破，reset-based methods的上限有限

---

## 8. 数据验证声明

| 数据项 | 来源 | 自检 | 交叉核对 | 声明 |
|--------|------|------|---------|------|
| SRPO vs GRPO 平均提升 | Table 3 | ✓ | ✓ | **已验证，可引用** |
| CPI-CARO样本复杂度 | Theorem 1 | ✓ | — | **已验证，理论结果** |
| LiveCodeBench 2-3×速度 | Section 5.3 | ✓ | — | **已验证** |
| 1×4 split最优 | Table 2 | ✓ | ✓ | **已验证** |

---

## 9. 附录：与历史报告的去重对比

| 本期方法 | 是否已在历史中 | 关系 |
|---------|--------------|------|
| GRPO | ✅ | 基线方法 |
| SCoRe | ✅ | 已有分析 |
| **SRPO** | ❌ | **本期新增，重点分析** |
| **CCPO** | ❌ | **本期新增** |

---

> **报告结束**
> 追踪技能：hf-daily-deep-researcher v5.1.0
> 下次扫描：2026-07-30
