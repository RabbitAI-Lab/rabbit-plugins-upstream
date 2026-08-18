## Description:

Provision or reuse a service-scoped Mermail mailbox, then safely find and inspect an expected verification, sign-in, onboarding, receipt, or order-status email for an active third-party workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to provide a task-scoped Mermail email identity, poll for the expected transactional message, and extract only the active workflow's needed code, link, receipt, or status detail. It is intended for active verification, sign-in, onboarding, receipt, and order-status workflows that require bounded email handling and fresh approval before using sensitive content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles OTPs, magic links, and transactional mailbox content that could enable account access or external actions.

Mitigation: Keep extracted secrets in protected task-local context and require fresh confirmation or host approval immediately before opening, entering, submitting, forwarding, or copying them.

Risk: Inbound email may contain malicious links, prompt injection, misleading sender information, or unsafe attachments.

Mitigation: Treat all message content as untrusted, use sanitized bounded text, reject suspicious or non-clean messages, and keep attachments metadata-only unless the active task and scanner bounds permit inspection.

Risk: A stale, ambiguous, held, or cross-service message could be mistaken for the active workflow's expected email.

Mitigation: Validate exact mailbox, recipient, sender or approved domain, subject, timestamp, and non-baseline message ID; stop as pending, ambiguous, quarantined, or timed out when the evidence is insufficient.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-agent-inbox)
- [Agent-inbox tool map](references/tools.md)
- [Agent-inbox security boundary](references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text summaries with protected task-local extraction details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports mailbox reuse or provisioning status, bounded polling results, candidate evidence, validation state, protected OTP or link readiness, and remaining user approval steps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
