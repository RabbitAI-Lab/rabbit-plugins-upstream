---
name: handoff-installer
description: Use when the user explicitly asks to install, update, adopt, or inspect the handoff protocol in a git repository. Do not use for starting, continuing, resuming, or handing off ordinary task work.
license: MIT-0
metadata:
  openclaw:
    requires:
      bins:
        - sh
        - git
      anyBins:
        - shasum
        - sha256sum
---

# Handoff 安装器

先检查当前用户消息，再使用工具。

- 没有明确要求安装、更新、采用旧版或检查状态：立即退出，不读仓库状态，不调用脚本，不修改文件。
- 明确要求检查：运行 `scripts/install.sh status [target]`。
- 明确要求首次安装：运行 `scripts/install.sh install [target]`。
- 明确要求更新：运行 `scripts/install.sh update [target]`。
- 明确要求采用无锁旧版：运行 `scripts/install.sh adopt-existing [target]`。

每次只选择一种模式。`target` 是用户指定的 git 仓库；省略时使用当前仓库。

`status` 永不转成写操作。`install` 报告旧版时，只提示用户明确要求 `update`；不要自行升级。
任何本地修改冲突都要停止，不得覆盖。

## 写模式确认

运行 `install`、`update` 或 `adopt-existing` 前：

1. 告知用户目标仓库的绝对路径，以及将写入的文件、创建的符号链接和会持久影响未来仓库工作的
   handoff 运行时策略。
2. 说明打包的运行时策略按本仓库约定使用中文；面向用户的沟通语言仍服从用户要求与适用规则。
3. 确认当前会话已有针对该模式和目标仓库的肯定确认。用户在知晓上述影响后明确指定模式和目标，
   可视为确认；否则先询问一次，收到确认前不得运行脚本。

`status` 只读，不需要写模式确认。

维护安装器时读 `references/protocol.md`；排查发现或触发行为时读 `references/compatibility.md`。

## 执行能力披露

四种模式都通过本地 shell 执行 `scripts/install.sh`，不发起任何网络请求，只操作 `target` 指向的
git 仓库：

- `status`：只读，只运行 `git` 查询命令，不写任何文件。
- `install` / `update` / `adopt-existing`：在 `target` 仓库内写入 `AGENTS.md`/`CLAUDE.md` 的
  handoff 片段、`.agents/skills/handoff/SKILL.md`、`.agents/tasks/TEMPLATE.md`、
  `tools/ledger.sh`、`.claude/skills/handoff` 符号链接；写入前逐项比对内容哈希，遇到不在
  预期旧/新哈希范围内的本地修改会中止，不覆盖。

不读取、不上传、不外发 `target` 仓库之外的任何数据。
