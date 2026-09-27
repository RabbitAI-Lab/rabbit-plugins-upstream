## Description:

Manage notes, tasks, calendars, files, contacts, and Deck Kanban boards in a Nextcloud instance through an agent-guided command-line integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[keithvassallomt](https://clawhub.ai/user/keithvassallomt)

### License/Terms of Use:

MIT-0

## Use Case:

Nextcloud users and their agents use this skill to retrieve and manage account notes, tasks, events, files, contacts, and Kanban boards, including creating public file shares when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An app password grants full Nextcloud account-level access if exposed or misused.

Mitigation: Use a revocable app password rather than the account password, try a test account first, and keep the token out of prompts and logs.

Risk: Edits, uploads, and deletions can change or permanently remove account data without a preview or undo.

Mitigation: Confirm the exact target and operation with the user before making changes; supply required confirmation tokens only after approval.

Risk: Public share links can expose files, and editable links can allow others to change them.

Mitigation: Confirm the shared path and permissions; prefer read-only links with a password and expiration.

Risk: Retrieved Nextcloud content may contain instructions intended to redirect the agent.

Mitigation: Treat retrieved notes, files, and descriptions as untrusted data, not as instructions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/keithvassallomt/skills/openclaw-nextcloud)
- [Project homepage (listed in skill metadata)](https://github.com/keithvassallomt/openclaw-nextcloud)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell commands; command results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 24+, access to a Nextcloud instance, and an account-level app password.]

## Skill Version(s):

0.7.1 (source: ClawHub release, skill metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
