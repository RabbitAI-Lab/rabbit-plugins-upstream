# REPORT() 通用汇报识别与路由

**Skill ID：** `zayn-report`

**版本：** `v0.3.0`

**状态：** Draft for testing

## 核心用途

识别汇报类型、对象、目的和周期，将日报、周报、月报、年中报告、年度报告、升级、决策及会议总结交给对应 Skill；仅为单项目汇报提供有限兜底。

## 适用与不适用

- 适用：类型不明的汇报、项目进展、需要判断调用哪个汇报 Skill。
- 不适用：已明确的单日日报、整周周报、月报、年中报告或年度报告，应分别使用对应专项 Skill。

## 输入要求

提供汇报对象、目的、时间范围、原始事实和期望形式。缺失时先补问，不猜测。

## 运行与输出

解析参数并输出状态表，判断类型后路由；只有单项目且事实充分时才输出通用项目汇报。

## Skill 关系

关联 `zayn-daily-report`、`zayn-weekly-report`、`zayn-monthly-report`、`zayn-midyear-report`、`zayn-annual-report`、`zayn-escalate`、`zayn-decision`、`zayn-minutes` 和 `zayn-route`。只允许一个 Skill 生成最终文本。

## 快速示例

输入“整理今天给领导看的工作总结”时，返回路由到 `zayn-daily-report`，不直接代写日报。

模板负责记录事实，Skill 负责检查、追问、分析和纠偏。
