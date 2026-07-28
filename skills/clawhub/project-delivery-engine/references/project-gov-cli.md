# project-gov 命令行工具

`project-gov` 负责项目文件机械检查、编号、启动语和受控写入；语义与调度裁决由主线程完成。工具返回的通过只表示机械校验通过，不表示语义完整。

所有 JSON（结构化输出）都会带 `skill_version（技能版本）`；单独保存的编译计划也绑定生成它的技能版本。

## 只读命令

```powershell
node "<skill-dir>\scripts\project-gov.mjs" inspect --root "<项目根>" --json
node "<skill-dir>\scripts\project-gov.mjs" validate --root "<项目根>" --json
node "<skill-dir>\scripts\project-gov.mjs" ids --root "<项目根>" --date YYYYMMDD --json
node "<skill-dir>\scripts\project-gov.mjs" startup --root "<项目根>" --text
node "<skill-dir>\scripts\project-gov.mjs" migrate-check --root "<项目根>" --json
node "<skill-dir>\scripts\project-gov.mjs" verify-materials --root "<项目根>" --json
```

- `inspect`：检查五件套、最小索引、体量、编号、引用、占位符、必需章节和模板规定的核心表格结构；只检查受管核心结构，不扫描项目内任意 Markdown（标记文本）表格或物理目录布局。
- `validate`：返回机械校验结果；输出必须明确语义未验证。
- `migrate-check（迁移检查）`：只读报告旧项目与当前结构版本的差异，不自动改写，也不自动生成迁移计划。输出列出 `checked（已检查）`、`not_checked（未检查）` 和覆盖范围；语义检查点格式无效、结构问题报告被截断或 Markdown 扫描不完整时返回 `indeterminate（无法确定）` 或迁移项，不得宣称项目已经最新。结果中的 `physical_layout（物理布局）` 仅浅层盘点根目录编号 Markdown 文档，供主线程判断；不递归扫描目录、不判定对错，也不影响 `up_to_date（结构是否最新）`。
- `verify-materials（核验物料）`：先验证物料索引表结构，再按其中的相对文件路径和 SHA-256（文件指纹）逐项重算；表格断裂、重复或歧义、哈希过期、文件缺失或无法机械核验时返回失败。`complete（核验完成）` 只表示索引中登记的行已核验且没有失败；空索引会返回 `indexed_count: 0（登记数量为零）` 和提醒，不能证明未登记物料完整。普通 `inspect/validate` 不读取全部物料正文，不能替代本命令。
- 结构性提醒（不阻断）：`HANDOFF.md` 缺少 `## 已证伪路线` 时，`inspect`、`validate` 和 `startup` 输出的 `warnings` 包含 `missing_handoff_falsified_routes`；仅为提醒，不影响 `ok` 判定。
- 五件套剩余空间低于 2 KiB 时，`warnings` 包含 `five_piece_remaining_below_2kib`；仅提醒，不影响 `ok` 判定。
- `ids`：生成历史、证据、物料和执行批次编号。
- `startup`：只有机械校验通过且 `HANDOFF.md` 声明检查点后变化已核对时才生成启动语；不写文件，也不验证声明是否真实。`--text` 成功时标准输出只包含可复制的启动语，状态元数据改用 `--json` 查看。

`HANDOFF.md` 必须且只能有一个 `## 语义检查点` 章节，并把它作为 `# HANDOFF.md` 标题后的第一个内容区块；两项声明必须紧随其后且各出现一次。工具会拒绝放在代码、注释、HTML（网页标记）、旧记录或其他位置的声明，也会拒绝重复、冲突、尖括号占位符、无效日历日期和非法时区。时间格式为 `YYYY-MM-DD HH:mm 时区`，时区可用 `Z`、`UTC`、`+08:00` 这类偏移量或 `Asia/Shanghai` 这类 IANA 时区名。这仍只是结构和格式检查，不代表工具理解或证明了项目语义。

三个核心索引各使用一张标准索引表；项目可以保留额外自定义列，但标准列不得重复，编号不得重复。带中文说明的明确同义表头可识别；多张都像标准索引的表会报告歧义，不会任选一张后宣称迁移完成。旧项目需要合并或保留分类旧表时，由主线程先核对记录覆盖关系，再提出受控修改，工具不会自动压平历史数据。

`verify-materials` 只核验索引中的普通项目内相对文件路径和标准 SHA-256 值；外部链接、目录、绝对路径、路径重定向、超过 256 MiB 的单文件或非标准哈希会明确列为无法核验，不会猜测或静默通过。项目外、绝对或不安全路径默认隐藏正文，只返回物料编号、索引行、路径类型和原因；同一行可机械发现多个前置问题时，`reasons（多个原因）` 一次列出，同时保留旧的 `reason（首个原因）` 字段。

## 受控写入

`propose（预演）` 生成带写前指纹的执行计划，不修改项目正文；只有预演通过时才会写入 `--out` 指定的计划文件，失败结果只输出到终端，不占用重试路径。预演成功后，位于 `.project-gov/operations` 或 `.project-gov/ops` 的本次操作文件会自动删除；其他位置的输入文件不会删除。`apply（执行）` 复核计划后写入项目内容；执行成功或失败后完整恢复时，位于 `.project-gov/plans` 的本次编译计划会自动删除。执行前拒绝、恢复不完整或清理失败时保留文件并明确报告。

`propose` 的终端和 `--json` 输出都只显示动作类型、路径、数量、体量变化、警告和错误；动作正文只保存在 `--out` 指定的编译计划中，错误详情也有长度上限，避免把整文件重复展开到日志和上下文。

```powershell
node "<skill-dir>\scripts\project-gov.mjs" propose --root "<项目根>" --plan "<operation.json>" --out "<项目根>\.project-gov\plans\<plan-id>.json" --json
node "<skill-dir>\scripts\project-gov.mjs" apply --plan "<项目根>\.project-gov\plans\<plan-id>.json" --json
```

最小操作计划：

```json
{
  "schema_version": 1,
  "plan_id": "run_YYYYMMDD_HHMMSS_topic",
  "actions": []
}
```

五种动作的最小字段：

```jsonl
{"kind":"mkdir","path":"历史记录/变更记录"}
{"kind":"write_file","path":"STATUS.md","content":"# STATUS.md\n","overwrite":true}
{"kind":"append_after","path":"TODO.md","after":"## 下一步","match":"exact","content":"- 待处理事项"}
{"kind":"replace_line_contains","path":"HANDOFF.md","contains":"- 检查点后变化：","replacement":"- 检查点后变化：已核对"}
{"kind":"replace_block_exact","path":"STATUS.md","old_block":"旧文本块\n","replacement":"新文本块\n"}
```

`append_after` 的 `match` 可用 `exact` 或 `contains`；追加和替换的锚点都必须只命中一次。

`replace_line_contains（按包含内容替换行）` 的替换文本只能是一行；多行修改必须使用 `replace_block_exact（精确替换文本块）`。后者会先统一比较 Windows/Unix 换行格式，旧文本块必须且只能精确命中一次；`replacement` 可为空字符串，用于删除该文本块。编译与执行阶段使用同一匹配规则。三种文本编辑动作都保留目标文件原有的 CRLF/LF（Windows/Unix 换行）风格。

动作只支持 `mkdir`、`write_file`、`append_after`、`replace_line_contains` 和 `replace_block_exact`。写入范围限于五件套、三个最小索引、`历史记录/`、`证据库/` 和 `项目物料/`。

`mkdir` 只用于治理根目录下的子目录，例如 `历史记录/变更记录`；不接受单独的 `历史记录`、`证据库` 或 `项目物料`。新建目录必须在同一计划中有实际写入的后代文件；已有目录不受此限制。建档时直接 `write_file` 写入三个最小索引，工具会自动创建必要的上级目录，不预建无内容空目录。

对上述治理范围进行建档、checkpoint（检查点）或交接写入时，必须按 `propose → apply` 执行。工具无法表达时必须停止并说明，不得直接修改绕过。

## 执行边界

- 路径必须留在项目根内，不得经绝对路径、父级跳转、符号链接或目录联接逃逸；即使目录联接仍指向同一项目内的其他位置，也视为路径重定向并拒绝。
- 执行前核对写前指纹；文件已变化时停止。
- `apply` 会在创建锁、备份或写文件前检查编译计划绑定的技能版本和计划结构版本；版本不同或缺失时直接拒绝并要求重新预演。随后再检查工具标识、项目根、动作和写前指纹；字段不完整或重新编译后不一致的旧计划同样必须重新预演。
- 写入使用项目锁和原子替换；失败时恢复原文件。
- 本次事务备份只服务于回滚：写入成功且机械验证通过后自动删除；失败但完整回滚成功后也自动删除；只有回滚不完整或清理失败时才保留，并在结果的 `backups_retained（保留备份）` 与 `backup_cleanup（备份清理）` 中明确报告。
- `apply` 会分开报告“项目写入结果”和“锁文件清理结果”；锁清理异常不得把已经成功提交的写入伪报成失败。
- 回滚只能处理本次创建的空目录，不得移除原有目录或用户文件。
- 五件套已超限时，写入计划必须使其变小；未超限时不得写到超过 45 KiB。

## 治理缓存盘点

`prune` 是只读盘点命令：列出 `.project-gov/plans`、`.project-gov/backups`、`.project-gov/operations` 和 `.project-gov/ops` 中超过指定天数的非符号链接直接子项，返回真实总数和有界样本，不递归展开正文，也不删除任何文件。符号链接和目录联接不会被跟随或展开。

本次操作文件、编译计划和事务备份按上文规则在流程完成后自动清理。旧缓存需要处理时，先用 `prune` 定位，再由用户明确授权单独处理；项目正文和锁文件不属于盘点范围。

```powershell
node "<skill-dir>\scripts\project-gov.mjs" prune --root "<项目根>" --older-than-days 30 --json
```
