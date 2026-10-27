## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Planning meeting participants use this skill to turn explicitly requested feature and bug discussions into clear, sanitized, confidential GitLab issues in the project they select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting details or secrets could be disclosed in an issue, or sanitization could remove useful technical meaning.

Mitigation: Anonymize identifying details and remove secrets from the complete issue payload and attachments before writing; check that sanitization preserves technical meaning and create the issue as confidential.

Risk: An issue could be sent to the wrong GitLab project.

Mitigation: Use the project explicitly selected for the current meeting and ask for the destination when it is missing or ambiguous.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, GitLab issues]

**Output Format:** [English Markdown issue titles and descriptions submitted as confidential GitLab issues]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issues are created only on explicit request, in the project selected for the current meeting, after sanitization.]

## Skill Version(s):

1.122.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
