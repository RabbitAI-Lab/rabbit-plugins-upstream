# inbox/ — 候选区

官方但信息不全、或待补全的候选条目暂存于此，**不进 core**。

- 何时写入：检索到官方来源但信息不足以写完整条目时。
- 规则：frontmatter 标 `confidence: unverified` 或缺失关键字段。
- 补全后：按入库标准补全，经用户确认后移入 core/。

## 当前登记（缺口 / 待补）

### 范式缺口：去中心化 / 对等编排（confidence: unverified）

- **缺口**：core 案例的「编排」维度全是中心化 / 网关式，缺一个**去中心化、对等（peer-to-peer）、无中心调度**的 verified runtime harness 作对照。
- **为何暂缺**（防污染门的诚实结论）：现实中去中心化多智能体的代表（如 Microsoft AutoGen 的分布式 actor runtime、Fetch.ai uAgents）本质是 **import 进来写代码的「库/语言框架」**，按本 skill 的概念边界（运行时 vs 库）属**排除项**，只作"模式来源"（见 `pattern-actor-model.md`），不作 harness 案例入库。截至目前，未找到同时满足"去中心化编排 + 运行时宿主（可独立启动/配置装配）+ 官方可交叉核验"的案例。
- **设计时怎么办**：命中"去中心化 / 对等编排"象限时，**从第一性原理 + actor-model 模式推演**（见 `h-framework.md` 的范式全空间判据），并在设计文档里显式标注"无成熟 harness 案例背书，属框架内推演"。发现合格的官方 runtime 案例后，按入库标准补全、经用户确认再移入 core/（占用流动层名额，当前 2/5，尚有余量）。
