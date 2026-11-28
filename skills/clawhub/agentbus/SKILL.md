---
name: agentbus
description: "多 agent 共享文件夹任务总线：派单、领取、回执、台账，每一步留痕；角色由 CONTRACT.md 决定，不绑定任何产品。"
version: 0.2.0
slug: agentbus
displayName: "Agent Bus"
summary: "零依赖单文件任务总线。把活派给另一个 agent，结果可追查、可复核。"
tags: [task-bus, multi-agent, handoff, audit, cli, coordination]
homepage: "https://github.com/lisong2003-lgtm/agentbus"
license: MIT
---

# Agent Bus

一个共享文件夹当任务总线。派单方建任务包，执行方领取、干活、写回执，
`complete` 时校验结论码并记台账。没有 broker、没有 socket、没有数据库。

## 何时使用

- 本机有两个以上 AI agent，需要把活交给另一个做，过几天还能查"谁干的、干完没"。
- 用户提到"总线""派单""回执""台账""交接"，或给出了一个 `CONTRACT.md` 路径。
- 需要跨会话、跨天交接；需要留下可复核的审计记录。

## 何时不用

- 只有一个 agent；或只是"问一句、答一句"。交接没有意义。
- 需要实时对话、并发修改同一份文件。这套只支持"一个任务一个人领"。

## 第一步：先看有没有总线

```bash
python3 agentbus.py status          # 没初始化会报错
python3 agentbus.py doctor          # 有总线就体检
```

找不到 `agentbus.py` 时，先按用户给的路径找；仍找不到就问他总线在哪，
**不要自己新建一条**——空总线会让任务静默丢失。

## 作为执行方接入

```bash
python3 agentbus.py claim --worker <你的名字>   # 领一个任务，拿租约
# 读任务包，干活，把结果写进同目录的 回执包.md
python3 agentbus.py complete --id <编号>
```

回执里必须有一行且只有一行结论：

```
结论：COMPLETED
```

允许 `COMPLETED` / `FAIL` / `PARTIAL`（`PASS` 视作 `COMPLETED`）。写在正文句子里不算，
会被拒收——这是故意的，防止"未达到 PASS"被读成通过。

长任务记得续租，否则租约过期会被别人重新领走：

```bash
python3 agentbus.py heartbeat --id <编号>
```

## 作为派单方

```bash
python3 agentbus.py dispatch --title "..." --goal "..." --assignee worker-a
```

验收标准里尽量写"每项差异须附实测命令与原始输出"这类可核对的约束——
这是这套东西唯一能防住 AI 编造的地方。

## 命令

| 命令 | 作用 |
|---|---|
| `init` | 初始化或接管已有总线（幂等，不动历史） |
| `dispatch` | 建任务包入队 |
| `claim --worker X` | 原子领取，拿租约 |
| `complete --id X` | 校验回执结论，写台账与复盘 |
| `status` | 队列状态（JSON） |
| `doctor [--fix]` | 体检；`--fix` 隔离坏队列文件 |
| `requeue [--id X]` | 过期任务放回队列 |
| `heartbeat --id X` | 续租 |
| `adapter <name>` | 打印某 agent 的接入片段 |

## 边界

- 不并发：一个任务只能一个人领。
- 不校验内容质量：哈希只证明文件没变，不证明内容对。
- 不改别人的东西：不要动已领取的任务，不要手工改台账。
- worker 不自判通过：结论码由谁出，写在 `CONTRACT.md` 里。

## 排障

| 现象 | 原因 |
|---|---|
| `claim` 一直返回 `EMPTY` | 队列真为空，或 pending 里的文件损坏（已自动隔离进 `corrupt/`） |
| `complete` 报"缺少结论" | 结论码写进了句子，没有独占一行 |
| `complete` 报"还在 pending" | 忘了先 `claim` |
| 任务莫名消失 | 领了不交且租约过期，被人 `requeue` 重新领走了 |

详细用法见同目录 `README.md`。
