## Description:

Manage Notes, Tasks, Calendar, Files, Contacts, and Deck Kanban boards in a Nextcloud instance via CalDAV, WebDAV, Notes, and Deck APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[keithvassallomt](https://clawhub.ai/user/keithvassallomt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Nextcloud notes, tasks, calendars, files, contacts, shares, and Deck Kanban boards from a configured account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives the agent broad Nextcloud account-level access, including read, write, delete, and public-share capabilities.

Mitigation: Install only with a revocable Nextcloud app password, prefer a test account first, and revoke the app password if activity looks wrong.

Risk: Public share links can expose files or folders to anyone with the URL, and editable links can allow modification or deletion.

Mitigation: Confirm public shares carefully, prefer read-only links, and use passwords and expiry dates for shared links.

Risk: Destructive operations can make immediate, non-transactional changes to notes, files, tasks, calendars, contacts, shares, boards, stacks, cards, or labels.

Mitigation: Confirm the exact target before destructive actions and rely on the skill's action-specific confirmation tokens where required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/keithvassallomt/skills/openclaw-nextcloud)
- [OpenClaw Nextcloud homepage](https://github.com/keithvassallomt/openclaw-nextcloud)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON command output with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 24+ and NEXTCLOUD_URL, NEXTCLOUD_USER, and NEXTCLOUD_TOKEN; network egress is to NEXTCLOUD_URL.]

## Skill Version(s):

0.6.0 (source: server release metadata, OpenClaw metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
