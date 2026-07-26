# 旧状态迁移

高风险工作正在进行时不要强制迁移。v2 可以读取旧项目状态。

## 旧文件映射

| 旧文件 | v2 角色 |
| --- | --- |
| `TARGET.md` | 更高权限的结果和 Non-Goals |
| `ACCEPTANCE.md` | 更高权限的验收标准 |
| `WORK_ORDER.md` 或编号工单 | 当前范围权限 |
| `STATUS.md` | 当前证据输入，不是范围权限 |
| `NEXT_ACTIONS.md` | 候选下一步 |
| `PENDING.md` | 阻塞、决策和以后想法 |
| `EVALUATION.md` | 历史决定 |
| `LOOP_RUNS.jsonl` | 只追加的执行证据 |
| `LOOP_STATE.md` | Active Packet 的 Lite 前身 |

## 采用 v2

1. 保留历史文件；
2. 创建 `Docs/ACTIVE_PACKET.md`；
3. 链接当前权威 TARGET、ACCEPTANCE 和 Work Order；
4. 只复制当前阶段投影，不复制历史；
5. 执行前解决冲突；
6. 继续向 `LOOP_RUNS.jsonl` 追加精简记录；
7. 停止扩展重复状态日志。

## 只使用旧协议

没有 Active Packet 时：

- 读取 target、acceptance、当前 Work Order、最新状态、阻塞和一个下一步；
- 保留项目已有状态枚举；
- 只写项目已采用的状态文件；
- 在自然边界建议迁移，不在紧急修复中强制迁移。

范围权限不明确时设置 `Invalid State`。

