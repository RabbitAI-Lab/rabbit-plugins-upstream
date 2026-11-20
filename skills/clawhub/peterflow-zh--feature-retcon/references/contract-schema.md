# 追平契约与恢复协议

本文件是契约生命周期、机械状态和恢复规则的单一事实来源。

## 目录

- [生命周期](#生命周期)
- [Frontmatter schema](#frontmatter-schema)
- [命令](#命令)
- [写前协议](#写前协议)
- [恢复来源](#恢复来源)
- [敏感信息](#敏感信息)
- [继续、阻塞与恢复](#继续阻塞与恢复)
- [正常关闭](#正常关闭)

## 生命周期

每个权威根同时只允许一份 `RECONCILIATION.md`：

```text
评估（无文件）
  → 用户确认
  → executing
  → paused ↔ executing（同一轮次分段推进）
  → blocked ↔ executing
  → restoring → restored → 复验恢复证据 → ready_to_close
  → 或 executing → 复验完成证据 → ready_to_close
  → close 重新核验并删除契约
```

主题根的 `RECONCILIATION.md` 存在表示有活动轮次。`close` 将已校验内容保存为私有 JSON 恢复包，再删除活动契约；恢复包是静态资料，不参与活动轮次发现，不维护任务进度。不能仅凭恢复包存在断言关闭成功，需以脚本结果及活动契约是否仍在核对。

已关闭轮次在当前明确撤销授权下，可从恢复包重开为 `restoring`，保留原 round_id 和日志，再执行恢复与基线复验。已恢复的结果不能再作为新的撤销来源。

## Frontmatter schema

固定字段：

| 字段 | 含义 |
|---|---|
| `schema_version` | 契约结构版本，当前为整数 `1`；新增关闭字段向后兼容读取和恢复 |
| `round_id` | 本轮唯一标识 |
| `status` | `executing`、`paused`、`blocked`、`restoring`、`restored`、`ready_to_close` |
| `authority_root` | 权威根绝对路径 |
| `target_stage` | 本次执行上限：`requirements`、`design`、`tasks`、`implementation`、`validation` |
| `completion_stage` | 整轮闭环终点，不浅于执行上限；缺失或 `null` 时允许读取和恢复，但禁止正常关闭 |
| `created_at` | 契约创建时间 |
| `confirmed_at` | 用户执行确认时间 |
| `version_control` | `git` 或 `none` |
| `baseline_ref` | 可选的不可变 Git commit SHA；未选择 Git 恢复来源时为 `null`，包括 Git 已初始化但无 HEAD 的情况 |

正文必须保留模板中的全部章节。机器日志位于固定标记之间，人工编辑不得改变标记、JSON 结构或日志项。

## 命令

从已安装 Skill 的目录运行：

```bash
python3 scripts/contract.py init <authority-root> \
  --target-stage <stage> \
  --completion-stage <stage> \
  --version-control <git|none> \
  [--baseline-ref <ref>] \
  --writable-root <root>

python3 scripts/contract.py prepare <contract> --path <file> \
  [--recovery-mode <embed|git>] \
  [--allow-sensitive] [--allow-large]

python3 scripts/contract.py applied <contract> --path <file>
python3 scripts/contract.py status <contract> [--set <executing|paused|blocked|restoring>]
python3 scripts/contract.py scope <contract> --target-stage <stage> \
  [--completion-stage <stage>] [--writable-root <root>] --confirmation <用户确认原文或定位>
python3 scripts/contract.py restore <contract>
python3 scripts/contract.py verify <contract>
python3 scripts/contract.py verify <contract> --mark-ready --evidence <closing-evidence.json>
python3 scripts/contract.py close <contract> --archive <recovery.json>
python3 scripts/contract.py inspect-recovery <recovery.json>
python3 scripts/contract.py reopen <recovery.json> --confirmation <本次撤销授权> --writable-root <root>
```

`--allow-sensitive`、`--allow-large` 和 `recovery-mode=git` 只能反映契约中已经记录的用户选择，命令行开关本身不构成授权。

`scope` 只记录已有确认，不产生授权。它保留 `round_id`、基线和全部恢复日志；暂停的契约还需显式恢复 `executing`。闭环终点不能降低；新可写根重新确认后用可重复的 `--writable-root` 追加，不能移除有恢复日志的原根。

## 写前协议

对每次文件修改、创建或删除执行：

1. `prepare` 校验路径位于已确认可写根内。
2. `prepare` 检测符号链接、敏感候选和载荷大小。
3. `prepare` 先把原始哈希、模式和恢复来源写入契约。
4. 修改目标文件。
5. `applied` 重新检测修改后内容，再记录新哈希、模式和反向差异。
6. `verify` 检查当前文件与日志链一致。

同一文件可多次变更，每次生成独立日志项。恢复前必须先校验全部日志结构，并将每个目标重新解析到已确认可写根内；任一路径非法时，不得开始文件恢复。恢复时按日志逆序执行，任何外部漂移都会把契约置为 `blocked`。

写前登记会先核对已有日志与当前内容，防止把用户后续修改悄悄吸收为本轮新基线。恢复前校验全部日志和载荷，并模拟整轮逆序恢复；已知漂移会在任何目标文件恢复之前被拒绝。控制状态可记为 blocked，但不能因此覆盖目标。

恢复脚本在每次目标写入前持久化 `restore_pending`，完成后与 restored 状态一起清除。只有确有该中断记录时，重试才允许把精确前态识别为已恢复；首次恢复、关闭后的 reopen 以及尚未写入目标的重开，都严格核对末次写后态。用户后来把内容改回某个中间版本，也属于漂移，不能当作恢复重试。

没有恢复意图记录的旧日志不能仅凭“内容等于某次前态”推断发生过恢复。若在 `prepare` 后发生写入却没有 `applied`，同样先核对操作与内容归属，不捏造记录强行恢复。

脚本只处理常规文件，不跟随符号链接，不递归快照目录。目录结构调整必须拆成可逆的文件创建与删除，并在删除清单中明确列出。

撤销文件迁移时，`restore` 在改动任何文件前核对原父目录，在授权根内按 0700 补建缺失目录。若所需目录已被文件占用，处理冲突后再重试。恢复的文件沿用日志登记的权限。

## 恢复来源

默认 `embed`：把原始字节 gzip 压缩后 Base64 编码存入契约，能够在无 Git 时精确恢复。Base64 不是加密。

选择 `git` 时，`init` 先把已有引用解析为不可变 commit SHA；日志只保存仓库、该 SHA 和相对路径。`prepare` 还会证明当前字节与冻结基线完全一致。没有 HEAD、未登记 Git 基线或当前内容有修改时，使用 `embed` 保存真实前态，不创建基线提交。即使 `HEAD`、分支或标签随后移动，已有冻结引用也不改变。要长期保留且能在没有该 Git 对象时恢复，优先使用默认 embed。

估算后的嵌入载荷超过 10 MiB 时暂停，让用户选择：

- 明确确认后使用 `--allow-large` 嵌入。
- 在内容与 Git 引用一致时改用 `--recovery-mode git`。
- 缩小本轮范围。

## 敏感信息

契约权限始终为 `0600`。脚本只输出敏感信号名称和路径，不输出命中值；敏感日志的可读差异被省略，但精确恢复载荷仍可能含秘密。

检测到敏感候选时默认停止。用户逐文件确认本地载荷风险后，才可使用 `--allow-sensitive`。若敏感信号首次出现在修改后内容中，`applied` 会省略差异、保存哈希并把契约置为 `blocked`，等待用户确认。用户拒绝时，将该文件移出可写范围并由用户处理或恢复本次修改。

`init` 会核对声明的 `version_control` 与权威根实际状态。有 Git 时，`verify` 检测契约是否进入索引；被跟踪或暂存即阻塞。Git 不可读不能静默当成没有仓库。恢复包也保持 `0600`，不写入已跟踪或暂存路径；选择明确的本地资料位置，不能自动修改 `.gitignore`、`.git/info/exclude`、索引或提交历史。恢复包可能含原始敏感内容，压缩和 Base64 不是加密。

## 继续、阻塞与恢复

继续未完成轮次前运行 `status` 和 `verify`，阅读契约中的变更断言、进度和阻塞。只有解决阻塞或重新确认边界后，才把状态从 `blocked` 改回 `executing`。

阶段性暂停、交接或等待下一次授权时，将状态设为 `paused`，记录完成水位、剩余工作和下次所需授权。保留契约，不运行恢复，不创建替代轮次。

只有用户明确要求撤销本轮修改时：

1. 运行 `restore`，让脚本逆序恢复。
2. 运行 `verify`，确认日志链与前态一致。
3. 重新运行基线验证，检查活跃引用没有停在中间状态。
4. 确认契约没有尚未恢复的独有要求。
5. 提供 `outcome=restored` 的关闭证据，运行 `verify --mark-ready --evidence` 和带新恢复包路径的 `close`。

`restore` 完成后状态为 `restored`，仅代表文件已恢复；它不能证明验证基线和引用已经复验。

漂移、缺失 Git 对象、损坏载荷或基线验证失败都保持阻塞，不得通过删除契约绕过。

## 正常关闭

`verify` 的 `valid` 仅表示 schema、日志链、文件哈希、权限和 Git 状态一致。正常关闭要求执行上限已达到闭环终点、状态为 `executing`、独立关闭证据属于同一轮次且没有剩余工作。`blocked` 必须先解决阻塞；`paused` 不能关闭。Skill 逐项证明：

- 断言已吸收。
- 闭环终点及全部上游阶段门槛通过，必要检查没有 NotRun 或未解释失败。
- 零未解释残留。
- 水位已更新。
- 契约未被 Git 跟踪。
- 契约没有独有有效要求。

按 [关闭证据](closure-evidence.md) 提供证据后运行 `verify --mark-ready --evidence`。脚本登记契约指纹和证据哈希；`close --archive` 重新检查当前文件、契约和证据，保存恢复包并再次核对，之后才删除活动契约。两个命令分开执行，任一失败保留现场，不用 `rm`、`unlink` 或补丁绕过。状态查询不是关闭许可。

恢复包路径须在已授权根内，父目录已经存在，不能占用目标文件或已有不同内容。新包以不覆盖方式原子创建；文件系统不支持时返回失败，保留活动契约，不降级为覆盖写入。同一内容的已写包允许用于中断后的重试。正常完成和撤销完成分别保存恢复包，撤销后保留原完成包。

登记的授权根和目标路径不随符号链接改向重新解释；目录位置改变时停止。Git 查询失败不是“未被跟踪”，校验必须报错。关闭最终复核必须仍对应归档的同一份契约摘要，不能因为另一份新状态也达到 close_ready 就删除它。

执行期间仍保持单写者并停止有关后台写入。上述预检与不覆盖创建不构成任意并发下的文件系统事务隔离，也不阻止绕开脚本的直接编辑。

完整关闭后需要撤销时：

1. `inspect-recovery` 只读核对轮次、权威根及目标路径，不输出恢复载荷；核对当前用户确实要求撤销这一轮。
2. 使用本次明确授权的工作根调用 `reopen`。脚本校验包及日志，预检目标漂移和范围，拒绝覆盖任何活动契约；此命令只重建恢复控制记录，不改目标文件。
3. 执行 `restore`，重新校验当前现场后逆序恢复。恢复包并不授权覆盖后续修改，也不自动迁移绝对路径。
4. 实际复验基线和引用，准备 restored 证据，以新的归档路径关闭。不能把文件恢复成功当成业务验证成功。

`verify` 在机械一致性或关闭证据失效时返回非零退出码；机械有效但尚未达到关闭条件时可返回 0，同时 `close_ready: false`。执行者必须区分这两个字段，不能只看退出码决定功能完成。

旧契约缺少 `completion_stage` 时，依据原始确认用 `scope` 补齐，不猜测、更不删除重建。旧版 `ready_to_close` 没有证据登记时不能关闭：尚未恢复的轮次先转回 `executing`，补齐终点和证据；需要恢复的轮次转为 `restoring` 后继续 `restore`。保留旧恢复日志。

脚本检查结构、证据存在性和漂移，不能证明自然语言结论真实，也不能阻止绕过脚本直接删除文件。Agent 仍须阅读逐项证据，完成整个闭环复核。
