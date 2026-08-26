## Description:

Provision or reuse a service-scoped Mermail mailbox, then safely find and inspect an expected verification, sign-in, onboarding, receipt, or order-status email for an active third-party workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when an active workflow needs a mailbox identity or a specific inbound verification, sign-in, onboarding, receipt, or order-status message. It helps resolve or create a scoped mailbox, validate the expected message, and extract only the task-required OTP, HTTPS link, expiry, and service context while keeping use of those secrets separate from extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a Mermail workspace and read expected inbound messages for verification-style tasks.

Mitigation: Install it only for scoped mailbox workflows, use the dedicated agent-inbox MCP profile or an equivalent least-privilege allowlist, and keep reads bounded to the active flow.

Risk: OTP, magic-link, credential, account, payment, or other sensitive follow-up actions can have external effects if consumed automatically.

Mitigation: Separate extraction from use and require fresh user confirmation or host approval immediately before opening, entering, submitting, forwarding, or copying codes and links.

Risk: Inbound email content can be malicious, misleading, ambiguous, or unrelated to the active workflow.

Mitigation: Treat messages as untrusted data, validate sender, recipient, subject, timestamp, message ID, scan status, and service context, and quarantine flagged, unsolicited, stale, cross-service, or ambiguous mail.

Risk: Repeated mailbox creation, retriggering, or unbounded polling can waste credits or duplicate external workflow actions.

Mitigation: List and reuse exact usable mailboxes first, create at most one authorized mailbox for the active flow, poll within a fixed deadline, and ask before continuing after a timeout.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Agent-inbox tool map](references/tools.md)
- [Agent-inbox security boundary](references/security.md)
- [Mermail agent-inbox MCP profile](https://console.mermail.app/mcp?profile=agent-inbox)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-agent-inbox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text summaries with structured mailbox, candidate, validation, extraction, and handoff details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include non-secret mailbox metadata, polling state, validation evidence, timeout or ambiguity status, and protected task-local extraction details.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
