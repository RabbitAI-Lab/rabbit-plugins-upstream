## Description:

常见办公流程自动化处理 - 智能办公助手，支持文档处理、数据整理、邮件管理、日程安排、报表生成等

This skill is ready for commercial/non-commercial use.

## Publisher:

[wensen2024](https://clawhub.ai/user/wensen2024)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and office teams use this skill to automate common office workflows such as document generation, spreadsheet cleanup, bulk email preparation, scheduling, report generation, and workflow coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive business data may be processed across documents, spreadsheets, finance records, HR files, or email content.

Mitigation: Use explicit file paths and least-privilege access, keep backups, and require a preview before modifying or distributing outputs.

Risk: Bulk email, content publishing, and automated distribution can create unintended external actions.

Mitigation: Require draft mode, explicit recipient lists, and human approval before sending, publishing, or distributing generated materials.

Risk: SMTP credentials and business-system access could be exposed or misused if configured broadly.

Mitigation: Store credentials outside prompts, scope accounts to the minimum needed permissions, and review configuration before use in a work environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wensen2024/skills/office-automation-pro)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with command snippets, configuration examples, and task execution summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe generated office files, cleaned data, scheduled actions, email drafts, or reports depending on the requested workflow.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
