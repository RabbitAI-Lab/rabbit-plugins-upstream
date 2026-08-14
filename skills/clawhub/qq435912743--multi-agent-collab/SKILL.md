---
name: multi-agent-collab
version: 1.0.0
description: |
  多智能体协作编排引擎。把问题分解为角色(Analyst/Critic/Integrator 等)，
  多 agent 并行提案→Critic 过滤低质→Integrator 按 scorer 择优/综合。
  实体化"超级智能体(终局)·多智能体协作编排"，支撑规模化协作超越单 agent。
agent_created: true
visibility: public
---

# multi-agent-collab（多智能体协作编排）

> 北极星能力域「超级智能体(终局)·多智能体协作编排」实体化——把"超级智能体"
> 从单体内核扩展到"多角色协作"的规模化形态，逼近超越一线大模型的协作智能。

## 何时使用
- 单 agent 难以一次做对的复杂问题，需要"多视角提案 + 批判择优"。
- 需要角色分工(分析/批判/综合)、并行产出、质量门控。
- 需要可审计的"谁提了什么、为何选中这个"协作轨迹。

## 工作流
1. **角色分工(decompose)**：按问题给各 agent 分配职责与共享上下文。
2. **并行提案(propose)**：每个 agent 基于上下文产出候选。
3. **批判过滤(critique)**：Critic 给每条候选打分/挑刺，低于阈值标记淘汰。
4. **择优综合(integrate)**：Integrator 用 scorer 选最优或融合 top-k。
5. **可靠自验证**：`--selftest` 断言 Critic 淘汰与 Integrator 择优全部正确。

## 运行
```bash
python scripts/collab.py --selftest
# 实际：python scripts/collab.py --problem p.json   （roles/critic/scorer 由调用方注入）
```

## 增强点（融入元进化闭环）
- 自验证：selftest 含"淘汰离谱提案 + 选中正确解"基准。
- 自进化：已注入 learner，纳入 meta-evolver 的 sense/plan/record 闭环。
- 接入：可作为 super-agent-loop 的一个"并行子图"节点，构成超级智能体协作层。

## 已知限制
- roles/critic/scorer 由调用方注入(本技能只管协作编排与门控)。
- 当前为同步串行调度；大规模需加并发/异步层。
- 无 agent 间记忆共享协议，跨轮上下文需调用方维护。
