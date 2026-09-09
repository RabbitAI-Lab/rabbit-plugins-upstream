# idempotent-rebuild-verification

哈希钉扎的 agent 工作区重建验证工具。当 runbook 重放后出现"某文件 sha256 不符"或
快照擦除后产物消失时，本工具**先分类、后动手**：

- `$(cat file)` 往返剥掉尾部换行 → **良性质漂移**，重跑 writer 即可（**勿盲目重贴**大 heredoc）；
- heredoc 粘贴截断 / 下载写入 HTML 错误页 / 同尺寸内容被改 → **真损坏**，需整块重贴/重下；
- runbook 里的代码步骤可能被**内嵌围栏静默截断**（CommonMark：` ```bash ` 块内再出现
  ` ``` ` 即闭合）→ 提取器按 CommonMark 规则切分并标记 suspect；
- 快照擦除后"脚本在、build/ 与模型不在"是**正常态** → 只重跑产物步骤。

**纯标准库 · 离线 · 确定性 · JSON 机器可读输出 · 每条带 next_action。只读，不修改被验证文件。**

## v2.0.0 相对 v1.0.6

v1 是纯散文（SKILL.md 约 4KB 提示词 + 一个只处理"单个尾部换行"的内联 triage 片段）。
v2 把全部规则机械化为可离线运行的确定性 CLI（`scripts/rebuild_verify.py`，约 600 行，
仅用 hashlib/re/json/os/sys 等标准库）：

| v1 的散文规则 | v2 的命令 |
|---|---|
| Rule 1（先 triage 再重贴） | `verify` —— 7 类分类 + 良性/损坏判定 + next_action |
| Rule 2（批量校验） | `manifest` —— 每行 `path sha256 [size]`，rc 0/2/3 |
| Rule 5（钉扎提取） | `pins` —— 64-hex 钉扎 + 所在标题 + 引用文件 + 围栏内外 |
| Rule 4（按行范围切步骤） | `extract-steps` —— CommonMark §4.5 正确的块切分 + heredoc 终止核查 + suspect 标记 + `--write-steps` 字节精确落盘 |
| Rule 3（擦除后重跑） | `wipe-audit` —— 脚本/产物/shim 五类扫描 + 4 态判定 + 步骤路由建议 |
| （无） | `gen-fixtures` —— 确定性测试夹具；`scripts/selftest.py` —— 12 组离线自检 |

版本统一为 2.0.0（v1 的 frontmatter 1.0.0 与发布版 1.0.6 漂移的问题不复存在）。

## 用法

```bash
# 单文件：内容 + 尺寸双钉（尺寸钉可抓出 HTML 错误页/截断下载）
python3 scripts/rebuild_verify.py verify ~/model.gguf \
  --want 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef \
  --want-size 4294967296
# => {"status":"benign","class":"trailing_newline_drift","next_action":"重跑该文件的 writer 步骤…",…}

# 批量
printf 'scripts/run.sh aaaa…\n~/model.gguf bbbb… 4294967296\n' > manifest.txt
python3 scripts/rebuild_verify.py manifest manifest.txt --root .

# runbook 钉扎清单
python3 scripts/rebuild_verify.py pins runbook.md

# 程序化步骤提取（CommonMark 正确；suspect 步骤按显式行范围人工切割）
python3 scripts/rebuild_verify.py extract-steps runbook.md --lang bash --write-steps /tmp/steps

# 快照擦除后诊断
python3 scripts/rebuild_verify.py wipe-audit .

# 确定性测试夹具
python3 scripts/rebuild_verify.py gen-fixtures /tmp/fix

# 全部自检（应 100% PASS）
python3 scripts/selftest.py
```

**退出码**：`0` 全好/ok · `2` 输入错误（stderr 单行 JSON）· `3` 漂移/缺失/脚本缺失异常。

## 漂移分类（verify 的 7+2 类）

| class | status | 根因 | next_action |
|---|---|---|---|
| `ok` | ok | — | 无 |
| `trailing_newline_drift` | benign | `$(cat f)` 剥 1..N 个尾部 `\n`（POSIX XCU） | 重跑 writer 步骤，勿盲目重贴 |
| `crlf_drift` | benign | 编辑器 CRLF 往返 | 转 LF 或按 CRLF 重新钉扎 |
| `html_error_page` | error | 下载失败写入 404/错误页 | 检查 URL/认证，重下并断言字节数 |
| `truncated_paste` | error | heredoc 粘贴中断/下载截断 | 删除后整块重贴/重下 |
| `content_change` | error | 同尺寸内容被改 | 与新鲜写出 diff |
| `unknown` | warn | 尺寸不同且无良性解释 | 与新鲜写出 diff |
| `size_ok` / `size_mismatch` | warn | 仅尺寸钉扎 | 按 got_sha256 补内容钉 / 重下 |

## 文件

```
SKILL.md                  # 加载地图 + 命令契约 + 硬规则 + 边界
README.md                 # 本文件
CHANGELOG.md              # 版本记录
scripts/rebuild_verify.py # 全部工具（纯标准库，约 600 行）
scripts/selftest.py       # 12 组离线自检
references/
  drift_classes.md        # 漂移分类语义与根因
  runbook_extraction.md   # CommonMark 块切分与 suspect 判定
  snapshot_semantics.md   # 快照排除清单与擦除后判定
```

## 已知边界

- `html_error_page` 的关键词分支要求文件含 `< >` 标签上下文；纯文本 404 页落入
  `truncated_paste`/`unknown`（next_action 仍指向重下/核对）。
- `extract-steps` 不识别管道链/命令链里的 heredoc（有意保守降级 → 人工核对）。
- `wipe-audit` 排除目录清单按环境文档校准：默认 `SNAPSHOT_EXCLUDED` 常量，可用环境变量
  `RV_SNAPSHOT_EXCLUDED`（空白/逗号/分号/冒号分隔）覆盖，跨环境先核对。
- 不执行 runbook 步骤；不做二进制语义校验（只校验字节完整性）。
- 自研 CLI 的语义自检基于 CommonMark §4.5 与 POSIX XCU 的规范文本（2026-09-06 核对），
  未对照真实 CommonMark 规范测试套件逐例验证。

## 发布完整性

- TREE-SHA256-v1（发布包 8 个文件，排除 README.md 以破 hash-in-file 循环）：
  `2909f8dd71acc16f830f8fa8b8700c42d92f07731e7967dd5d57a04a336fbd2f`
  （重算方式见仓库 `tools/upload_user_output.sh` 同套 hash 函数；README 只记录值。）
