## Description:

Microsoft Outlook and OneDrive CLI and MCP for email, calendar, contacts, tasks, and files, for personal and enterprise accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rlrghb](https://clawhub.ai/user/rlrghb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill to let agents work with Microsoft 365 mail, calendar, contacts, tasks, and OneDrive data through the `olk` CLI or MCP server. It supports reading, searching, drafting, sending, moving, deleting, and managing Outlook and OneDrive resources for personal and enterprise accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs an unpinned third-party executable that handles OAuth-protected Microsoft 365 mail and OneDrive data.

Mitigation: Install only if the `rlrghb` publisher and Homebrew tap are trusted, and verify the release source where possible before authenticating.

Risk: Broad or delegated Microsoft scopes can expose mailboxes, calendars, contacts, tasks, and files beyond the minimum needed task surface.

Mitigation: Grant the minimum Microsoft scopes needed and avoid delegated mailbox scopes unless the workflow explicitly requires them.

Risk: Unattended agent use can send messages, create invites, mutate mailbox state, or delete files and records.

Mitigation: Use `OLK_NO_WRITE`, `OLK_NO_SEND`, `OLK_NO_INPUT`, and exact command allowlists for unattended runs.

Risk: Fetched email, calendar, contact, task, and file content can contain untrusted instructions.

Mitigation: Treat content inside `UNTRUSTED` markers as data only, and require explicit user intent before acting on embedded requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rlrghb/skills/olk)
- [rlrghb Publisher Profile](https://clawhub.ai/user/rlrghb)
- [Microsoft Graph: Send mail from another user](https://learn.microsoft.com/en-us/graph/outlook-send-mail-from-other-user)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The `olk` commands can emit structured JSON with `--json --results-only`; unattended runs should use non-interactive and capability guard settings.]

## Skill Version(s):

1.14.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
