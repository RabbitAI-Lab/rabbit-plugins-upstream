## Description:

ShellMail is a full email client for AI agents via the ShellMail API that can read, search, send, reply, manage mailbox state, retrieve OTPs, and manage ShellMail addresses when explicitly invoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aaronbatchelder](https://clawhub.ai/user/aaronbatchelder)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use ShellMail to give an agent a dedicated ShellMail inbox for account verification, OTP retrieval, search, and controlled email actions without using personal email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ShellMail token grants access to inbox contents, OTP codes, sending, deletion, and address management.

Mitigation: Install only if the user trusts shellmail.ai, use ShellMail for agent-specific mail rather than personal email, and revoke or remove the token when no longer needed.

Risk: Email sending and destructive mailbox actions can affect external recipients or permanently remove mail and addresses.

Mitigation: Review send and delete actions before approving them; destructive commands require explicit confirmation for the specific action.

## Reference(s):

- [ShellMail API and service](https://shellmail.ai)
- [ClawHub skill page](https://clawhub.ai/aaronbatchelder/skills/shellmail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHELLMAIL_TOKEN, curl, python3, and outbound HTTPS access to https://shellmail.ai by default.]

## Skill Version(s):

1.3.1 (source: SKILL.md frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
