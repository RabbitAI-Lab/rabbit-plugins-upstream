## Description:

Manage disposable email addresses using GuerrillaMail for creating temporary or throwaway addresses, checking inboxes, and avoiding sharing a real email with untrusted services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cprite](https://clawhub.ai/user/cprite)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use DropMail to generate disposable email addresses, refresh and inspect GuerrillaMail inboxes, and remove cached mailbox state after use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disposable-mail traffic is routed through GuerrillaMail, and messages may contain verification codes, login links, or other sensitive content.

Mitigation: Do not use the disposable inbox for sensitive account recovery, financial, medical, or long-lived login flows.

Risk: Inbox contents and per-email session cookies are cached under ~/.dropmail.

Mitigation: Treat the local database and sessions file as sensitive, keep file permissions private, and remove disposable addresses when finished.

Risk: A system-wide symlink install can be unsafe if the source directory is writable by less-trusted users.

Mitigation: Prefer a user-local install, or ensure any system-wide installed copy is root-owned and not writable by less-trusted users.

Risk: Email content displayed in the terminal is untrusted.

Mitigation: Treat displayed messages as untrusted content and review links or instructions carefully before acting on them.

## Reference(s):

- [GuerrillaMail API Reference](references/api.md)
- [Server-resolved source repository](https://github.com/cprite/dropmail)
- [ClawHub skill page](https://clawhub.ai/cprite/skills/dropmail)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.7+ and stores mailbox state locally under ~/.dropmail.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
