# 按需路由索引

SKILL.md 只保留身份、流程和边界；下面是唯一出口，按问题选一份读，不要整包加载。

| 你要做什么 | 读这个 | 里面有什么 |
| --- | --- | --- |
| 先跑起来：host / audit / plan / apply / verify / restore | `docs/usage.md` | 命令顺序、dry-run、冲突处理和事务目录 |
| 核对 plan、manifest、verify 的字段与退出码 | `docs/execution-contract.md` | 机器契约、动作白名单、恢复语义 |
| 核对审计 JSON 字段和读取边界 | `docs/audit-json-contract.md` | 只读证据、warning/unknown 码、脱敏规则 |
| 理解三层账本和整体设计 | `docs/architecture.md` | Hot/Warm/Cold、量化方法、适配器分层 |
| 判断某个动作能不能做 | `docs/safety.md` | allowlist、禁止项、隔离与回滚 |
| 验收和回归清单 | `docs/acceptance.md` | PASS/FAIL 门槛、发布专项验收与阶段归档说明 |
| 对接非 Codex 宿主 | `references/adapter-contract.md` | 能力三态、接口、缺失 Home 时的降级 |
| 和 Ponytail、Skill Architect、Memory Orchestrator 分工 | `references/integration-routing.md` | 唯一职责、交接数据、降级规则 |
| 测量固定注入、判断漂移、跑发布闸门 | `docs/injection-measurement.md` | 七块口径、状态机、57,344 B 闸门、隐私边界 |
| 查七块预算与 MCP 口径 | `references/budgets.md`、`references/mcp-measure.md` | 逐块数字、MCP `tools/list` 与 App 整体 `UNMEASURED` 的区别 |
| 理解 Hot/Warm/Cold 的字段口径 | `references/context-model.md` | 分层定义和 Token/磁盘账本 |
| 改脚本前看入口 | `scripts/README.md` | 整体瘦身与注入测量脚本的职责与约束 |
| 发布记录与版本变化 | `CHANGELOG.md` | 版本、兼容性和已知缺口 |

规则：只有 Hot 或实际避免加载的 Warm 才算 Token 收益；Cold 只算磁盘。
