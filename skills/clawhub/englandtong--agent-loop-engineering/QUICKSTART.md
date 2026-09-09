# Quickstart / 快速开始

Advanced. This is the execution plane for coding work that is **already
authorized**. If the goal is still vague, use `cms-project-governance` first.

## Install / 安装

```bash
openclaw skills install agent-loop-engineering
```

## Try it in 30 seconds / 30 秒验证

Say to your agent / 对 agent 说：

```text
接着跑，把失败的测试修掉，别每一步都问我
```

You should get / 你应该得到：

- a bounded loop that runs in stages and keeps loop state in `Docs/`;
- automatic stops at stage review instead of one endless run;
- a final verdict of `Ready for Independent Acceptance`, `Needs Fix`,
  `Blocked` or `Invalid State`.

If it asks you for a target or acceptance criteria, that is correct — it will
not start without them.

## Safety / 安全

- Writes only inside the resolved workspace.
- Stops and asks before destructive Git, migration, reset, overwrite or force
  push.
- Stops after two consecutive attempts with the same failure signature.
- Stores no API keys, tokens or credentials.
