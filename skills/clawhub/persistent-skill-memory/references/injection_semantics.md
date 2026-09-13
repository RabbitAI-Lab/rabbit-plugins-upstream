# injection_semantics.md — 标记块注入语义（供参考）

实现：`scripts/skill_memory.py::inject_block`（行级处理，字节周边保留）。

## 块布局
```
<<<SKILL_INDEX_BEGIN>>>
[domain-a]
name1
name2
[domain-b]
name3
<<<SKILL_INDEX_END>>>
```
- 每**非空**域一个头行 `[domain]`，其下列出该域全部名字，**每行一个名字**（域内字典升序）。
- **为什么不用逗号拼接**：名字来自 SKILL.md frontmatter，可含逗号（如 `quotey, special`）；逗号拼接无法往返（verify 会把一个名字拆成两个）。行格式下唯一约束：名字不得恰为 `[小写-连字符]` 形态（与域头模式 `^\[[a-z][a-z0-9-]*\]$` 冲突）——frontmatter 名字行本就不含换行，其余字符安全。
- 域顺序 = 固定优先级序（`categorization.md`）。
- **不截断**、无 description、无计数——紧凑性即 token 预算（见 `stats` 的 `prompt_block_bytes`）。
- 块尾恒带换行；注入前保证与文件尾之间恰好一个空行。

## inject 状态机
| prompt 文件现状 | 动作 | 输出 status | 退出码 |
| --- | --- | --- | --- |
| 无 BEGIN/END | 追加到文件尾 | `appended` | 0 |
| 恰好一对、BEGIN 在 END 前、标记各独占一行 | **仅替换内部**，标记外字节不动 | `replaced`（内容相同则 `unchanged`） | 0 |
| 半开 / 多对 / 倒序 / 标记未独占行 | **不改文件** | `marker_error` | **2** |
| 文件不存在 | **不创建** | — | **2** |

## 工作示例（状态判定）
- 对**从未注入过**的 prompt 文件首次 `inject` → `appended`（文件里原本没有标记对）。
- 文件已含标记对（哪怕内部是旧内容/空块）→ 走**替换**路径：内容不同 = `replaced`，
  内容恰好相同 = `unchanged`。**"已有标记" ≠ appended**。
- 例：文件 `A\n<<<SKILL_INDEX_BEGIN>>>\nold\n<<<SKILL_INDEX_END>>>\nB\n` + 1 个 general 域技能 x-tool
  → status `replaced`，最终字节：
  ```
  A
  <<<SKILL_INDEX_BEGIN>>>
  [general]
  x-tool
  <<<SKILL_INDEX_END>>>
  B
  ```

## 不变式（selftest G6/G7 覆盖）
1. **幂等**：同输入双注入 → 文件字节恒等。
2. **不重复**：任何路径下标记对至多一对（v1 失败模式：重复注入堆出多份索引）。
3. **不自动修复**：标记异常一律人工修（自动补全/清理会吞掉标记外内容；多模型 spec 评审一致结论）。
4. **行尾策略**：周边字节原样保留（含原 CRLF）；注入块自身用 `\n`。
5. **哨兵**：标记块之前的所有字节（系统提示主体）永不被改写。

## verify 语义
- 解析标记块内部：匹配域头模式 `^\[[a-z][a-z0-9-]*\]$` 的行忽略；其余非空行 = 名字（strip 后入集合）。
- `missing` = **在磁盘但不在 prompt**（新装未注入）；`stale` = **在 prompt 但不在磁盘**（已删/假名）。
- 两者皆空 → rc0 `{ok:true}`；任一非空 → rc3 `{ok:false, missing, stale}`（两者可同时存在）；无标记块/多对 → rc2。
- 自愈路径：`verify` rc3 → 重跑 `inject` → `verify` rc0（selftest G7 验证）。

## 典型用法（`hook` 生成的包装器语义）
```bash
./skill_add.sh /path/to/installer.sh [args...]
# 模板（set -euo pipefail）：
#   "$@"                                        # 1) 原始安装命令，参数透传
#   python3 skill_memory.py index   --root R    # 2) 重索引（stdout JSON）
#   python3 skill_memory.py inject  --root R --prompt-file P   # 3) 幂等注入
#   python3 skill_memory.py verify  --root R --prompt-file P   # 4) 对账
# 语义：installer 失败 → set -e 透传其退出码，不重索引（避免污染 prompt）
#       verify 漂移   → 包装器退出码 3，调用方据此告警
```
