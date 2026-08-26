---
name: jys-s4
description: |
  执行JYS的S4剧本写作：把S2剧情骨架细化为事件级大纲，确定产品植入并逐段完成台词。默认由$jys主控调度；仅当用户明确调用$jys-s4、JYS状态的next_skill为jys-s4，或当前已处于S4且用户修改开头钩子时直接使用。普通完整短剧请求交给$jys。
---

# S4 写剧本

## 调用与前置条件

1. 每轮开始完整读取 [JYS工作区契约](../jys/references/workspace-contract.md)、`JYS_WORKSPACE/status.md` 和 [JYS创作规则](../jys/references/creation-rules.md)。
2. 默认由 `jys` 主控调度；用户明确调用 `$jys-s4` 或状态中的 `next_skill` 为 `jys-s4` 时可直接执行。
3. 沿用已绑定的 `JYS_WORKSPACE`，不得搜索其他项目。确认 `s1`、`s2`、`s3` 均为 `confirmed`，并能读取 `s2-workspace.md` 与S3确认的完整产品资料；缺少前置条件时返回对应步骤，不得重置项目。
4. 根据 `s4_outline` 与 `s4_script` 进入当前阶段，保留用户已经确认的内容。

## 职责与边界

- 先确认事件级大纲，再逐段完成剧本。
- S2确定剧情走向和首段剧情功能，不锁定首段的具体台词、动作和画面。
- 不得改变S2确认的核心因果、人物关系和产品机制必要动作。
- 用户确认后的S4事件级大纲是逐段写作唯一的剧情依据。
- 对标剧本只参考信息密度和表达方式，不能新增大纲中没有的事件。
- 产品事实和SKU只以当前项目确认的product文件为准。

## 执行路径

| 当前任务 | 必读文件 |
|---|---|
| 事件级大纲尚未确认 | [01-事件级大纲](references/01-事件级大纲.md) + [开头钩子设计指南](../jys/references/开头钩子设计指南.md) |
| 逐段写作 | [02-逐段写作](references/02-逐段写作.md) |
| 当前是首段或用户修改开头 | 在当前阶段文件之外，额外读取 [开头钩子设计指南](../jys/references/开头钩子设计指南.md) |
| 当前是带货段 | 在 `02-逐段写作` 之外，先读取 [03-带货段落](references/03-带货段落.md) |

不得读取与当前任务无关的S4 reference，也不得用一个reference覆盖另一个reference的职责。

## 工作文档

- 只使用 `JYS_WORKSPACE/s4-workspace.md`。
- 文件不存在时创建；存在时先读取并续写。除非用户明确要求重置当前项目，否则不得覆盖或清空。
- 大纲确认后写入一次；每段正文确认后追加一次。每次先读取，再写入完整累计内容。
- 最终剧本从工作文档读取并整合，不依赖历史消息。

## 状态转换

- 大纲确认前保持 `s4_outline: in_progress`、`next_skill: jys-s4`。
- 大纲确认后写入工作文档，将 `s4_outline` 标记为 `confirmed`、`s4_script` 标记为 `in_progress`，继续使用 `jys-s4`。
- 完整剧本确认后将 `s4_script` 标记为 `confirmed`，并把 `next_skill` 更新为 `jys-s5`。
- 每轮结束前更新当前/下一 Skill 和动作，并按共享契约输出默认下一步尾注。
