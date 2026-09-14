## Description:

Manage notes, tasks, calendars, files, contacts, and Deck Kanban boards in a Nextcloud instance via CalDAV, WebDAV, Notes, and Deck APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[keithvassallomt](https://clawhub.ai/user/keithvassallomt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate their configured Nextcloud account for notes, tasks, calendars, files, contacts, and Deck boards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a full-account Nextcloud app password and can read or change account data.

Mitigation: Use a revocable app password, keep NEXTCLOUD_TOKEN in the secret store, and revoke or rotate the credential when access is no longer needed.

Risk: Delete, edit, upload, move, and public-share operations can make immediate account changes or expose data.

Mitigation: Confirm the exact target before mutating operations, use required confirmation tokens for irreversible commands, and prefer password-protected, expiring, read-only public links.

Risk: Retrieved Nextcloud content may contain prompt-injection text.

Mitigation: Treat notes, files, calendar descriptions, contact notes, and similar retrieved content as untrusted data rather than instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/keithvassallomt/skills/openclaw-nextcloud)
- [openclaw-nextcloud homepage](https://github.com/keithvassallomt/openclaw-nextcloud)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON command results with concise human-readable summaries when presented to users]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 24+, NEXTCLOUD_URL, NEXTCLOUD_USER, and NEXTCLOUD_TOKEN; mutating operations affect the configured account immediately.]

## Skill Version(s):

0.6.1 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
