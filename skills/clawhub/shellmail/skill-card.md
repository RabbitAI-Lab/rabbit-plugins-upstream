## Description:

ShellMail lets an agent manage a ShellMail inbox for reading messages and OTPs, searching mail, sending or replying to email, and managing mailbox state through the ShellMail API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aaronbatchelder](https://clawhub.ai/user/aaronbatchelder)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to give an agent an explicit ShellMail inbox for sign-ups, OTP retrieval, mailbox search, and controlled email sending or replies. It is intended for ShellMail-specific requests, not generic email accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ShellMail token grants access to inbox contents, OTPs, sending, deletion, and address management.

Mitigation: Install only when the user trusts shellmail.ai, use agent-specific or disposable email, and review token-saving configuration before approval.

Risk: Deleting a message or deleting the ShellMail address can irreversibly destroy mail or revoke access.

Mitigation: Require fresh explicit user confirmation for the specific destructive action before using commands that require --confirm.

Risk: The skill can send or reply to email from the user's ShellMail address.

Mitigation: Send mail only when the user explicitly asks, and present the recipient, subject, and body before execution.

Risk: A custom API endpoint could receive the bearer token and mailbox data if misconfigured.

Mitigation: Use the default ShellMail endpoint unless the user intentionally sets a trusted HTTPS endpoint and opts in with SHELLMAIL_ALLOW_CUSTOM_API=1.

## Reference(s):

- [ClawHub ShellMail skill page](https://clawhub.ai/aaronbatchelder/skills/shellmail)
- [ShellMail service and API endpoint](https://shellmail.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with inline bash commands; command results are JSON or text from the ShellMail API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHELLMAIL_TOKEN; outbound network access is limited to https://shellmail.ai unless the user explicitly opts in to a trusted custom HTTPS endpoint.]

## Skill Version(s):

1.3.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
