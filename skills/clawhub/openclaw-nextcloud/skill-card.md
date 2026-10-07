## Description:

Connects an agent to a Nextcloud account to manage notes, tasks, calendars, files, contacts, and Deck Kanban boards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[keithvassallomt](https://clawhub.ai/user/keithvassallomt)

### License/Terms of Use:

MIT-0

## Use Case:

Nextcloud users and their agents can organize notes, tasks, calendars, files, contacts, and Kanban boards through a connected Nextcloud account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An app password gives access to the full Nextcloud account.

Mitigation: Use a dedicated, revocable Nextcloud app password rather than the main account password.

Risk: Deletes, edits, and uploads can change or remove account data.

Mitigation: Review the exact target and operation with the user before approving changes or supplying confirmation tokens.

Risk: Public share links can expose files to anyone with the link.

Mitigation: Confirm the file and permissions before sharing; prefer read-only links with a password or expiration where appropriate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/keithvassallomt/skills/openclaw-nextcloud)
- [Project homepage (declared in skill metadata)](https://github.com/keithvassallomt/openclaw-nextcloud)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Plain-language responses and JSON results from Nextcloud commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands that delete data or create public links require explicit confirmation.]

## Skill Version(s):

0.7.2 (source: ClawHub release, skill metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
