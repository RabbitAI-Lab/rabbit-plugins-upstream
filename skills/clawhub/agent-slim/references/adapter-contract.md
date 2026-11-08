# 宿主适配器契约

## 目标

让 Codex 首版实现和未来其他 Agent 适配器共享同一套最小接口，同时避免把未实测的平台能力写成已支持。

## 能力声明

```json
{
  "host": "codex",
  "adapterVersion": "0.1",
  "capabilities": {
    "hot_warm_cold_inventory": "supported|unsupported|unknown",
    "frontmatter_parse": "supported|unsupported|unknown",
    "reference_graph": "supported|unsupported|unknown",
    "token_usage_read": "supported|unsupported|unknown",
    "skill_usage_index": "supported|unsupported|unknown",
    "safe_move": "supported|unsupported|unknown",
    "quarantine": "supported|unsupported|unknown",
    "plugin_management": "supported|unsupported|unknown",
    "plugin_disable": "supported|unsupported|unknown",
    "session_archive": "supported|unsupported|unknown",
    "regression_runner": "supported|unsupported|unknown",
    "rollback": "supported|unsupported|unknown"
  }
}
```

三态含义：

- `supported`：本机文件证据或实现路径已证明该能力可用。
- `unknown`：目录、索引或测试命令缺失，不能确认可用；执行器不得把它当作可用。
- `unsupported`：本技能明确不实现该能力，例如插件配置修改和插件停用。

能力为 `unknown` 时，执行器不得尝试破坏性动作；能力为 `unsupported` 时返回明确错误。适配器必须同时报告检测方式和证据。Home 不存在或不可写时，盘点、解析、引用、移动和隔离能力都必须降级为 `unknown`，不得假装支持。

## 核心对象

| 对象 | 必需字段 |
|---|---|
| Inventory | runId、host、scope、items、unknowns、createdAt |
| Item | id、layer、source、loadedWhen、tokenEvidence、diskBytes、references、riskHints |
| SlimPlan | planId、items、mode、actions、exclusions、rollbackPlan、evidence |
| ApplyResult | transactionId、applied、skipped、failed、quarantine、auditPath |
| VerificationResult | checks、summary、blockingFailures、artifacts |
| RollbackResult | transactionId、restored、failed、hashMatches、notes |

## 方法

1. `inspect(scope) -> Inventory | unsupported`
2. `plan(inventory, policy) -> SlimPlan | unsupported`
3. `apply(plan, mode) -> ApplyResult | unsupported`
4. `verify(plan, suite) -> VerificationResult | unsupported`
5. `rollback(transactionId) -> RollbackResult | unsupported`

所有方法必须幂等或明确返回已有事务，不得重复执行后产生第二份不一致变更。

## 错误码

| 错误码 | 含义 | 调用方动作 |
|---|---|---|
| CAPABILITY_UNSUPPORTED | 宿主无该能力 | 跳过并标待确认 |
| SCOPE_VIOLATION | 目标越界 | 立即停止 |
| EVIDENCE_MISSING | 缺少关键证据 | 降级为只读建议 |
| REGRESSION_FAILED | 能力回归失败 | 回滚 |
| ROLLBACK_FAILED | 回滚失败 | 阻断并人工恢复 |
| PRIVACY_BLOCKED | 隐私或秘密检查失败 | 阻断发布 |

## 平台限制

- Codex 首版只实现经当前宿主实测的能力。
- 其他 Agent 的适配器可以复用对象和方法命名，但不能复用未经验证的命令或假设。
- 只定义接口、未实现和未验证的宿主统一标记 `architecture-only`。
