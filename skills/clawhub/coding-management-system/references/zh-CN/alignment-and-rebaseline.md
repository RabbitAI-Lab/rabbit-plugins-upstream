# 方向对齐、重基线、审计与路线图

使用足以回答当前问题的最轻审查。方向检查、目标修改和全项目审计必须分开。

## 方向对齐

每个阶段询问：

1. 用户或操作人员得到了什么变化？
2. 它服务哪个 Target 和验收标准？
3. 假设、范围或架构是否移动？
4. 下一步是否仍是最高价值的授权动作？
5. 什么证据可以反驳过早完成？

第 3、6、10 阶段记录正式结论：

- `Aligned - Continue`
- `Aligned - Ready for Review`
- `At Risk`
- `Locally Compliant, Globally Misaligned`
- `Owner Review Required`
- `Blocked`

以下情况立即触发：

- 连续两次核心或 QA 失败；
- 范围增长超过 20%；
- 自动检查通过但主要用户流程失败；
- Agent 无法用一句话说明与目标的关系；
- 新想法改变 Core Target、Non-Goals、架构、数据、Release 或生产行为；
- 技术上正确但不再解决原始问题。

方向对齐不能改写 Target。

## 新想法分类

在一个 decision/backlog 区域记录并分类：

- `Observation`
- `Clarification`
- `Improvement Candidate`
- `Scope Change`
- `Core Target Change`
- `Conflict`

只有不改变 acceptance 或 Non-Goals 的 Clarification 可以立即影响活动工作。Improvement Candidate 等待下一次计划边界；Scope、Target 和 Conflict 必须 Controller 或 Owner 复核。

## Target 重基线

当新需求可能改变 Target、Non-Goals、架构/数据边界、Release 策略或验收时使用。

比较：

- 旧目标及原因；
- 新需求；
- 增加的用户价值；
- 被保留或作废的当前工作；
- 验收变化；
- 成本与风险；
- Owner 决策。

决策：

- `No Target Change`
- `Clarification Only`
- `Scope Change Approved`
- `Core Target Change Approved`
- `Owner Decision Required`
- `Reject / Defer`

重基线审查中不能编码或 Dispatch。Owner 批准后先更新 Target 和 Acceptance，再使用独立 Planning/Dispatch 模式。

## 全项目审计

全项目审计默认只读，可评估架构、代码质量、完成度、证据健康、风险债务和治理一致性。不能签署最新交付、修改 Target 或 Dispatch。

分开列出：

- 已验证当前事实；
- 过时或缺失证据；
- Accepted-With-Risk 债务；
- 误导性完成声明；
- 局部成功但不服务整体目标的工作；
- Owner 决策。

## 路线图与结束线

定义：

- 原始结果；
- 当前用户可感知能力；
- 当前阶段 Must Finish；
- Not Required Now；
- 必须停止扩展的内容；
- 下一个可独立产生价值的交付；
- 明确结束证据。

不能把每个小修复当成 Milestone。只有连贯能力通过验收后才关闭 Milestone。

