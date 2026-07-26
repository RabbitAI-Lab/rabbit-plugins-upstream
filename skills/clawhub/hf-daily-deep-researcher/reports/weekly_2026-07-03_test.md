# Agentic RL / Credit Assignment 周报

**报告周期**: 2026-06-25 ~ 2026-07-03  
**生成时间**: 2026-07-03 13:15  
**版本**: v4.1.2-test

---

## 本周新发现（10 篇）

### 🔴 P0 级（里程碑/核心方法）

#### 1. iStar: Agentic RL with Implicit Step Rewards
- **arXiv**: 2505.xxxxx (OpenReview, v3 2025-09-28)
- **作者**: Xiaoqian Liu, Ke Wang, Yuchuan Wu, Fei Huang
- **核心**: 隐式过程奖励模型（Implicit PRM），与策略模型交替优化，通过轨迹级 DPO 目标生成隐式步级奖励
- **亮点**: 无需额外 rollout 或显式步标签，兼容 PPO/GRPO/RLOO/REINFORCE++
- **性能**: WebShop 86.5% success, VisualSokoban 91.7%, SOTOPIA 硬场景 +14% (self-chat), +48% (vs GPT-4o)
- **与已有工作对比**: 
  - vs GiGPO: 更细粒度 credit assignment，不依赖 same-state grouping
  - vs PRIME: token-level 奖励在多 turn 中噪声过大，iStar 在 turn-level 更稳定
- **关联**: 与 HiPER 的 hierarchical advantage 互补，iStar 提供隐式 dense reward，HiPER 提供显式分层估计

#### 2. OPRL: Online Process Reward Learning for Agentic RL
- **arXiv**: 2509.19199 (v2 2025-09-24)
- **核心**: 在线学习 PRM，仅使用 on-policy 轨迹和结果偏好，DPO 派生目标将轨迹偏好转为密集步级奖励
- **理论保证**: 隐式步奖励是偏好一致的、基于势能的 shaping，保持最优策略集不变
- **性能**: 与 iStar 相近（WebShop 86.5%, VisualSokoban 91.7%）
- **区别**: OPRL 强调在线更新（每步用当前策略的 rollout），iStar 强调隐式 PRM 与策略交替优化
- **关联**: 两者都解决同一问题（无标签步级 credit），方法论不同，可对比研究

#### 3. GraphGPO: Graph-Based Credit Assignment
- **arXiv**: 2605.26684 (ICML 2026 Poster, v2 2026-06-01)
- **机构**: NTU
- **核心**: 将所有 rollout 轨迹聚合成统一的状态转移图，估计每个状态到目标的距离，基于距离缩减分配 graph-based advantage
- **创新**: 从"组内比较"（GiGPO）升级到"图全局信息"，挖掘失败轨迹中的有价值步骤
- **关联**: 与 HiPER 的 HAE 框架类似（都利用全局/分层信息），但 GraphGPO 用图结构，HiPER 用层级分解

---

### 🟡 P1 级（重要改进/新方向）

#### 4. DataPRM: Process Reward Modeling for Agentic Data Analysis
- **arXiv**: 2604.24198 (v2 2026-06-20)
- **作者**: Z Qiu, Ningyu Zhang 等
- **核心**: 面向数据分析 Agent 的过程奖励模型，解决通用 PRM 的两个盲区：Silent Error（静默错误）和 Grounding Error（探索误罚）
- **方法**: 环境交互式验证 + 三元奖励策略（正确/可纠正/不可纠正）
- **性能**: DABench 78.73%, TableBench 64.84%（RL 设置）; ScienceAgentBench +7.21%, DABStep +11.28%（TTS 设置）
- **意义**: PRM 从"数学推理"扩展到"数据分析"，验证环境交互对过程监督的重要性

#### 5. AT²PO: Agentic Turn-based Policy Optimization via Tree Search
- **年份**: 2026
- **核心**: Turn-level tree structure + entropy-guided expansion + turn-wise credit assignment
- **关联**: 将 tree search 的 credit 机制引入 turn-level，可能与 MCTS-DPO 有交集

#### 6. A²TGPO: Agentic Turn-Group Policy Optimization
- **年份**: 2026
- **核心**: Turn-group normalization + variance-rescaled accumulation + adaptive turn-level clipping
- **关联**: GiGPO 的 turn-level 扩展，改进组间比较稳定性

---

### 🟢 P2 级（相关/方法改进）

7. **AEM**: Adaptive Entropy Modulation for Multi-Turn Agentic RL (2026) - 响应级熵动态调节 advantage
8. **T²PO**: Uncertainty-Guided Exploration Control (2026) - token-level 不确定性干预 + turn-level 重采样
9. **A³**: Learning CLI Agents with Structured Action Credit (2026) - CLI agent 结构化 action credit
10. **Survey**: From Reasoning to Agentic: Credit Assignment in LLM RL (2604.09459) - 47 方法综述，2D 分类法

---

## 趋势洞察

### 1. 隐式 PRM 成为主流方向
本周 2 篇 P0 论文（iStar, OPRL）都采用**隐式过程奖励模型**，核心共识：
- 显式步标签成本高、有偏、易 reward hacking
- 轨迹偏好 → 隐式步奖励 是更 scalable 的路径
- 与策略模型联合训练/交替优化，形成 self-reinforcing loop

### 2. Credit Granularity 持续下探
- Token-level → Step/Turn-level → Graph-based edge-level
- GraphGPO 将 credit 分配到**状态转移图的边**，比 GiGPO 的 same-state grouping 更细粒度
- 趋势：越细粒度的 credit，越需要全局信息来稳定方差

### 3. 从 Verifiable 扩展到 Unverifiable/Open-ended
- iStar 和 OPRL 都在 SOTOPIA（开放式社交交互，不可验证奖励）上验证
- 核心挑战：开放式环境中状态 rarely overlap，传统 same-state grouping 失效
- 解决方案：隐式 PRM 不依赖状态重叠，只用轨迹偏好

### 4. PRM 应用领域扩展
- DataPRM 将 PRM 从数学/代码扩展到**数据分析**
- 关键发现：通用 PRM 在数据分析中 fail 的两个新模式（Silent Error, Grounding Error）
- 启示：不同 agent 领域可能需要 domain-specific PRM

---

## 与现有工作的关联

| 本周论文 | 已有方法 | 关系 |
|---------|---------|------|
| iStar | GiGPO, PRIME | 替代/改进：不依赖 same-state overlap，比 token-level 更稳定 |
| OPRL | iStar | 平行工作：同目标（无标签步级 credit），不同优化路径 |
| GraphGPO | GiGPO, HiPER | 扩展：从组内比较 → 图全局信息；从层级分解 → 图结构 |
| DataPRM | AgentPRM, SWE-PRM | 领域扩展：从通用 agent → 数据分析专用 |
| AT²PO | MCTS-DPO, Turn-PPO | 方法融合：tree search + turn-level credit |

---

## 可跟进问题

1. **iStar vs OPRL 的系统性对比**：两者目标相同，方法不同（交替优化 vs 在线学习），benchmark 性能相近，哪个更稳定/更易扩展？
2. **GraphGPO 与 HiPER HAE 的结合**：GraphGPO 的图全局信息 + HiPER 的层级分解，能否互补？
3. **隐式 PRM 的理论极限**：步级奖励的方差下界？何时隐式奖励会失效？
4. **DataPRM 的通用性**：三元奖励策略是否可迁移到其他 agent 领域（如软件工程、网页导航）？

---

*报告由 HF Daily Deep Researcher v4.1.2 自动生成*
