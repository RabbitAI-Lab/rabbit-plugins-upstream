---
slug: cron-guard
name: cron-guard
version: "1.0.0"
displayName: 定时守护
summary: cron 作业可靠性护栏，脚本优先、确定环境、静默成功，跨平台故障模式一网打尽。
license: MIT
description: |-
  定时守护为无人值守的 cron 作业与后台任务提供可靠性护栏。它把"在 cron 里跑一行 bash"的高危模式，改造为"脚本优先、环境确定、静默成功"的工程化模式，覆盖 shell 引用陷阱、命令替换意外、cwd/env 漂移、SIGPIPE 误报、git 推送冲突等高频故障。

  核心能力：脚本优先原则、确定环境（cwd/env 文档化）、静默成功约定（NO_REPLY）、故障模式目录与修复模板、跨平台适配（POSIX + Windows/PowerShell）、cron 作业预检清单、加固头部模板。

  适用场景：cron 作业加固、后台任务可靠性提升、无人值守脚本编写、CI 定时任务、Agent 长驻守护脚本、跨平台定时作业。

  差异化：相比原始仅 POSIX 聚焦的方案，本技能新增 Windows/PowerShell 等效模式（覆盖三大平台）、结构化故障模式目录（症状→原因→修复模板）、可粘贴的加固头部、作业上线前预检清单、以及与定时调度专家/定时大师的分层协作说明。从"经验零散"升级为"检查清单驱动"。

  触发关键词：定时守护, cron 加固, 脚本可靠性, shell 陷阱, 静默成功, guardrails, hardening, worker, reliability, cron, shell
tags:
- 自动化
- 定时调度
- 可靠性工程
tools:
- read
- exec
---

# 定时守护

cron 作业的失败很少是"逻辑 bug"，多半是 shell 引用炸了、环境漂移了、管道误报了。本技能用"脚本优先 + 确定环境 + 静默成功"三原则，把这些无聊但致命的坑堵死。

## 分层定位

| 层级 | 技能 | 职责 |
|:-----|:-----|:-----|
| 守护层 | **定时守护（本技能）** | 脚本可靠性、shell 陷阱、跨平台加固 |
| 精通层 | 定时大师 | heartbeat/cron 决策、推送策略 |
| 易用层 | 定时助手 | 自然语言、模板、成本优化 |
| 引擎层 | 定时调度专家 | 时区、并发、自清理、熔断 |

本技能管"被调度的脚本怎么写得可靠"，引擎管"调度本身怎么可靠"。

## 三大原则

### 原则 1：脚本优先

**禁止**在 cron 里写多行 `bash -lc '...'`。把逻辑放进仓库脚本，cron 只跑一行短命令。

```bash
# 错误：cron 里塞多行 shell（引用地狱）
bash -lc 'cd /app && for f in *.csv; do python3 process.py "$f" && mv "$f" done/; done'

# 正确：cron 跑一个脚本
python3 tools/process_all.py
```

### 原则 2：确定环境

cron 执行环境的 `cwd`、`PATH`、环境变量与交互式 shell 不同。必须显式确定：

```bash
# 脚本开头确定 cwd
cd "$(dirname "$0")/.." || exit 1

# 文档化所需环境变量
: "${API_KEY:?API_KEY 未设置}"
: "${DATA_DIR:?DATA_DIR 未设置}"
```

### 原则 3：静默成功

成功时**不输出任何内容**（或只输出 `NO_REPLY`），只在失败时告警。避免每次成功都发通知淹没用户。

```bash
# NO_REPLY 约定
if do_work; then
  echo "NO_REPLY"   # 静默成功
  exit 0
else
  echo "ALERT: 任务失败 - $(date)" >&2
  exit 1
fi
```

若运行时不支持 `NO_REPLY`，理解为"成功时打印空"。

## 快速开始：4 步加固

1. **逻辑进脚本**：把 cron 命令的逻辑移到 `tools/<job>.py` 或 `tools/<job>.sh`。
2. **cron 只跑一行**：`python3 tools/<job>.py`（不要多行 `bash -lc`）。
3. **确定 cwd/env**：脚本内 `cd` 到仓库，文档化环境变量。
4. **静默成功**：成功打印空/`NO_REPLY`，失败才告警。

## 加固头部模板（可直接粘贴）

在 cron 任务说明或脚本开头加入这两行：

```text
加固要求（必须）：遵循脚本优先、确定 cwd、静默成功原则。
多步/解析逻辑写入 tools/*.py 脚本，cron 只跑一行短命令。
```

## 跨平台适配

原始方案仅覆盖 POSIX（bash/sh）。本技能补充 Windows/PowerShell 等效模式：

| 原则 | POSIX (bash/sh) | Windows (PowerShell) |
|:-----|:----------------|:---------------------|
| 脚本优先 | `python3 tools/job.py` | `python tools\job.py` |
| 确定 cwd | `cd "$(dirname "$0")/.."` | `Set-Location $PSScriptRoot\..` |
| 必需变量 | `: "${VAR:?未设置}"` | `if (-not $env:VAR) { throw "VAR 未设置" }` |
| 静默成功 | `echo "NO_REPLY"` | `Write-Output "NO_REPLY"`（或无输出） |
| 错误退出 | `set -euo pipefail` | `$ErrorActionPreference = "Stop"` |
| 错误告警 | `echo "ALERT" >&2` | `Write-Error "ALERT"` |

**可移植性铁律**：不要硬编码某台机器的绝对路径。优先用仓库相对路径、文档化的环境变量、最小化的 `cd` 包装。

## 故障模式目录（核心差异化）

### 模式 1：`unexpected EOF while looking for matching ')'`

**症状**：cron 报语法错误，找不到匹配括号。

**原因**：
- `$(...)` 命令替换未闭合
- `bash -lc '...'` 嵌套引号断裂

**修复模板**：把整段多行 shell 替换为脚本，cron 只跑 `python3 tools/<job>.py`。

### 模式 2：`pipefail` + `head` 导致 SIGPIPE 误报

**症状**：命令明明输出正常，却以非零退出码失败。

**原因**：`set -o pipefail` 下，`head` 提前关闭管道，上游收到 SIGPIPE 被视为错误。

```bash
# 错误：pipefail + head 误报
set -euo pipefail
cat bigfile.log | head -10   # head 读够关闭管道 → cat 报 SIGPIPE → 整体失败
```

**修复模板**：
```bash
# 方案 A：去掉 pipefail（仅此场景）
set -euo pipefail
cat bigfile.log | head -10 || true

# 方案 B（推荐）：在脚本里只读需要的部分
python3 -c "
with open('bigfile.log') as f:
    for i, line in enumerate(f):
        if i >= 10: break
        print(line, end='')
"
```

### 模式 3："本地能跑，cron 里失败"

**症状**：交互式 shell 正常，cron 里报 command not found 或路径错误。

**原因**：
- cwd 不同（cron 默认 HOME，非仓库目录）
- PATH 不同（cron 不加载 `.bashrc`/`.zshrc`）
- 环境变量缺失

**修复模板**：
```bash
#!/usr/bin/env bash
set -euo pipefail
# 确定 cwd
cd "$(dirname "$0")/.." || exit 1
# 显式 PATH（cron 的 PATH 很精简）
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin"
# 文档化必需变量
: "${API_KEY:?API_KEY 未设置}"
# ... 实际逻辑 ...
```

### 模式 4：`git push` 被拒（non-fast-forward）

**症状**：`! [rejected] ... (non-fast-forward)`，自动化向长期分支推送失败。

**保守修复**（不用 force-push）：
```bash
# 被拒后：fetch 远程，把本地新提交移植上去，重试一次
if ! git push origin feature-branch; then
  git fetch origin feature-branch
  git rebase origin/feature-branch   # 或 cherry-pick
  git push origin feature-branch
fi
```

**铁律**：自动化脚本**禁止** `git push --force`，会覆盖他人提交。

### 模式 5：Python `-c` 单行引号陷阱

**症状**：`python3 -c "..."` 在 cron 里引号错乱。

**原因**：双引号内的 `$`、`"` 被 shell 解释。

**修复模板**：把 `-c` 内容写成脚本文件，cron 跑 `python3 tools/job.py`。

### 模式 6：Windows 路径与反斜杠

**症状**：PowerShell 脚本路径解析错误。

**原因**：反斜杠被转义，或路径含空格未加引号。

**修复模板**：
```powershell
# 用单引号字面路径，避免变量插值
Set-Location 'C:\Program Files\App'
# 或用 $PSScriptRoot 相对路径
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
```

### 模式 7：临时文件残留

**症状**：脚本中断后临时文件未清理，下次运行冲突。

**修复模板**：
```bash
# trap 确保退出时清理
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
# ... 使用 $TMPFILE ...
```

```powershell
# PowerShell 等效
$tmp = New-TemporaryFile
try {
  # 使用 $tmp
} finally {
  Remove-Item $tmp -ErrorAction SilentlyContinue
}
```

### 模式 8：并发执行冲突

**症状**：周期任务未跑完下一轮就启动，数据冲突。

**修复模板**：文件锁防并发：
```bash
LOCKFILE="/tmp/job.lock"
exec 200>"$LOCKFILE"
if ! flock -n 200; then
  echo "NO_REPLY"  # 上一轮还在跑，静默跳过
  exit 0
fi
# ... 实际逻辑 ...
```

## 上线前预检清单

把 cron 作业上线前过一遍这个清单：

```markdown
## cron 作业上线预检
- [ ] 逻辑在脚本文件中，cron 只跑一行命令
- [ ] 脚本开头确定 cwd（cd 到仓库）
- [ ] 所需环境变量已文档化并校验
- [ ] PATH 已显式设置（不依赖 .bashrc）
- [ ] 成功时静默（NO_REPLY 或无输出）
- [ ] 失败时输出简短告警到 stderr
- [ ] 临时文件用 trap 清理
- [ ] 周期任务有文件锁防并发
- [ ] 无 force-push / 无 rm -rf 危险操作
- [ ] 本地用 cron 模拟环境测试过（env -i）
```

本地模拟 cron 环境测试：

```bash
# 用最小环境模拟 cron 执行
env -i HOME="$HOME" PATH="/usr/local/bin:/usr/bin:/bin" \
  bash -c 'cd /repo && python3 tools/job.py'
```

## NO_REPLY 约定详解

许多平台把精确输出 `NO_REPLY` 视为"静默成功"（不触发人工通知）。

| 场景 | 输出 | 平台行为 |
|:-----|:-----|:---------|
| 成功 | `NO_REPLY`（或空） | 不通知 |
| 成功但有需知 | 简短摘要 | 通知（低优先级） |
| 失败 | `ALERT: <原因>` 到 stderr | 通知（高优先级） |

若运行时不支持 `NO_REPLY`，等效于"成功时打印空"。

## 场景化指南

### 场景 A：加固现有 cron 作业

```bash
# 1. 把 cron 里的多行命令提取为脚本
mkdir -p tools
cat > tools/daily-sync.py <<'EOF'
#!/usr/bin/env python3
import sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# ... 同步逻辑 ...
if success:
    print("NO_REPLY")
else:
    print("ALERT: 同步失败", file=sys.stderr)
    sys.exit(1)
EOF
chmod +x tools/daily-sync.py

# 2. cron 改为一行
# 旧: bash -lc 'cd /app && python3 sync.py && ...'
# 新: python3 /repo/tools/daily-sync.py
```

### 场景 B：跨平台定时作业

```bash
# 检测平台跑对应脚本
case "$(uname -s)" in
  Linux*|Darwin*) python3 tools/job.py ;;
  MINGW*|MSYS*|CYGWIN*) python tools/job.py ;;
  *) echo "ALERT: 不支持的平台" >&2; exit 1 ;;
esac
```

### 场景 C：Agent 长驻守护脚本

```bash
# tools/guardian.sh
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.." || exit 1
LOCKFILE="/tmp/guardian.lock"
exec 200>"$LOCKFILE"
flock -n 200 || { echo "NO_REPLY"; exit 0; }

# 健康检查
if curl -sf http://localhost:8080/health >/dev/null; then
  echo "NO_REPLY"
else
  echo "ALERT: 服务健康检查失败 $(date)" >&2
  exit 1
fi
```

## FAQ

**Q：我的 cron 作业在 Windows 上跑怎么办？**
A：用 PowerShell 脚本替代 bash 脚本，遵循同样的三原则。参考跨平台适配表。Windows Task Scheduler 调度 `powershell -File tools\job.ps1`。

**Q：NO_REPLY 必须精确匹配吗？**
A：是的，精确输出 `NO_REPLY`（大写、无多余空格）。若平台不识别，等效于"成功时无输出"。

**Q：脚本优先是不是过度工程？**
A：不是。多行 shell 在 cron 里的引号陷阱几乎不可避免。脚本文件可测试、可版本控制、可 lint，长期收益远大于"省一个文件"。

**Q：pipefail 到底该不该用？**
A：该用，但要注意 `| head` 场景。`set -euo pipefail` 是好习惯，遇到 SIGPIPE 误报时局部 `|| true` 或改用脚本读取。

**Q：force-push 真的完全禁止吗？**
A：自动化脚本里禁止。个人临时分支可酌情，但 cron 作业绝不能 force-push，会覆盖他人成果。

**Q：和定时调度专家有什么区别？**
A：本技能管"脚本写得可不可靠"，定时调度专家管"调度得可不可靠"。一个防 shell 炸，一个防漏跑。

## 故障排查速查

| 症状 | 查这里 |
|:-----|:-------|
| `unexpected EOF` / 引号错误 | 模式 1：脚本优先 |
| 明明成功却报失败 | 模式 2：SIGPIPE |
| 本地能跑 cron 不行 | 模式 3：cwd/env 漂移 |
| git push 被拒 | 模式 4：non-fast-forward |
| python -c 引号乱 | 模式 5：写脚本文件 |
| Windows 路径错 | 模式 6：PowerShell 路径 |
| 临时文件冲突 | 模式 7：trap 清理 |
| 周期任务重叠 | 模式 8：文件锁 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent
- **操作系统**：Linux / macOS（POSIX）/ Windows（PowerShell）
- **Shell**：bash 4+ / sh / PowerShell 5+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| bash 或 PowerShell | Shell | 必需 | 系统自带 |
| python3 | 运行时 | 推荐（脚本载体） | 系统自带或 python.org |
| flock | CLI | Linux/Mac 推荐（文件锁） | util-linux 自带 |
| curl | CLI | 可选（健康检查） | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本技能本身无需 API Key。
- 被守护的脚本可能需要外部 API Key，必须在脚本内通过环境变量引用并文档化，禁止硬编码。

### 可用性分类
- **分类**：MD+EXEC（Markdown 指南 + 脚本执行）
- **说明**：本技能提供加固原则与故障模式目录，Agent 据此编写/审查 cron 脚本，实际执行由调度系统调用脚本。
