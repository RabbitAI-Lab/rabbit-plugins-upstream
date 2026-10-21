## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction. Use for GitLab Meeting Assistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting facilitators and teams use this assistant to turn explicitly requested feature and bug reports into sanitized, confidential GitLab issues in the project selected for the meeting. It asks for clarification only when the requested action, content, or destination is too ambiguous to proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting details or credentials could be exposed if sensitive content survives sanitization.

Mitigation: Inspect the complete proposed issue content and attachments for identifiers and secrets before each write; omit content that cannot be safely sanitized.

Risk: An issue could be written to the wrong project or lack the intended confidentiality.

Mitigation: Use the explicitly selected project with a GitLab connection scoped to it, create issues as confidential, and verify the returned confidentiality status.

## Reference(s):

- [GitLab Meeting Assistant on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [English GitLab issue titles, descriptions, acceptance criteria, and comments, plus concise chat replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authored issue content is sanitized; issues are confidential and created only on explicit instruction.]

## Skill Version(s):

1.115.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
