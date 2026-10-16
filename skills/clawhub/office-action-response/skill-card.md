## Description:

Helps prepare responses to Chinese patent office actions, including a response statement, amended claims, and an amendment comparison table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent applicants, patent teams, and their advisers use the skill to prepare a response to a Chinese patent examination notice from the full notice and application materials. Users choose the response strategy and review any amended claims before the final draft is produced.

### Deployment Geography for Use:

Global (Chinese patent applications only)

## Known Risks and Mitigations:

Risk: Full office-action and patent application materials are sent to PatentMax for processing, potentially including confidential client information.

Mitigation: Check client, firm, or company data-handling requirements and obtain authorization before sending confidential materials.

Risk: A local trial/API key and task records are stored under ~/.patentmax.

Mitigation: Protect access to the local account and stored credentials and records.

Risk: Submitting a response is a paid task, and generated legal documents may need correction before filing.

Mitigation: Confirm the stated fee before submission, review strategy and claims, and have a patent professional check the documents before filing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/office-action-response)
- [Example office action (fictional)](references/demo-office-action.md)
- [Example application (fictional)](references/demo-application.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Response statement in chat and Word (.docx) files for the statement, amended claims when applicable, and amendment comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Users review the strategy and proposed claims unless they explicitly request automatic confirmation.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
