# 操作字段、结构限制与导出

## 生成图表方案

`diagram.plan` 接收 `prompt`、`type`、`direction`、`theme` 与可选 `instructions`。描述长度为 5 至 12000 字符；类型为 `flowchart`、`sequence`、`state`、`erd`、`architecture`；方向为 `TB`、`LR`、`BT`、`RL`；主题为 `light`、`dark`、`neutral`。

结果是版本 1 的结构化图表，包含 `title`、`nodes` 和 `edges`。节点最多 100 个，关系最多 200 条；ID 以字母开头且保持稳定。关系的 `from` 和 `to` 必须引用已有节点，不允许重复 ID、悬空关系或自环。入口不接收原始 Mermaid、HTML、URL、文件路径或脚本。

## 渲染并导出图表

`diagram.render` 接收当前用户成功的 `plan_task_id`、可选 `edits` 与 1 至 4 个不重复的 `formats`。`edits` 只能覆盖 `title`、`direction`、`theme`、`nodes`、`edges`；格式限 `svg`、`png`、`pdf`、`json`。

平台使用锁定版本 Mermaid 11.12.1 与 Playwright 1.55.1 本地渲染，阻断远程资源并清理 SVG。结果通过私有 `artifacts` 交付，不产生公开 URL。
