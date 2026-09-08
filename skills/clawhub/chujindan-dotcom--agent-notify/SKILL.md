---
name: agent-notify
description: 让 agent（Claude Code / Codex / Hermes / OpenClaw 通用）干完活主动播报到语音设备（小智音箱、机器人等）。守护进程读会话记录判断任务状态，完成或卡死时把「任务名+状态+时间」拼成中文播报句推给后台。首次使用需配置后台 WebSocket 地址、设备 MAC、授权码。【服务器端后台设计重点】① 一个 WS 端点即可，握手首帧收 {"mac","code"}，回 {"type":"auth","ok":true} 或 ok:false + error（建议区分 invalid_code 与 session_not_found，客户端会把原文透传给用户）；② 只处理 type=="task_status" 的帧，直接取现成的 text 字段丢 TTS，其余 type 静默忽略——注意静默丢弃在协议层零反馈，排障时极难定位；③ 鉴权铁律：播给哪台设备必须由 code 反查绑定关系，绝不信任请求体里的 mac，否则任何拿到 token 的人改个 MAC 就能往别人设备推送；④ 设备离线是常态而非边界情况（小智类设备约两分钟无人声即断连），后台需要 pending 队列在设备重连后补播并设 TTL，否则大部分通知会蒸发；⑤ 30 秒 ping/pong 保活，客户端断线指数退避重连、握手被拒则不重连；⑥ 播报文案由客户端拼好（状态已译成中文、ISO 时间已转成"下午2点05分"），后台不必二次加工。Triggers 触发词：任务播报, 干完告诉我, 通知机器人, 语音播报, agent-notify, 配置播报, 开启播报, 停止播报, 停止这个skill, 关闭后台监听, 播报状态, 小智播报。
---

# agent-notify

干完活让机器人喊你一声。跨 agent 通用（Claude Code / Codex / Hermes / openclaw）。

所有操作都通过同目录的 `notify.py`。配置存在 `~/.agent-notify/config.json`，**所有 agent 共用一份**——在 Claude Code 里配好了，Codex 那边直接能用。

## 第一次使用：配置 + 校验 + 启动

先看有没有配过：

```bash
python3 <SKILL_DIR>/notify.py status
```

**如果没配过**，向用户要三样东西，一次问全，别挤牙膏：

1. **后台 WebSocket 地址** —— 例如 `ws://192.168.1.10:9004/agent/notify`
2. **设备 MAC** —— 就是音箱/机器人的 device-id，例如 `aa:bb:cc:dd:ee:ff`
3. **授权码** —— 后台签发的，后台会同时校验它和 MAC

拿到后：

```bash
python3 <SKILL_DIR>/notify.py setup \
  --url ws://192.168.1.10:9004/agent/notify \
  --device-id aa:bb:cc:dd:ee:ff \
  --auth-code XXXX
```

`setup` 会**立刻建一次 WebSocket 连接做校验**。看到这行才算通：

```
✓ 校验通过：授权码和 MAC 后台都认，skill ↔ 后台 ↔ 设备可以协同工作
```

没通就把 `✗ 校验失败：` 后面的原话念给用户，别自己编原因。常见三种：

| 报错 | 真实原因 |
|---|---|
| `后台拒绝：invalid_code` | 授权码不对，找后台核对 |
| `后台拒绝：...` | MAC 不在该授权码名下，或设备未登记 |
| `后台没有回校验结果（超时）` | 接口没实现，或地址写错 |
| `did not receive a valid HTTP response` | **多半是代理**。`env \| grep proxy` 看一眼；notify.py 默认已绕过代理，若仍失败则是端口不通 |

校验通过后启动后台监听：

```bash
python3 <SKILL_DIR>/notify.py start
```

守护进程脱离终端运行，**agent 退出后它还活着**，直到显式 stop。

## 停止

用户说"停止这个 skill / 关掉播报 / 别再通知我了"：

```bash
python3 <SKILL_DIR>/notify.py stop
```

## 手工推一条

用户说"跟机器人说一声 xxx"，或者你想在长任务开始时先打个招呼：

```bash
python3 <SKILL_DIR>/notify.py send --task "跑评测" --status started
python3 <SKILL_DIR>/notify.py send --task "跑评测" --status done --detail "LoCoMo 0.8175"
```

`--status` 取值：`done` `error` `stuck` `need_input` `started`

## 它是怎么知道任务状态的

没有 IPC，靠读会话记录文件。每个 agent 只有"文件在哪、怎么读"不同：

| agent | 会话文件 | 判据 | 验证程度 |
|---|---|---|---|
| claude-code | `~/.claude/projects/*/*.jsonl` | `stop_reason`：`end_turn`=完成，`tool_use`=在干 | **本机实测通过** |
| hermes | `~/.hermes/sessions/session_*.json` | 最后一条 assistant 且不含 tool_use = 完成 | 格式实测，未跑活会话 |
| codex / openclaw | 各自 sessions 目录 | 通用 JSONL 解析 | **未实测，可能判不准** |

判不出来时返回 `unknown`，**只沉默不误报**——绝不因为看不懂就谎报"完成"。

推送两种事件：

- **done** —— 一轮跑完
- **stuck** —— 还在 `tool_use` 但会话文件 10 分钟没动静。这是卡死，也是最该叫你的那个状态

同一轮只推一次（任务名+时间做指纹去重）。

## 后台要实现什么

一个 WebSocket 端点，四种 JSON 文本帧：

```jsonc
// 1. agent 连上来的第一帧
→ {"mac":"aa:bb:cc:dd:ee:ff","code":"<授权码>",
   "agent":"claude-code","host":"walter-pc","v":1}   // agent/host 是附带信息，后台可忽略
← {"type":"auth","ok":true}
← {"type":"auth","ok":false,"error":"invalid_code"}       // code 不对
← {"type":"auth","ok":false,"error":"session_not_found"}  // code 对，但这个 mac 没有活跃会话
// 客户端不校验应答的 type，只认 ok 字段，兼容 hello_ack 那种写法。

// 2. 状态推送
→ {"type":"task_status","agent":"claude-code","task":"跑一下评测","status":"done",
   "time":"2026-09-08T11:09:21+08:00","detail":"",
   "text":"对了，你要我监测的Claude Code任务：跑一下评测的状态变成：已完成，时间为上午11点09分，别忘了哦"}
← {"type":"ack"}        // 可选，不回也不影响
// ⚠ type 必须是 "task_status"。线上后台对其它 type（notify/tts/speak/message）
// 走的是"忽略非 task_status 消息"分支：不报错、不回包、不关连接，纯静默丢弃。
// 实测踩过——协议层完全看不出错，只能靠音箱响不响判断。

// 3. 保活，30 秒一次
→ {"type":"ping"}
← {"type":"pong"}
```

### 服务器端设计重点

六条，前三条决定能不能跑通，后三条决定好不好用。都是实测踩出来的。

**① 鉴权：设备必须由 code 反查，绝不信请求里的 mac**
`mac` 只用来对账。若直接拿请求体里的 mac 决定播给谁，任何拿到 token 的人改个 MAC 就能往别人设备推送。正确做法是后台存一张 `code → 绑定设备` 的表，一个 code 只能捅一台设备，吊销就是删一行。

**② 静默丢弃是排障黑洞，务必留日志**
后台若走"忽略非 task_status 消息"这类分支，请**至少打一行日志**。协议层不报错、不回包、不关连接，客户端完全看不出区别——实测发 `notify`/`tts`/`speak`/`message` 四种 type 全是石沉大海，最后只能靠"音箱响不响"来二分定位，极其低效。

**③ 错误码要能区分**
建议至少给出 `invalid_code`（码不对）和 `session_not_found`（码对但该设备没有活跃会话）两种。客户端会把 error 原文透传给用户，能区分就少一半来回。

**④ 设备离线是常态，不是边界情况**
小智类设备约两分钟无人声就断连。人写代码写半小时，agent 干完那一刻设备大概率不在线。所以后台**需要 pending 队列**：`session_not_found` 时落盘暂存，设备重连后补播，并设 TTL（如 6 小时）和条数上限，避免隔夜的通知第二天早上集中轰炸。没有这一层，大部分通知会直接蒸发。

**⑤ 保活与重连**
30 秒 ping/pong。客户端已实现断线指数退避重连；但**握手被拒不重连**——那是配置错，重试只会刷屏。

**⑥ 播报文案已经拼好，别二次加工**
`text` 字段里状态已译成中文（`done`→已完成）、ISO 时间已转成口语（`下午2点05分`）。直接丢 TTS 即可。若后台想自己拼，注意这两处：英文枚举会被念成"状态变成 done"，ISO 时间会被念成"二零二六年零九月零八日T十四时零五分"。

### 播报文案

`text` 字段是拼好的播报原文，后台**直接丢给 TTS 即可**，不用再拼：

```
对了，你要我监测的{agent}任务：{任务名}的状态变成：{状态}，时间为{时间}，别忘了哦
```

两处必须做转换，否则念出来是灾难（模板在 `notify.py` 顶部的 `TEMPLATE` / `STATUS_CN`）：

| 原始值 | 播报值 | 不转会念成 |
|---|---|---|
| `done` / `error` / `stuck` / `need_input` / `started` | 已完成 / 出错了 / 卡住了 / 在等你确认 / 开始跑了 | "状态变成 done" |
| `2026-09-08T11:09:21+08:00` | 上午11点09分（整点说"11点整"） | "二零二六年零九月零八日T十一时…" |

`agent` / `task` / `status` / `time` 四个结构化字段照旧保留，后台要落库或改口径都还有原料。

## 装到别的 agent

`notify.py` 不依赖任何 agent，把这个目录拷过去或做软链即可：

```bash
ln -s ~/.claude/skills/agent-notify ~/.hermes/skills/agent-notify
ln -s ~/.claude/skills/agent-notify ~/.codex/skills/agent-notify
```

配置是共用的，装完直接 `start` 就行，不用重新 setup。

## 自测

不碰真后台，本地起个假服务器把全流程跑一遍：

```bash
python3 <SKILL_DIR>/notify.py selftest
```

覆盖：拒绝错误授权 / 接受正确授权 / MAC 大小写归一化 / 检测到任务完成 / 推送内容含任务名+状态+时间。

## 依赖

`websockets`（Python）。缺了就 `pip install websockets`。
