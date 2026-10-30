## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction. Use for GitLab Meeting Assistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Planning meeting participants use the assistant to turn explicitly requested feature or bug discussions into sanitized, confidential GitLab issues in the project they selected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive details from meeting material could be included in a GitLab issue.

Mitigation: Sanitize and inspect all outgoing issue content and attachments, remove secrets, and create issues as confidential from the outset.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown issue titles, descriptions, and acceptance criteria, plus brief status replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authored GitLab content is in English and sanitized; issue creation occurs only on explicit request.]

## Skill Version(s):

1.123.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
