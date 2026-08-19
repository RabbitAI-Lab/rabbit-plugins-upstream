# JYS 工作区、状态与默认续接契约

本文件是 `jys` 与 `jys-s1` 至 `jys-s5` 的共同执行契约。主控或任一子 Skill 开始工作前都必须读取本文件；子 Skill 不得只凭历史消息推断项目路径或下一步骤。

## 1. 路径绑定

- `JYS_PROJECT_ROOT`：用户明确指定的项目根目录；未指定时，只能使用当前唯一的 Codex 工作区或仓库根目录。
- `JYS_WORKSPACE`：固定为 `JYS_PROJECT_ROOT/jys-workspace`。
- 同一项目跨任务继续使用同一个 `JYS_WORKSPACE`。新建 Codex 任务不等于新建 JYS 项目。
- 路径不唯一、不可写或用户声明新项目但目录已有 `status.md` 时，必须询问路径；除此之外不要重复询问项目位置。
- 不得搜索、读取或写入其他项目的 `jys-workspace`。

## 2. 状态文件是唯一续接来源

每轮开始先读取 `JYS_WORKSPACE/status.md`，每轮结束再更新。状态文件 YAML frontmatter 中以下字段是路由真源：

```yaml
schema_version: 2
current_stage: S1
current_skill: jys-s1
next_skill: jys-s1
next_action: 等待用户确认套路内核和变体
waiting_for: 套路内核和变体选择
s1: in_progress
s2: not_started
s3: not_started
s4_outline: not_started
s4_script: not_started
s5_delivery: not_started
final_confirmation: pending
```

允许的阶段状态只有：

- `not_started`：尚未开始。
- `in_progress`：正在处理，或正在等待本阶段必要的用户选择。
- `confirmed`：用户已经明确确认该阶段结果。

`final_confirmation` 只使用 `pending` 或 `confirmed`。

## 3. 默认下一 Skill

收到新消息时按以下顺序路由：

1. 用户明确调用 `$jys` 或 `$jys-s1` 至 `$jys-s5` 时，以明确调用为准。
2. 用户提出与当前默认步骤冲突的明确需求时，按需求和前置条件重新路由，并更新状态。
3. 用户只回复“继续”“好的”“就这样”、确认语句或普通补充时，直接调用 `next_skill`，不要再次询问是否继续。
4. 只有缺少不可替代的用户选择、事实、文件或唯一项目路径时才提问；一次只询问当前阻塞项。
5. `waiting_for` 非空时，下一轮仍使用当前 Skill 接收答案，不能提前跳到后续 Skill。

## 4. 状态转换

| 条件 | current/next Skill | 状态更新 |
|---|---|---|
| S1 正在选套路或等待确认 | `jys-s1` | `s1: in_progress` |
| S1 已确认；内核明确要求产品机制先行 | `jys-s3` | `s1: confirmed` |
| S1 已确认；普通路线 | `jys-s2` | `s1: confirmed` |
| S2 等待替换选择或骨架确认 | `jys-s2` | `s2: in_progress` |
| S2 已确认但 S3 未完成 | `jys-s3` | `s2: confirmed` |
| S3 已确认但 S2 未完成 | `jys-s2` | `s3: confirmed` |
| S2、S3 均确认 | `jys-s4` | 进入 `s4_outline` |
| S4 大纲已确认 | `jys-s4` | `s4_outline: confirmed; s4_script: in_progress` |
| S4 完整剧本已确认 | `jys-s5` | `s4_script: confirmed` |
| S5 已完整交付，等待最终反馈 | `jys-s5` | `s5_delivery: confirmed; final_confirmation: pending` |
| 用户最终确认 | 无 | `final_confirmation: confirmed` |

不得仅因文件存在就标记 `confirmed`；确认状态必须来自用户明确确认或旧状态中已有的等价记录。

## 5. 每轮回复尾注

每次 JYS 回复末尾都必须写状态尾注，但不得把它写成重复确认问题：

```text
下一步默认调用：$jys-s2
默认动作：根据已确认人物组合继续生成替换方案。你直接回复内容或“继续”即可按此推进；如需改变步骤，直接说明。
```

若正在等待选择，保持当前 Skill：

```text
下一步默认调用：$jys-s2
默认动作：接收你的人物组合选择后继续生成替换方案。
```

流程完成时：

```text
下一步默认调用：无，当前 JYS 项目已完成。
```

## 6. 旧状态兼容

- `status.md` 没有 `schema_version` 时视为 v1。
- 首次写入 v2 前备份为 `status.v1.backup.md`；已有备份不得覆盖。
- 原有 S1、S2、S3 的“是”映射为 `confirmed`，“否”映射为 `not_started`。
- 存在 `s4-workspace.md` 只能证明 S4 已开始；没有明确确认记录时写 `s4_script: in_progress`，不得自动写 `confirmed`。
- S5 和最终确认没有旧证据时分别写 `not_started`、`pending`。
- 迁移不得删除或改写原有正文内容。

## 7. 文件写入边界

- 项目状态只写入当前 `JYS_WORKSPACE`。
- 套路和产品数据库继续位于 `../jys/assets/kernels/` 与 `../jys/assets/products/`，由 S1 独占写入。
- 数据库写入前按 `db-write-guide.md` 创建单份 `.bak` 回滚副本；先完成内容文件，再原子更新索引，最后更新 `assets/library-version.json`。
- S2、S3、S4、S5 对共享数据库只读。

