## Description:

This skill helps teams plan, run, and review meetings using a scientific meeting methodology, Tencent Meeting tmeet commands, ROI reporting, and Feishu Bitable task tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1027399464-tech](https://clawhub.ai/user/1027399464-tech)

### License/Terms of Use:

MIT-0

## Use Case:

Teams, operators, managers, and agents use this skill to prepare structured Tencent Meeting sessions, capture meeting outcomes, calculate meeting ROI, and turn decisions into Feishu Bitable task-board records for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can drive Tencent Meeting actions that create, cancel, invite, remove, kick, call, or sign out users.

Mitigation: Show operation details and require explicit user confirmation before any sensitive Tencent Meeting write action.

Risk: The Feishu Bitable integration uses app credentials and local configuration or token-cache files.

Mitigation: Review Feishu app permissions before use, keep ~/.config credential files private, and avoid printing access tokens or secrets.

Risk: Task-board writes can create or update operational records in Feishu.

Mitigation: Review generated task records and confirm the target Bitable URL and table before add, batch, or update operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/1027399464-tech/skills/scientific-meeting)
- [Feishu OpenAPI base](https://open.feishu.cn/open-apis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON task examples, and Python helper-script usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce meeting agendas, structured minutes, ROI summaries, decision/task tables, Feishu Bitable task records, and confirmation-gated command suggestions.]

## Skill Version(s):

3.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
