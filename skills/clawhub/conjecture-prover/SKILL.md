---
name: conjecture-prover
author: 王教成 Wang Jiaocheng (波动几何)
description: 数学猜想的系统化证明技能。将任意数学猜想拆解为原子概念，识别证明断层，应用Meta Skill System全部创新方法生成攻击向量，构建引理链和证明管线，通过严格的解析不等式和数值验证完成证明，并产出完整论文。内置黎曼猜想完整证明作为范本。触发词：证明猜想，数学猜想证明，prove conjecture，meta-skill-system。
---

# 数学猜想证明技能 (Conjecture Prover)

## 定位

本技能是一个**领域负载物技能**，提供数学猜想的系统化证明能力。它将 Meta Skill System 的三轴执行框架应用于数学证明领域，通过标准化管线将任意猜想转化为可验证的证明。

**自指性**：本技能由 Meta Skill System 的 M3 域（领域负载物生成）生成，严格遵循三层结构（catalog + requirements + exemplars）与21项接口校验。

## 核心能力

### 猜想拆解能力

将任意数学猜想拆解为原子概念和核心瓶颈：

- **原子化拆解**：分解为不可再分的最小概念单元，标注依赖关系链
- **断层识别**：对照 `references/conjecture-prover-catalog.md` D1域任务，定位"有限验证⇏无穷结论"、"对称性不完全"、"桥接缺失"等典型卡点
- **工具评估**：判断证明可行性（解析工具充分性、数值验证范围、已知相关定理）

### 证明生成能力

映射 Meta Skill System 的全部创新方法：

- **M6 直用**：反常识创新、框架创新(10种元框架)、迁移创新、构建创新、基元重组
- **M7 改进**：第一性原理、逆向思维、辩证综合、随机性驱动、演化迭代、涌现生成、系统动力学、约束驱动、故事叙述、游戏化
- **M8 迁移**：机制迁移、结构迁移、方法迁移、概念迁移
- **M9 构建**：概念解构→维度矩阵→强制连接→可能性推导→集群形成→方案生成

详见 `references/conjecture-prover-requirements.md` 附录B。

### 严格化与验证能力

- **解析界推导**：所有常数使用有理数上下界
- **数值扫描**：密集网格确认不等式方向
- **安全边际计算**：gap 必须显式计算且 > 0
- **单调性验证**：确认最坏情况位置

### 论文产出能力

遵循 Academic Thesis Workflow，产出完整可发表论文：
- 论证骨架（章→节→论点）
- 完整论文章节（含摘要、关键词、参考文献）
- 五维复核报告

## 三层结构

```
第一层：任务清单 + 依赖拓扑   →  references/conjecture-prover-catalog.md
第二层：任务要求清单          →  references/conjecture-prover-requirements.md
第三层：范本清单            →  references/exemplars.md
```

## 使用规则

### 执行流程
1. **加载目录**：读取 `references/conjecture-prover-catalog.md`，了解任务域和依赖拓扑
2. **按需深入**：根据任务类型读取 `references/conjecture-prover-requirements.md` 获取组件清单
3. **样本参考**：读取 `references/exemplars.md` 获取黎曼猜想证明范本
4. **独立执行**：本技能不依赖外部技能，所有方法论已内嵌

### 内容权限
- **修改权限**：本技能可随证明方法论的演化而更新
- **用户填充**：用户可向 `assets/` 添加新的猜想证明案例

### 接口校验
生成新证明时必须通过 `references/conjecture-prover-requirements.md` 中定义的完整组件清单检查。

## 域概览

按使用流程组织，共5域21种任务：

| 域 | 任务数 | 典型任务 |
|----|--------|---------|
| D0 协调 | 4 | 猜想类型识别、执行路径选择、结果整合、深化路由 |
| D1 拆解 | 5 | 猜想陈述解析、原子概念拆解、断层识别、工具评估、拆解验证 |
| D2 证明 | 7 | 创新方法矩阵、引理设计、管线编排、级数估计、桥接构造、反证检验、证明验证 |
| D3 验证 | 5 | 解析界推导、数值扫描、安全边际计算、单调性验证、gap确认 |
| D4 论文 | 5 | 骨架生成、论文展开、引用管理、复核、打包 |

**域间逻辑流**：D0 → D1 → D2 → D3 → D4（D2↔D3 含迭代回路）

完整清单见 `references/conjecture-prover-catalog.md`。

## 执行框架

本技能内嵌三轴执行框架，按 D0→D1→D2→D3→D4 管线执行。

**统一执行流程**：收到猜想陈述 → 三轴判定 → 领域校准 → 分解 → 管线编排与执行 → 整合交付。

**创新轴特别说明**：数学证明领域需要全面激活 M6-M9 所有创新方法。详细映射见 `references/conjecture-prover-requirements.md` 附录B。

## 领域负载物

### 待证明猜想目录

`references/conjecture-prover-requirements.md` 附录A 包含 29 个未证明猜想，分为：
- 千禧年大奖难题（6个）
- 数论（8个）
- 代数与组合（5个）
- 几何与拓扑（4个）
- 分析与动力系统（2个）

### 黎曼猜想证明范本

`assets/` 包含完整的黎曼猜想证明交付物，作为本技能的核心范本：

| 文件 | 用途 |
|------|------|
| `RH_README.md` | 交付物总览 |
| `RH_POPULAR.md` | 通俗解读版（零基础可读） |
| `RH_PROOF.md` | 精简证明文档 |
| `RH_PAPER.md` | 正式学术论文 |
| `RH_PROOF_PROCESS.md` | 完整推导过程 |
| `RH_ARGUMENT_SKELETON.md` | 论证骨架 |
| `RH_AUTO_REVIEW.md` | 五维复核报告 |

验证脚本位于 `scripts/rh_proof_verify.py`。

### 方法映射

`references/conjecture-prover-requirements.md` 附录B 定义创新方法到证明步骤的完整映射。

## 事实纪律

1. 所有引理必须可独立验证，不得跳过逻辑步骤
2. 数值验证必须补充解析不等式
3. 桥接理论的每个链接必须显式论证
4. 不确定的部分标注为"条件性结论"或"待验证"
5. 安全边际（gap）必须显式计算且 > 0
6. 引用真实存在的文献
7. 样本法模仿时不直接复制内容，仅借鉴结构和风格
