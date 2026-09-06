---
name: idempotent-rebuild-verification
version: 2.0.0
description: >
  哈希钉扎的 agent 工作区重建验证：纯标准库、离线、确定性 CLI。分类"良性质漂移 vs 真损坏"
  （$(cat) 尾部换行剥离 / CRLF / 截断粘贴 / HTML 错误页 / 同尺寸改动），批量清单校验，
  runbook 钉扎提取，CommonMark 正确的步骤提取（内嵌围栏不再静默截断），快照擦除后
  状态判定与步骤路由。JSON 机器可读输出，每条带 next_action。不修改任何被验证文件。
author: orionshaowswmw
license: MIT
tags: [rebuild, idempotency, sha256, sandbox, snapshot, agent-workspace, verification]
metadata: {"openclaw": {"emoji": "🔁"}}
---

# idempotent-rebuild-verification v2.0.0

**一句话**：runbook 重建/快照擦除后出现"哈希不符/产物消失"时，先用本工具分类
（良性=重跑 writer；损坏=整块重贴/重下），再动手 —— 盲目重贴大 heredoc 本身就会制造损坏。

## 何时使用

- 重放哈希钉扎的 runbook 后，某个 `sha256 must be:` 不符 → `verify` 先分类。
- 一批钉扎文件 → `manifest` 批量校验（每行 `path sha256 [size]`）。
- 想知道 runbook 里钉了哪些文件 → `pins`。
- 要从 markdown runbook 程序化执行步骤 → `extract-steps`（suspect 步骤按显式行范围切割）。
- 快照擦除后判断"哪些步骤要重跑" → `wipe-audit`。
- 需要确定性测试夹具 → `gen-fixtures`。

## 加载地图（token 经济）

| 场景 | 读什么 |
|---|---|
| 直接用工具 | 本文 + `python3 scripts/rebuild_verify.py --help` |
| 追问某类漂移的根因/处置 | `references/drift_classes.md` |
| 步骤提取/内嵌围栏疑问 | `references/runbook_extraction.md` |
| 快照排除清单/擦除后判定 | `references/snapshot_semantics.md` |

## 命令契约

```bash
python3 scripts/rebuild_verify.py verify FILE --want HEX [--want-size N]
python3 scripts/rebuild_verify.py manifest MANIFEST [--root DIR]
python3 scripts/rebuild_verify.py pins RUNBOOK.md
python3 scripts/rebuild_verify.py extract-steps RUNBOOK.md [--lang bash|sh|shell|python|text|all] [--write-steps DIR]
python3 scripts/rebuild_verify.py wipe-audit DIR
python3 scripts/rebuild_verify.py gen-fixtures DIR
python3 scripts/selftest.py                # 全部自检（应 100% PASS）
```

| 命令 | 输出（stdout 单行 JSON） | 退出码 |
|---|---|---|
| verify | `{status: ok/benign/warn/error, class, next_action, detail{size,got_sha256,want_sha256,…}}` | 0 ok · 2 输入错 · 3 漂移/不符 |
| manifest | `{total, n_ok, n_drifted, n_missing, ok[], drifted[{rel,class,next_action}], missing[]}` | 0 全 ok · 2 · 3 |
| pins | `{n_pins, pins[{line,sha256,heading,referenced_file,in_code_fence,raw}]}` | 0 · 2 |
| extract-steps | `{n_steps, suspect[], steps[{index,lang,start_line,end_line,bytes,heredocs,status,sha256}]}`；行号=内容行（开栏=start_line-1，闭合围栏=end_line+1）；`--lang` 精确匹配（未标注块计 text）；`--write-steps` 额外写字节精确步骤+steps.json | 0 · 2 |
| wipe-audit | `{verdict: clean/normal_post_wipe/pre_wipe_or_full/scripts_missing_too, next_action, next_actions[], present{…}}` | 0 · 2 · 3(脚本缺失异常) |
| gen-fixtures | 确定性夹具（canonical 1116B + 7 种漂移形态 + manifest + 6 步 runbook） | 0 · 2 |

**漂移分类 class 全集**：`ok` `trailing_newline_drift`(benign) `crlf_drift`(benign)
`html_error_page` `truncated_paste` `content_change` `unknown` `size_ok` `size_mismatch`。
**值类型**：数字=JSON number；哈希=64 位小写 hex 字符串；行号=1-based int。
**错误**：stderr 单行 JSON `{"status":"error","tool":…,"error":…}`。

## 硬规则（不可违反）

1. **先分类，后动手**：任何"哈希不符"先跑 `verify`；`benign` → 重跑 *writer* 步骤，
   **勿盲目重贴** heredoc（重贴本身是损坏源）；`error` 类才按 next_action 重贴/重下。
2. **只读**：verify/manifest/pins/extract-steps/wipe-audit 绝不修改被验证文件；
   写盘只发生在 `--write-steps DIR` 与 `gen-fixtures DIR` 显式指定处。
3. **不联网**：所有命令离线。
4. **确定性**：gen-fixtures 与 steps.json 的 sha256 相同输入→相同字节（无时间戳/随机）；
   清单/钉扎校验结果可复现。
5. **suspect 步骤不自动执行**：extract-steps 标记 suspect（未闭合/内嵌围栏切断 heredoc）
   的步骤必须按显式行范围人工切割后确认 EOF 标签再执行。
6. **判定边界**：wipe-audit 的排除目录清单默认 `SNAPSHOT_EXCLUDED` 常量，可用环境变量
   `RV_SNAPSHOT_EXCLUDED`（空白/逗号/分号/冒号分隔）按所在环境文档覆盖；
   它给出的是"要重跑哪类步骤"的建议，不是重建执行器。

## 自检

`python3 scripts/selftest.py`：12 组检查（夹具确定性、提取器字节精确、7+ 分类逐一、
manifest/pins/wipe-audit 语义、退出码纪律、CRLF/空文件/多尾换行边界、仅标准库、
SKILL 幻影扫描、JSON 契约）。任何 FAIL 先修工具再交付。

## 边界外（明确不做）

- 不执行 runbook 步骤（只提取/校验/分类）。
- 不做增量/全量 diff 报告（同尺寸改动请对新鲜写出做 `diff`）。
- 不处理非文本二进制语义（图像/模型内容正确性不校验，只校验字节完整性）。
- 快照排除清单是环境相关的，跨环境使用先核对 `references/snapshot_semantics.md`。
