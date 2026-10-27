# MochiLab 学习陪练与错题复习 · Study Coach and Mistake Review

`mochi-study-coach` · v1.0.0 · MIT-0

围绕卡住的知识点讲解和练习，记录错因与参考依据，按复习记录安排下一次练习。

Explain difficult concepts, practice related questions, record mistakes and sources, and schedule the next review from actual results.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-study-coach`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. 

## 示例 / Examples

## 能帮你做什么

从学生的解题过程定位问题，逐步提示、讲解并安排同类练习；保存参考答案、来源和复习反馈，持续追踪薄弱点。

## 直接这样说

```text
这道题我卡在第二步，先提示我，不要直接给答案。
```

```text
帮我记录这次错因，明天用同类题再练一次。
```

```text
今天该复习哪些题？先别显示参考答案。
```

## 保存与继续使用

结果保存在当前助手的工作区，后续可以按记录编号查找和继续处理。


## What it does

Work from the learner’s attempt to give progressive hints and related practice; retain reference answers, sources, review feedback and due dates.

## Try it

```text
I’m stuck on step two; give me a hint before the full answer.
```

```text
Record this mistake and give me a similar exercise tomorrow.
```

```text
Show today’s review questions without the answers.
```

## Save and continue

Records stay in the active agent workspace and can be retrieved by their IDs.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
