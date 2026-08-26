# 知识库索引（knowledge/index.md）

> 轻量索引：先读本文件定位，再按需读详文。本文件只存 H+P 标签 + 一句话定位，常驻、很小。

## 使用方式（渐进三档读取）

1. 扫下表，定位"当前要设计的层"有哪些案例/模式相关。
2. 读选中条目的 frontmatter 摘要确认相关性。
3. 只读 1–2 个条目的完整详文。

---

## 框架案例（frameworks/core/）

| 框架 | 一句话定位 | P·扩展 | E | T | C | S | L | V | 原创点 |
|---|---|---|---|---|---|---|---|---|---|
| DeepSeek Harness | 一切皆插件、无特权内核 | 插件化(激进) | 循环即插件 | MCP/defineTool | 组装注入 | 事件溯源日志 | 生命周期/审批 | 轨迹回放 | 无特权内核·Cordis·事件溯源 |
| Hermes Agent | 自进化、文件即记忆 | 插件化 | 自进化循环 | 40+工具/MCP | 文件即记忆 | Markdown 记忆 | 审批/密钥拦截 | 自修复验证 | 自进化·文件即记忆 |
| Claude Code | 产品级 coding agent | 插件化 | loop+subagents | 内置工具/MCP | CLAUDE.md/压缩 | auto memory/JSONL | hooks/权限 | checkpoint/回滚 | subagent 隔离·hooks |
| Codex Harness | 原生 agent 运行时 | 插件化 | thread/turn | 内置+动态加载 | 上下文压缩 | thread 持久化 | HITL/中断 | 事件流/benchmark | app-server·Item/Turn/Thread |
| OpenClaw | 网关/多渠道 agent OS | 插件化 | 网关+engine | 3200+skills | 矢量记忆/会话隔离 | SQLite+矢量 | 权限分离/ClawKeeper | 审计/回放 | 权限分离·网关化 |

> 详细见 `frameworks/core/` 下各条目文件。

---

## 跨领域模式（patterns/）

| 模式 | 来源领域 | 可迁移到 | 一句话 |
|---|---|---|---|
| event-sourcing | 数据库/软件工程 | S / V | 只追加不修改，事件流是单一真相源 |
| dependency-injection | 软件工程 | P(扩展方式) / T | 内核极薄，能力靠注入，可逆注册 |
| graph-state-machine | 工作流/编排 | E | 用图定义状态与流转，显式声明 |
| declarative-configuration | DevOps/基础设施 | P(配置方式) | 用配置描述行为，而非写死代码 |
| capability-security | 安全 | L / T | 最小权限，按能力授予而非按身份 |
| pure-function-effects | 编程语言 | S / P | 副作用显式化、可逆、可组合 |
| immutable-state | 函数式编程 | S / C | 状态不可变，变更即新版本 |
| cqrs | 软件工程 | S / V | 读写分离，命令与查询走不同路径 |
| actor-model | 并发/分布式 | P(编排) / E | 隔离实体间消息传递，天然并发 |
| reversible-computation | 编程语言 | L / P | 副作用可回滚，卸载即清理 |

> 详细见 `patterns/` 下各条目文件。

---

## 容量状态

- 常驻层（pinned）：5 / 5（用户指定，默认不替换）
- 流动层（rotating）：0 / 5
- core 总量：5 / 10
- archive/：空；inbox/：空
