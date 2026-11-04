## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting facilitators and project teams use the skill to turn discussed feature and bugfix requests into sanitized, confidential GitLab issues when explicitly asked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive meeting details or credentials could be disclosed in a GitLab issue or attachment.

Mitigation: Anonymize identifying details, remove secrets, and inspect the complete issue payload and attachments before writing; create issues as confidential from the outset.

Risk: Sanitization and confidentiality safeguards depend on the agent and GitLab integration carrying them out correctly.

Mitigation: Use the intended project with appropriately limited access, confirm the integration can set confidentiality, and verify the created issue is confidential.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Sanitized English GitLab issue content and brief status replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issues are created as confidential only after an explicit request and clear project selection.]

## Skill Version(s):

1.128.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
