## Description: <br>
通联 VIP 对账单配置工作流。当有新增门店或终端需要配置VIP对账单时，按固定模板生成对账单配置表（6列格式）→发给康文博确认→建飞书任务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shouqianba](https://clawhub.ai/user/shouqianba) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations employees use this skill to prepare VIP reconciliation configuration spreadsheets for new stores or terminals, confirm them with the intended internal owner, and create the follow-up Feishu task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect merchant, store, or terminal identifiers can produce an invalid reconciliation configuration. <br>
Mitigation: Verify the merchant and terminal data before sending the Excel file. <br>
Risk: The generated Excel file may contain business-sensitive merchant or terminal data. <br>
Mitigation: Share the attachment only with the intended recipient and under the organization's data-handling rules. <br>
Risk: The named recipient and same-day Feishu task may not match every organization's workflow. <br>
Mitigation: Install and use the skill only when it matches the internal 通联 VIP reconciliation process, and confirm the recipient and deadline before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shouqianba/skills/tonglian-vip-reconciliation) <br>


## Skill Output: <br>
**Output Type(s):** [files, configuration, guidance] <br>
**Output Format:** [Excel spreadsheet plus concise message and task guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [One terminal per row; merchant, store, and terminal identifiers should be treated as text fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
