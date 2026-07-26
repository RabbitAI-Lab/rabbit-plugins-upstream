# 证据与完成判定

## 证据类别

自动证据包括：

- 针对性测试和回归测试；
- typecheck；
- build；
- lint 或静态分析；
- Schema、migration 或确定性产物验证。

功能证据包括：

- 浏览器或 UI 工作流；
- API 请求和响应；
- CLI 实际行为；
- 生成文件检查；
- 安装、启动、重启流程；
- 设备或目标环境 smoke；
- 操作人员工作流。

需要独立证据时，可使用：

- QA 重新运行；
- Reviewer 独立复现；
- 干净环境；
- 只获得任务原始材料的独立 Agent；
- Release 或类生产门禁。

## 证据质量

证据必须说明：

- 运行或观察了什么；
- 环境；
- 时间；
- 结果和退出码；
- 产物或日志路径；
- 重大限制。

只有“测试通过”“看起来正常”“已经实现”等文字，不构成充分证据。

## 证据冲突

采用较差结果：

- build 通过但用户流程失败：未完成；
- unit test 通过但目标环境不可用：环境标准仍未完成；
- 截图正常但交互失败：未完成；
- 自己的 round-trip 通过但真实 consumer 失败：未完成；
- Developer 说完成但 QA 失败：`Needs Fix`。

## Ready For Review

只有以下条件全部满足才设置 `Ready for Review`：

- 所有授权 Must Pass 已勾选；
- 必需自动证据通过；
- 必需功能证据通过；
- 回归范围合理；
- 已明确已知限制；
- 没有停止规则；
- 结果仍与原始目的对齐。

## Accepted With Risk

仅在以下条件使用：

- 核心用户结果可用；
- 剩余风险不阻塞；
- 影响和负责人明确；
- Follow-up 和时限/边界已记录；
- 缺少的不是核心用户流程或必需环境验证。

重复出现的 Accepted-With-Risk 必须触发治理复核。

## Lite 独立完成

当 `qa_required: false` 时，只有自动和功能证据都通过、全部标准已勾选，执行 Agent 才能设置：

- `qa_decision: Accepted`
- `project_state: Accepted`

其他情况保持 `qa_decision: Not Reviewed`，设置 `execution_state: Ready for Review` 并交接。

## 活动不等于完成

以下不能证明完成：

- 使用时间；
- Loop 数量；
- 文件数或代码行；
- Markdown 记录数量；
- 只有 checker 通过；
- 没有可用行为的计划或 Handoff。

