---
schema_version: 2
project_name: "……"
project_root: "……"
jys_workspace: "jys-workspace"
current_stage: S1
current_skill: jys-s1
next_skill: jys-s1
next_action: "确认本项目使用的套路内核和变体"
waiting_for: "套路内核和变体选择"
s1: not_started
s2: not_started
s3: not_started
s4_outline: not_started
s4_script: not_started
s5_delivery: not_started
final_confirmation: pending
last_updated: "……"
---

# JYS 工作状态

> 本文件只属于当前项目。JYS 与 S1-S5 必须沿用本文件所在的同一个 `jys-workspace`，不得根据任务名重新推断路径，也不得跨项目读写。项目整体移动后，确认仍为同一项目再更新 `project_root`。

## 状态说明

- `not_started`：尚未开始。
- `in_progress`：正在处理或等待本阶段必要选择。
- `confirmed`：用户已明确确认。
- 每轮结束必须更新 `current_skill`、`next_skill`、`next_action`、`waiting_for` 与 `last_updated`。

## S1 套路内核

……（待 S1 填写）

## S2 定制化剧情骨架

……（待 S2 填写；完整过程保存在 `s2-workspace.md`）

## S3 带货产品

- 产品名称：……（待 S3 填写）
- 产品文件：……（待 S3 填写）
- 不可变产品事实：……（记录产品规格、单件/单盒基础数量及其他明确事实）
- SKU：……（逐条原样记录 product 文件中的完整 SKU；价格与购买数量或规格不可拆分）
- 明确功能机制：……（只记录产品资料已说明的作用方式）

## S4 写作进度

- 大纲状态：未开始
- 已确认段落：无
- 当前段落：无
- 完整过程：`s4-workspace.md`

## S5 交付进度

- 完整交付：未开始
- 最终确认：待确认

