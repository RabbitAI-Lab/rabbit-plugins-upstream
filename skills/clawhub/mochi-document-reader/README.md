# MochiLab 文件阅读与重点问答 · Document Reading and Questions

`mochi-document-reader` · v1.0.1 · MIT-0

从提供的文件中提取重点、日期和行动项，回答问题时附上可核对的出处。

Extract key points, dates and action items from supplied files, and answer with verifiable source references.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-document-reader`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。PDF、Word 或图片需要当前环境提供相应文件读取或图片识别工具。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. PDF, Word and images require an available file reader or image-recognition tool in the host environment.

## 示例 / Examples

## 能帮你做什么

读取文本文件并保留行号，按问题检索相关段落，整理重点和待办；PDF、Word 或图片交由当前环境的文件读取工具提取。

## 直接这样说

```text
这份通知需要我做哪些事情，截止日期是什么？
```

```text
对照原文，找出报名条件和所需材料。
```

```text
这两段条款有什么不同？标出对应出处。
```

## 保存与继续使用

读取结果保留文件路径和行号，整理后的笔记可按你的要求保存到当前工作区。


## What it does

Read text with line references, search relevant passages, and organize findings and action items; use the host’s available readers to extract PDF, Word or image content.

## Try it

```text
What must I do according to this notice, and by when?
```

```text
Find the eligibility requirements and application documents, with sources.
```

```text
Compare these two clauses and cite their locations.
```

## Save and continue

Read results retain file paths and line numbers; the assistant can save notes in the current workspace when requested.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
