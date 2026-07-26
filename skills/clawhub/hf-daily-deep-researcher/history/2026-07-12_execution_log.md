# 执行记录

| 日期 | 扫描区间 | 发现论文数 | P0 | P1 | P2 | 报告 doc_id | 日志 doc_id |
|------|---------|-----------|----|----|----|------------|------------|
| 2026-07-12 | 2026-07-05 ~ 2026-07-12 | 1 | 1 | 0 | 0 | QA2qduqVeoIcdhxiGwactQ4gnmd | ALf0d8uHVopBZ1xleYGc1EMKnud |

### 2026-07-12 执行详情

- **扫描模式**: 轻量扫描（7天窗口）
- **搜索策略**: arXiv API (cs.LG, cs.AI) + kimi_search 多关键词并行（8组关键词）
- **P0 论文**: SAO: Single-Rollout Asynchronous Optimization for Agentic RL (arXiv:2607.07508, 清华, 2026-07-08)
- **验证状态**: 所有实验数据执行三级验证（自检→交叉核对→显式声明）
- **报告状态**: ✅ 已生成并保存
- **飞书通知**: ⚠️ 需要用户授权，未能自动发送

### 发现论文详情

**SAO (P0)**
- 标题: Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning
- arXiv: 2607.07508
- 日期: 2026-07-08
- 机构: Tsinghua University
- 作者: Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong
- 核心创新:
  1. Single-rollout sampling 替代 GRPO group-wise
  2. Direct Double-Sided Importance Sampling (DIS)
  3. Skip-Observation Token-Level GAE
  4. Frozen-Attention Value Model
  5. Faster Value Update (K=2)
- 实验结果: AIME2025 97.3% vs GRPO 84.2%; SWE-Bench 29.8% vs GRPO 27.0%
- 训练稳定性: 1000+ steps 稳定 vs GRPO 160 steps 崩溃
- 部署状态: 已用于 GLM-5.2 (750B-A40B) 训练管线
