## Description:

Manage disposable email addresses using GuerrillaMail for temporary address creation, disposable inbox checks, and avoiding use of a real email with untrusted services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cprite](https://clawhub.ai/user/cprite)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create temporary email addresses, refresh and read disposable inboxes, and clean up local mailbox state when testing or interacting with untrusted services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disposable inbox traffic is routed through GuerrillaMail, which can see received messages.

Mitigation: Do not use the skill for sensitive account recovery, financial, medical, or long-lived login flows.

Risk: Received messages and mailbox session cookies are stored locally under ~/.dropmail/.

Mitigation: Treat the local database and session file as sensitive, remove disposable addresses when done, and rely on the documented private file permissions.

Risk: A system-wide command installed from a mutable symlink could execute later local changes.

Mitigation: Prefer the user-local install path, or install a root-owned copy for system-wide use as documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cprite/skills/dropmail)
- [Server-resolved source repository](https://github.com/cprite/dropmail)
- [Server-resolved source commit](https://github.com/cprite/dropmail/commit/c0b2397c417e6348ef5fcd8abc7152657b238472)
- [GuerrillaMail API reference](references/api.md)
- [GuerrillaMail API endpoint](https://api.guerrillamail.com/ajax.php)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance and plain text CLI output with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI execution can create local SQLite and session files under ~/.dropmail/.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
