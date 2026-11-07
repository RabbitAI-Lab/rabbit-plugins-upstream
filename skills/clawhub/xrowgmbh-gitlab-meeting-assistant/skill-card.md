## Description:

Captures features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Teams can use this assistant during planning meetings to turn explicitly requested feature and bug reports into sanitized, confidential GitLab issues for the selected project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting notes or attached material could disclose confidential details or credentials in an issue.

Mitigation: Sanitize all authored content and attachments, remove secrets, inspect the complete payload, and create issues as confidential.

Risk: Ideas, quoted commands, or ambiguous requests could be mistaken for authorization to create an issue.

Mitigation: Create an issue only after a clear, explicit instruction in the current conversation, and clarify missing or ambiguous content or project selection.

## Reference(s):

- [GitLab Meeting Assistant on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Guidance, GitLab issue content]

**Output Format:** [Concise conversational text and structured issue content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates confidential issues only on explicit request.]

## Skill Version(s):

1.130.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
