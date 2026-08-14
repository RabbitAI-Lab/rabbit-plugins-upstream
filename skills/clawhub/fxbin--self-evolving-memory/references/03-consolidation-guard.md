# 模块三：记忆巩固守卫

本模块是大巩固与微巩固的**唯一事务真相源**。模块九和模块十一只声明业务 write-set 与校验项，不得另定义锁、run-id、快照、提交或恢复规则。

### 触发时机

- 大巩固可手动触发；Host 提供 Calendar/调度器时可建议每日低峰期触发
- 微巩固由模块十一的重大事件触发，但必须走与大巩固相同的事务协议
- 没有调度能力时只输出手动运行清单，不声称后台自动执行

### 不变量

1. `SOUL.md` 在大巩固和微巩固前后必须**字节级不变**；身份观察只能追加到 `self-reference/growth-journal.md`
2. `SECRET.md` 不属于普通巩固 read-set/write-set，不进入上下文、RAG、preimage 或日志；它只存 locator 与脱敏元数据且权限为 `0600`
3. 每个 run 必须在任何业务写入前封存**完整 write-set** 的 preimage/tombstone manifest
4. 不允许随机抽查、不允许部分提交、不允许“超时保留已完成部分”
5. 任一写入、read-back、哈希或业务校验失败，必须回滚整个 write-set；恢复未完成前禁止启动新 run

### 共享排他锁与唯一 run-id

- 大/微巩固共享锁目录：`self-reference/.consolidation.lock/`
- 以原子“仅当不存在时创建目录”获取锁；目录内 `owner.json` 记录 `run_id`、`kind`、`started_at` 和调用方。获取失败即停止，不等待并发写入
- `run_id` 格式：`YYYYMMDDTHHMMSSffffffZ-<至少8位随机nonce>`。不得只用分钟时间戳
- 事务目录：`self-reference/snapshots/<run_id>/`；不同 run 永不复用目录
- 遇到疑似陈旧锁不得直接删除：先读取 owner 与事务 manifest，按恢复状态机完成恢复或报告 `recovery_failed`

### 完整 write-set manifest

在持锁状态下，业务模块先声明本轮所有可能修改、创建、压缩或删除的**业务路径**。大巩固通常包括即时层目标（不含 `SOUL.md`/`SECRET.md`）、`recent_memory/index.json`、被压缩的 episodic 文件、promotion log、growth/user/relationship、当日日记，以及启用模块产生的图谱、主题、Forest、角色切片和问题池。微巩固至少包括事件图谱、主题索引、`MEMORY.md`、角色切片和问题池中的实际目标。

控制面文件明确排除在可恢复 business write-set 之外：锁目录、`owner.json`、事务 `manifest.json`、`.complete`、`self-reference/transaction-audit/` 下的 canonical audit projection，以及由 projection 重建的 consolidation/rollback/micro 日志视图。恢复 business write-set 不得覆盖或删除这些控制面证据。

`manifest.json` 至少包含：

```json
{
  "run_id": "20260721T002500123456Z-a1b2c3d4",
  "kind": "full",
  "state": "preparing",
  "business_outcome": null,
  "audit_state": "not_started",
  "created_at": "2026-07-21T00:25:00Z",
  "write_set": [
    {
      "target": "recent_memory/index.json",
      "existed": true,
      "preimage": "preimages/recent_memory/index.json",
      "sha256_before": "<hex>",
      "sha256_after": null
    },
    {
      "target": "self-reference/diaries/2026-07-21.md",
      "existed": false,
      "preimage": null,
      "sha256_before": null,
      "sha256_after": null
    }
  ]
}
```

- 对已存在目标保存逐文件 preimage，并逐一 read-back 计算 SHA-256；任何不一致都中止且不得业务写入
- 对不存在目标记录 `existed:false` tombstone；回滚时删除本 run 新建的对应目标
- 路径必须规范化为 Agent 工作目录内的相对路径，拒绝 `..`、符号链接逃逸和 write-set 外写入
- preimage 全部验证后，将 manifest 状态写为 `snapshot_complete`，再创建事务目录内 `.complete`。`.complete` **只表示回滚材料封存完成，不表示业务提交**

### 状态机与提交

合法状态仅为：

```text
preparing -> snapshot_complete -> mutating -> validating
                                      |             |
                                      +-> rollback_pending <-+
                                                |
                                                v
                                            restoring

validating --business_outcome=committed--> audit_pending
restoring  --business_outcome=rolled_back--> audit_pending
audit_pending -> finalizing_audit -> committed | rolled_back
business restore failure or audit durability failure -> recovery_failed (lock retained)
```

执行规则：

1. 只有 `.complete` 存在且 manifest=`snapshot_complete` 时才能进入 `mutating`
2. 每次业务写入后立即 read-back，计算 `sha256_after` 并更新 manifest；write-set 外写入视为失败
3. 完成业务校验前保持排他锁；`SOUL.md` 另做运行前后 SHA-256 比较，必须相同
4. 所有业务目标验证完成后，先封存 `business_outcome=committed` 的终态 outcome manifest；失败路径必须精确恢复全 business write-set 后封存 `business_outcome=rolled_back`
5. outcome manifest 之后必须完成下节 canonical audit durability 闭环，才能把 state 置为 `committed`/`rolled_back` 并释放锁；不允许先释放锁后补审计
6. 超时、取消、工具错误、容量/格式失败一律进入 `rollback_pending`，不得保留部分业务结果

### Canonical transaction audit

canonical audit 是控制面元数据，不属于可恢复 business write-set。每个 run 使用 create-only 路径 `self-reference/transaction-audit/<run_id>.json`，只保存脱敏 projection：`run_id`、`kind`、`business_outcome`、时间、失败代码、business target 数量、目标路径的不可逆 `path_id`、`sha256_before/after` 与 manifest SHA-256。禁止正文、diff、SECRET locator、秘密值、模型 prompt 或可逆编码。

锁内固定顺序不得改变：

1. **封存终态 outcome manifest**：成功路径完成全部业务 read-back 后写 `business_outcome=committed,state=audit_pending`；失败路径先精确恢复每个 preimage/tombstone 并校验原哈希，再写 `business_outcome=rolled_back,state=audit_pending`。逐字节 read-back manifest 并计算 SHA-256
2. **生成脱敏 projection**：只从已封存 manifest 的允许字段投影，create-only 写入 `<run_id>.json`；同名文件已存在时必须内容和预期哈希一致，否则视为审计冲突
3. **验证 projection**：逐字节 read-back，验证 schema、禁止字段和 SHA-256；将 projection hash 写回 manifest 的 `audit_sha256`，再 read-back manifest
4. **处理审计失败**：任一 projection 写入、read-back、schema/hash 或最终 manifest 更新失败，设置 `state=recovery_failed,failure_scope=audit`（能写时）并保持锁。若 `business_outcome=committed`，恢复程序只修复审计，不反向回滚已经验证提交的业务；若 outcome=rolled_back，业务仍须保持精确 preimage 状态
5. **释放锁**：只有 projection 已持久且验证成功后，才写 `audit_state=durable,state=<business_outcome>`，read-back 最终 manifest，然后释放锁

`consolidation-log.md`、`rollback_log.md`、`micro-consolidation-log.md` 只是 canonical projection 的非权威人类可读视图：不得在业务事务内写入，可在锁释放后的独立派生任务中重建；视图失败不改变 canonical outcome。

### 恢复状态机

- run 启动前先扫描锁与未终态 manifest；发现 `mutating`、`validating` 或 `rollback_pending` 时，必须先恢复业务；发现 `audit_pending`、`finalizing_audit` 或 `recovery_failed` 且 `failure_scope=audit` 时，只修复/验证脱敏 audit projection
- 对 `existed:true` 目标从已验证 preimage 恢复并逐文件 read-back 校验 `sha256_before`
- 对 `existed:false` 目标按 tombstone 删除本 run 新建文件；只处理 manifest 明确列出的路径
- 全 business write-set 恢复并验证后进入 `audit_pending`，按 canonical audit 固定顺序持久化 rolled_back projection；audit durable 后才写 `rolled_back` 并释放锁
- 任一业务目标无法恢复时写 `recovery_failed,failure_scope=business`；任一审计步骤失败时写 `recovery_failed,failure_scope=audit`。两者都保留锁和控制面证据，停止所有新巩固

### 标准化大巩固阶段

```text
阶段0 事务守卫：恢复检查 -> 获取锁 -> 唯一 run-id -> 冻结 write-set -> 全量 preimage/hash -> .complete
阶段1 事实巩固：扫描、证据门控（DPM 启用时）、评分、更新索引与日志
阶段1.5 深度提炼：仅 DPM 启用时执行，所有目标必须已在 write-set
阶段2 自我生长：更新 growth-journal/user-profile/relationship/diary；SOUL.md 不写
阶段3 全量校验：逐文件 read-back/hash + 容量/格式/身份不变量 -> commit 或整组 rollback -> canonical audit durable -> release lock
```

### 保留策略

- 仅对终态为 `committed` 或 `rolled_back`、`audit_state=durable` 且不处于恢复中的事务执行清理
- 保留最近 3 次事务 + 每月 1 号归档；普通快照永不包含秘密值
- canonical audit projection 独立于可清理 preimage 保留；清理本身必须在无活动巩固 run 时执行，并以新的 control-plane audit 记录被清理的 run-id，不得删除仍可能用于恢复的事务
