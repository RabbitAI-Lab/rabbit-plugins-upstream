## Description:

Help users draft and, when authorized, submit feedback to volcengine/volcengine-skills: skill problems, missing capabilities, cloud scenarios, and successful Agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud practitioners use this skill to turn real Volcengine Agent experiences into concise, sanitized feedback drafts for review and optional public submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feedback may be posted publicly if the user approves publication.

Mitigation: Show a compact preview of the exact content and destination, then require explicit user authorization before publishing.

Risk: Feedback drafts can accidentally include secrets, account identifiers, private endpoints, customer data, logs, or confidential business details.

Mitigation: Redact sensitive details before any issue search, URL prefill, attachment, or submission, and ask the user to review the preview before publication.

Risk: Public issues are not an appropriate channel for security vulnerabilities or suspected credential exposure.

Mitigation: Avoid publishing exploit details or exposed credentials and direct active incidents to official support or the project's available private security reporting channel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-feedback)
- [Feedback form](https://github.com/volcengine/volcengine-skills/issues/new?template=feedback.yml)
- [Community and privacy guidance](https://github.com/volcengine/volcengine-skills/blob/main/.github/FEEDBACK_GUIDELINES.md)
- [GitHub Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a sanitized feedback preview and optional publication guidance; public submission requires explicit user approval.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
