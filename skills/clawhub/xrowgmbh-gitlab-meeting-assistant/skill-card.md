## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction. Use for GitLab Meeting Assistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting participants use this skill to turn explicitly requested feature or bug discussions into sanitized, confidential GitLab issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential meeting details or secrets could be disclosed in a GitLab issue.

Mitigation: Sanitize every authored field and attachment, remove secrets, and inspect the complete outgoing content before each write.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [English GitLab issue titles and descriptions, with acceptance criteria when supported by the discussion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates confidential issues only on explicit request; sanitize authored content and redact secrets before writing.]

## Skill Version(s):

1.144.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
