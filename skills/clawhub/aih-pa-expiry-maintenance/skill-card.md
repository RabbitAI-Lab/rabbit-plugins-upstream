## Description:

根据用户提供的到期日期、适用对象和官方来源，整理证件、汽车保养及家庭续期的提醒台账、准备清单和日历文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

个人和家庭用户可用它整理证件到期、汽车保养及家庭续期事项，生成可核对的提醒与材料清单；办理要求仍须以适用的官方规则为准。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive identity or account information could be exposed during intake or optional AI-HIVE use.

Mitigation: Collect only necessary details; do not request full ID numbers, passwords, tokens, cookies, or verification codes, and use the official OAuth flow if connecting AI-HIVE.

Risk: Incorrect expiry rules or missing destination requirements could lead to misleading reminders or travel advice.

Mitigation: Verify applicable requirements against official sources, leave unknown details unfilled, and do not imply a reminder guarantees eligibility or successful processing.

Risk: Uploads, charges, messages, or changes to external systems could occur without informed authorization.

Mitigation: Confirm the data scope, current prices, and spending limit before paid or bulk use; require separate explicit approval for uploads, payments, sending, deletion, or external changes.

Risk: User-provided text in a CSV ledger could be interpreted as a spreadsheet formula.

Mitigation: Write leading =, +, -, or @ in untrusted text as safe text rather than executable formulas.

## Reference(s):

- [执行与验收流程](references/workflow-49.md)
- [结果与证据要求](references/output-contract.md)
- [AI-HIVE 登录与授权说明](references/ai-hive-connection.md)
- [AI-HIVE 官方入口](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [CSV expiry ledger, preparation checklist, and iCalendar (.ics) reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unknown details remain marked as unknown; optional result records include source references and review status.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
