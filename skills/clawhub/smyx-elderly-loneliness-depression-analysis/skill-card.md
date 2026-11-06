## Description:

Analyzes video from fixed cameras in older adults’ homes to identify behaviors associated with loneliness or depressive tendencies and support caregiver follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Family members and community care workers use the skill to review behavior summaries and risk reminders from older adults’ home videos, helping them decide when to check in or arrange support. It also retrieves prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home videos may be uploaded even when the no-analysis option is used.

Mitigation: Obtain consent that covers third-party uploads, and confirm export-only behavior and API destination controls before using private footage.

Risk: Cloud access tokens may be stored in a shared local database.

Mitigation: Require protected token storage and disabled HTTP wire logging; confirm the provider’s retention and report-access policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)
- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured behavior analysis reports and Markdown history lists with risk summaries, reminders, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports describe observed behavior and risk indicators; they are not medical diagnoses or psychological scale scores.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
