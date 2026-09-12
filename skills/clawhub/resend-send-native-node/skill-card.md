## Description:

Send email via Resend.com's HTTPS API - native Node.js, zero dependencies. Use when the user explicitly asks to email, send a message, mail a report, or deliver a notification to an email address. Externally sends email only with --send; defaults to dry-run and requires RESEND_ALLOWED_TO allowlist for real sends. Requires RESEND_API_KEY in the process environment for real sends. No OAuth, no 2FA, no Gmail required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jwestburg](https://clawhub.ai/user/jwestburg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to prepare and, after explicit approval, send outbound email through Resend. It is intended for reviewed notifications and report-style messages, not inbox reading or unreviewed disclosure of private workspace context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send external email when real-send gates are satisfied.

Mitigation: Review dry-run output first and approve real sends only after confirming the exact recipients, sender, reply-to, subject, and body.

Risk: A broadened recipient allowlist could permit delivery beyond the intended approval scope.

Mitigation: Keep RESEND_ALLOWED_TO operator-controlled and change it only after explicit approval for the exact recipient set.

Risk: Generated email content may include private logs, transcripts, memory, or workspace context if approved without review.

Mitigation: Send only curated, reviewed message text and avoid unfiltered private context in outbound email.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jwestburg/skills/resend-send-native-node)
- [Resend](https://resend.com)
- [Resend domains](https://resend.com/domains)
- [Resend pricing](https://resend.com/pricing)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON receipts, with Markdown usage guidance and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run is the default. Real sends require --send, RESEND_API_KEY, and an operator-controlled RESEND_ALLOWED_TO recipient allowlist.]

## Skill Version(s):

1.0.20 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
