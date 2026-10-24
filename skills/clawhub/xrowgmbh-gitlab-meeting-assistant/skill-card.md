## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to capture planning-meeting feature requests and bug reports as sanitized, confidential GitLab issues when a user explicitly asks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting notes may contain confidential information, personal details, or secrets.

Mitigation: Anonymize identifying details, remove secrets, review every draft before writing, and create the issue as confidential from the outset; verify its confidentiality afterward.

Risk: An incorrect or ambiguous destination could expose meeting content to the wrong project.

Mitigation: Use only the project explicitly selected for the current meeting, ask when it is missing or ambiguous, and use an appropriately scoped GitLab integration.

Risk: Quoted requests or commands embedded in meeting transcripts could be mistaken for authorization to create an issue.

Mitigation: Create an issue only after a clear, explicit instruction addressed to the assistant in the current user conversation.

## Reference(s):

- [GitLab Meeting Assistant on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)
- [Publisher profile: xrowgmbh](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [English GitLab issue titles and Markdown descriptions, with concise status or clarification text.]

**Output Parameters:** [Meeting discussion, an explicit issue-creation request, and the selected GitLab project.]

**Other Properties Related to Output:** [Creates confidential issues only on explicit request; sanitizes sensitive details and verifies the resulting issue's confidentiality.]

## Skill Version(s):

1.118.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
