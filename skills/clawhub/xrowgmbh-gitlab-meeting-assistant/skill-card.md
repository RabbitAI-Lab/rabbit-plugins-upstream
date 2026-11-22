## Description:

Captures sanitized feature and bug requests as GitLab issues during planning meetings when explicitly asked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Planning teams use it to turn explicitly requested feature and bug discussions into English, sanitized, confidential GitLab issues in the project they select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had partial coverage, so some referenced material may not have been reviewed.

Mitigation: Review referenced material that was outside the scan before relying on it.

Risk: English-only GitLab content may not suit every meeting's language needs.

Mitigation: Review the English issue draft with the requester before creating it when language fit is uncertain.

Risk: Meeting content may contain identifying details or secrets that should not be written to an issue.

Mitigation: Anonymize identifying details, remove secrets, and inspect the complete issue payload before each write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [English Markdown issue content and brief conversational replies; confidential GitLab issue records when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue creation requires an explicit request and a selected project; issue content is sanitized before writing.]

## Skill Version(s):

1.151.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
