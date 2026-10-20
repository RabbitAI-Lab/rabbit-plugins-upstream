## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Planning-meeting participants use the skill to turn explicitly requested feature and bug discussions into sanitized, confidential GitLab issues in the project selected for that meeting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting details or secrets could be disclosed through GitLab issue content or attachments.

Mitigation: Sanitize and review the complete outgoing content and attachments before each write; omit anything that cannot be sanitized safely.

Risk: An issue could be created without the intended confidentiality setting if the integration cannot set or verify it.

Mitigation: Do not create the issue unless confidentiality can be set, and verify the returned issue is confidential before reporting success.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [English-language GitLab issue content in Markdown and concise status replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sanitized work-item content; issue creation only on explicit request.]

## Skill Version(s):

1.114.1 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
