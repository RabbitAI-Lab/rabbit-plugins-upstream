## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Teams use this skill during planning meetings to turn explicitly requested feature or bug discussions into concise, sanitized, confidential GitLab issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external GitLab integration may not support confidential issues or may not expose confidentiality for verification, and meeting content may contain sensitive details.

Mitigation: Confirm the integration can set confidentiality and verify it on the returned issue; do not create the issue if confidentiality cannot be set. Remove identifying details and secrets from all authored content and attachments before writing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [English GitLab issue titles and descriptions in Markdown, plus brief conversational replies.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue creation requires an explicit request and selected project; authored issue content is sanitized and confidential.]

## Skill Version(s):

1.127.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
