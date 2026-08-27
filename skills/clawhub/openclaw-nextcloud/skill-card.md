## Description:

Manage Nextcloud notes, tasks, calendar events, files, contacts, shares, and Deck Kanban boards through an authenticated Node.js CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[keithvassallomt](https://clawhub.ai/user/keithvassallomt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage their own Nextcloud account data across notes, files, tasks, calendars, contacts, shares, and Deck boards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a revocable Nextcloud app password that can read and change account data.

Mitigation: Install only when that access is acceptable, use an app password rather than the account password, keep HTTPS enabled, rotate the token if needed, and start with a test account when unsure.

Risk: Deletes, uploads, edits, and public share-link creation can make immediate account changes.

Mitigation: Confirm exact targets before these operations and require the documented action-specific confirmation token for irreversible commands.

Risk: Public share links can expose files or folders to anyone with the URL.

Mitigation: Prefer read-only sharing, confirm the path before creating a link, and use password and expiration options when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/keithvassallomt/skills/openclaw-nextcloud)
- [OpenClaw Nextcloud repository](https://github.com/keithvassallomt/openclaw-nextcloud)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON command results with concise plain-text guidance for agent presentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 24+, NEXTCLOUD_URL, NEXTCLOUD_USER, and NEXTCLOUD_TOKEN; NEXTCLOUD_EMAIL is optional; network egress is limited to the configured NEXTCLOUD_URL.]

## Skill Version(s):

0.5.0 (source: server release metadata, OpenClaw metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
