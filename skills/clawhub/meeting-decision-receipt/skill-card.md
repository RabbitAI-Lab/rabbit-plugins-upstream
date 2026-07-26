## Description: <br>
分析已有会议转写、纪要、笔记或讨论记录，区分已定、暂定、提议和责任承诺强度，并输出带证据的执行纪要和管理层纪要。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killsnake01](https://clawhub.ai/user/killsnake01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, team leads, and operations staff use this skill to audit meeting notes for what was actually decided, who clearly accepted work, and which assignments remain unconfirmed. It is intended for existing text, notes, or discussion records, not audio transcription, employee evaluation, or automatic sending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting notes may contain confidential business information. <br>
Mitigation: Process only authorized meeting text or files and review generated summaries before sharing. <br>
Risk: The skill may produce incorrect or misleading responsibility assignments if meeting language is ambiguous. <br>
Mitigation: Review evidence-backed classifications and keep unconfirmed assignments separate from confirmed commitments. <br>
Risk: Generated follow-up messages or tasks could be sent prematurely. <br>
Mitigation: Require a second explicit confirmation before any message or task is sent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/killsnake01/skills/meeting-decision-receipt) <br>
- [Publisher profile](https://clawhub.ai/user/killsnake01) <br>
- [Classification rules](references/classification-rules.md) <br>
- [Decision taxonomy](references/decision-taxonomy.md) <br>
- [Commitment taxonomy](references/commitment-taxonomy.zh-CN.md) <br>
- [Evidence rules](references/evidence-rules.md) <br>
- [Safety guidance](references/safety.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries, structured JSON receipts, optional HTML previews, and shell commands for local redaction, validation, and rendering] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; default behavior generates content only and requires a second explicit confirmation before any message or task is sent.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
