## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Planning meeting participants use the agent to capture discussed feature and bug requests as sanitized, confidential GitLab issues when they explicitly ask. It helps organize issue details and gives brief status replies without implementing the requested changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If sanitization is not enforced at runtime, meeting details or secrets could be written to a GitLab issue.

Mitigation: Review the complete issue content and attachments for identifiers and secrets, and verify the selected project and confidential setting before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Text, Guidance, GitLab issue content]

**Output Format:** [English GitLab issue titles and descriptions, with concise conversational replies in the requester's chosen language]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue creation requires an explicit request and a clearly selected project; meeting content is sanitized and issues are created as confidential.]

## Skill Version(s):

1.125.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
