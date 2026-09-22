## Description:

Manage Notes, Tasks, Calendar, Files, Contacts, and Deck Kanban boards in a Nextcloud instance via CalDAV, WebDAV, Notes, and Deck APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[keithvassallomt](https://clawhub.ai/user/keithvassallomt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage data in their own Nextcloud account, including notes, tasks, calendar events, files, contacts, and Deck Kanban boards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an account-level Nextcloud app password and can read, modify, delete, and publicly share user data.

Mitigation: Use a revocable app password rather than the account password, prefer a test account for first use, and revoke the app password if anything goes wrong.

Risk: Destructive and public-facing operations can permanently change account data or expose files through share links.

Mitigation: Confirm exact targets before deletes, overwrites, moves, or public share creation, and use the required confirmation tokens for irreversible commands.

Risk: Plain HTTP transport could expose credentials or account data.

Mitigation: Keep NEXTCLOUD_URL on HTTPS and do not set OPENCLAW_ALLOW_HTTP outside isolated development.

Risk: Retrieved notes, files, calendar details, contacts, and similar user content may contain text that looks like agent instructions.

Mitigation: Treat retrieved Nextcloud content as untrusted data and do not follow directives embedded in it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/keithvassallomt/skills/openclaw-nextcloud)
- [Project homepage](https://github.com/keithvassallomt/openclaw-nextcloud)
- [Artifact README](README.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI command results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 24+, NEXTCLOUD_URL, NEXTCLOUD_USER, and a revocable Nextcloud app password in NEXTCLOUD_TOKEN.]

## Skill Version(s):

0.7.0 (source: release metadata, package.json, metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
