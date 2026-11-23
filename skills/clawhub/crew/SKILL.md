---
name: crew
description: 在 iTerm2 里给当前会话分屏，新开一个跑在 tmux 里的 agent（codex / agy / claude，可指定模型和 effort），组员之间用 tmux 互发消息；还能把整组保存到项目目录并一键恢复窗口、模型、effort 和历史对话。用户运行 /crew，或要求"新开一个 agent / 分屏起个 codex / 保存 agent 组 / 恢复 agent 组 / 给 design 发消息"时使用。
argument-hint: "[spawn [名称] [agent] [模型] [effort] | send <名称> <内容> | read <名称> | status | save | restore]"
---

# crew

所有操作都通过一个脚本完成，输出是 JSON（`ok: false` 时看 `error`）：

```bash
CREW=~/.claude/skills/crew/scripts/crew.py
python3 $CREW <子命令> ...
```

在项目目录里运行（脚本会向上查找 `.crew.json`）。需要 macOS、iTerm2、tmux，以及要用到的 agent CLI。

参数：`$ARGUMENTS`。为空时按 `spawn` 处理。

## 约定

- **组名** = 项目目录名（小写，非字母数字转成 `-`）。每个成员一个 tmux 会话，名为 `<组名>-<成员名>`，例如 `lego-design`。tmux 会话名是全局的，这个前缀用来避免不同项目的 `design` 撞在一起。
- **main** = 第一次执行 spawn 的那个 Claude Code 会话。它通常不在 tmux 里，这时组员给它发不了消息，由 main 用 `read` 去读组员的窗格。执行过 `restore` 之后 main 也进 tmux（`<组名>-main`），才能双向通讯。
- **状态文件**：`<项目>/.crew.json`，记录每个成员的 agent、模型、effort、会话 ID、分屏位置。

## spawn：新开一个 agent

1. `python3 $CREW models` 得到 6 个选项（codex、agy、claude 各前两个模型，带可用 effort；agy 跳过 `crew.py` 里 `AGY_MENU_SKIP` 列出的系列，目前是 argon，所以给出 neon 和 hydrogen）。
2. 用户在参数里已经给全（名称、agent、模型、effort）就直接到第 3 步。否则把 6 个选项列成编号清单，一次问清三件事：选哪个编号、agent 叫什么名字（如 `design`）、effort（默认 `high`）。让用户用一行回复，例如 `2 design high`。不要用 AskUserQuestion 做六选一（它最多 4 个选项）。
3. 启动：

   ```bash
   python3 $CREW spawn --name design --agent codex --model gpt-6.2-astra --effort high \
     --main-model <你自己的模型 ID>
   ```

   - `--main-model` 填你当前运行的模型 ID，恢复时 main 用它启动。
   - 名称只能用小写字母、数字、连字符。
   - 用户口头说的模型（如"astra 62"）对应到 `models` 输出里的 `model` 字段；对不上就问，不要猜一个相近的。
   - 默认分屏位置：第 1 个在 main 右侧，第 2 个在第 1 个下方，第 3 个在 main 下方，之后依次在已有 agent 右侧。要指定位置用 `--from <成员名> --split v|h`（v 左右分，h 上下分）。
   - codex 默认以 full access 启动（`-s danger-full-access -a never`）：执行命令不受沙箱限制，也不请求审批，范围是整台机器；这样它才能连上 tmux 主动给组员发消息。用户明确要求保留沙箱时加 `--sandbox`，此时 codex 不能主动发消息，只能被读取。
4. 脚本会等 agent 就绪、自动确认"信任此文件夹"对话框、给新 agent 发一条说明（组里有谁、怎么发消息），并记录会话 ID。看返回的 `status`：
   - `ready`：成功。告诉用户名称、模型、effort。
   - `trust_prompt` / `timeout` / `exited`：用 `read` 看窗格里是什么，把情况告诉用户。

## send / read：通讯

```bash
python3 $CREW send --to design "请看一下 SPEC.md 第 3 节，给出修改建议"
python3 $CREW read --name design --lines 80
```

- `send` 会自动加上 `[from <发送者>]` 前缀，支持多行。
- 发完消息对方需要时间处理；用 `read` 查看结果。还在生成时过一会儿再读，不要连续快速轮询。
- 给不在 tmux 里的成员发消息会报错（常见于 main 尚未恢复过）。

## status

`python3 $CREW status`：每个成员是否在 tmux 里、所在 tty、已保存的会话 ID 和当前实际的会话 ID。

## save：保存整组

```bash
python3 $CREW save --main-model <你自己的模型 ID>
```

- 重新读取每个窗格当前的会话 ID（成员执行过 `/clear` 或新开对话后 ID 会变），更新 `.crew.json`。
- 在项目目录生成 `<组名>-crew.command`，双击即可恢复。
- 把返回的 `updated`（ID 有变化的成员）和 `missing_session_id`（没有会话 ID、恢复时会开新对话的成员）告诉用户。

## restore：恢复

用户双击 `<组名>-crew.command`，或运行 `python3 $CREW restore --dir <项目目录>`。

- 该组窗口已经开着：切换过去。
- 否则新开一个 iTerm2 窗口，main 在 `<组名>-main` 里按会话 ID 恢复，其余成员按保存的分屏顺序依次恢复，各自带上原来的模型和 effort。
- tmux 会话还活着（只是窗口关了）时直接接回去，不会重启 agent。
- **main 的原窗口还开着时会拒绝恢复**：同一个对话不能被两个进程同时写。所以不要在 main 自己的会话里替用户执行 restore；告诉用户先退出当前这个窗口，再双击 `.command`。

## 已知限制

- 只恢复分屏结构，不恢复窗格的精确尺寸。
- 成员刚 `/clear` 还没说过话就保存，记录的是一个空对话的 ID，恢复时可能找不到对话；让它先回一句话再保存。
- 目前只支持由 Claude Code 会话作为 main 建组。
- 没有"移除成员"命令：关闭某个 agent 用 `tmux kill-session -t <组名>-<成员名>`，再手动把它从 `.crew.json` 的 `members` 里删掉。
