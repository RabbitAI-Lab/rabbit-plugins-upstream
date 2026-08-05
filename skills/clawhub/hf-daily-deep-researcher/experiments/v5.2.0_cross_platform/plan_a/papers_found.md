# 方案 A 搜索结果（kimi_search 完整方案）
# 搜索时间: 2026-07-29
# 搜索窗口: 2026年7月（扩展至全月，因 7/22-29 范围论文极少）
# 搜索工具: kimi_search（2组查询）+ web_fetch（1组 arXiv API，失败）

## 搜索统计
- kimi_search 调用次数: 2 组
- 去重后论文数: 约 11 篇（含非7月论文）
- 7月论文数: 1 篇（arXiv:2607.04713，日期 2026-07-06）

## 论文列表

### 1. 2026年7月论文

#### arXiv:2607.04713
- 标题: Reward-Swap Policy Optimization for Multi-Turn LLM Agents
- 日期: 2026-07-06
- 作者: 未完整提取
- 摘要: 通过 reward-swap 机制，RSPO 确保采样轨迹的多样性，同时保证优化一致性。先用 dense process rewards 训练 Agent A 得到 Agent B，Agent B 与环境交互生成轨迹存入 replay buffer，奖励恢复为 outcome rewards，然后 Agent A 用 outcome rewards 更新，同时从 replay buffer 采样做 off-policy 更新。
- 相关度: 高（Credit Assignment + Multi-Turn Agent）

### 2. 2026年其他月份论文

#### arXiv:2605.00425
- 标题: （未完整提取，关于 LLM to Agentic RL 的论文）
- 日期: 2026年5月
- 摘要: 讨论从 single-turn 到 multi-turn agentic settings 时 sparse rewards 的问题，以及 step-level supervision 的必要性
- 相关度: 高

#### arXiv:2605.30928
- 标题: Enhancing Human-Likeness in RL Agents via Hierarchical Macro Action Quantization
- 日期: 2026-05-29
- 作者: Quoc-Huy Tran 等
- 摘要: 提出 HiMAQ，通过两级向量量化将人类演示编码为 macro actions
- 相关度: 中（Hierarchical RL，间接相关）

#### arXiv:2604.09459
- 标题: From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models
- 日期: 2026-04-10
- 作者: Chenchen Zhang（独立研究者）
- 摘要: 综述了 47 种 CA 方法，按粒度（token/segment/step/turn/multi-agent）和方法论（Monte Carlo/TD/model-based/game-theoretic/information-theoretic）分类
- 相关度: 极高（Credit Assignment 综述）

#### arXiv:2603.21563
- 标题: Counterfactual Credit Policy Optimization for Multi-Agent Collaboration
- 日期: 2026-03-23
- 作者: Zhongyi Li 等
- 摘要: 提出 CCPO 和 SEPO，通过 counterfactual 估计 agent 的边际贡献，将联合结果转换为 agent-specific 学习信号
- 相关度: 极高（Multi-Agent Credit Assignment）

#### arXiv:2602.03719
- 标题: （未完整提取，关于 Credit Assignment 的论文）
- 日期: 2026年2月
- 摘要: 讨论 Monte Carlo estimation（VinePPO, Tree-GRPO, ReasonRAG）和 Explicit step-level reward methods（GiGPO, StepSearch, MT-GRPO, CriticSearch）
- 相关度: 高

#### arXiv:2601.21754
- 标题: Language-based Trial and Error Falls Behind in the Era of Experience
- 日期: 2026-01-29
- 作者: Haoyu Wang 等
- 摘要: 提出 SCOUT，用轻量级 scouts 探索环境动态，收集轨迹后通过 SFT 和 multi-turn RL 激活 LLM 的 latent world knowledge
- 相关度: 中（Agentic RL，间接相关）

#### arXiv:2601.06794
- 标题: No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- 日期: 2026-01-11
- 作者: Zhicong Li 等
- 摘要: 提出 ECHO，通过同步共进化循环联合优化 policy 和 critic，解决 static critic 随 policy 进化而失效的问题
- 相关度: 高（Credit Assignment + Critic）

### 3. 2025年及更早论文

#### arXiv:2510.13036
- 标题: Repairing Reward Functions with Feedback to Mitigate Reward Hacking
- 日期: 2025-10-14
- 相关度: 中（Reward Design，间接相关）

#### arXiv:2510.11062
- 标题: Stronger-MAS: Multi-Agent RL for Collaborative LLMs (AT-GRPO)
- 日期: 2025-10-13
- 相关度: 高（Multi-Agent RL）

#### arXiv:2509.25582
- 标题: Safe In-Context RL (SCARED)
- 日期: 2025-09-29
- 相关度: 中（Safe RL，间接相关）

#### arXiv:2406.13930
- 标题: ME-IGM: Individual-Global-Max in Maximum Entropy Multi-Agent RL
- 日期: 2024-06-20
- 相关度: 中（Multi-Agent Credit Assignment）

## 附加发现

### GitHub 资源库
- xxzcc/Awesome-Credit-Assignment-in-LLM-RL
- 2026.07 Refresh 中添加了多篇新论文（无明确 arXiv ID）：
  - DelTA (2026) — Token-level credit assignment
  - SCRL (2026) — Curriculum RL for credit assignment
  - TRIAGE (2026) — Role-typed credit assignment for agentic RL
  - OAR (2026) — Outcome-grounded advantage reshaping
  - CRAFT (2026) — Counterfactual credit from sibling rollouts
  - SC-GRPO (2026) — Self-conditioned credit assignment
  - GRAIL (2026) — Gradient-reweighted advantages
  - VPR (2026) — Verifiable process rewards for agentic reasoning
  - PivoARL (2026) — Pivotal-aware self-feedback retry

## 搜索问题记录
- arXiv API 日期范围查询报 500 错误
- HuggingFace Daily Papers 页面 fetch 失败
- kimi_search 的日期范围过滤语法未生效（返回了全年论文）
