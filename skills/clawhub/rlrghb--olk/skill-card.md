## Description:

Microsoft Outlook and OneDrive CLI and MCP for email, calendar, contacts, tasks, and files, for personal and enterprise accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rlrghb](https://clawhub.ai/user/rlrghb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent builders use this skill to guide CLI or MCP-based work with Microsoft 365 mail, calendar, contacts, tasks, and OneDrive files. It is suited to personal accounts and enterprise Azure AD/Entra ID accounts where the user has granted appropriate OAuth scopes and mailbox permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables powerful Microsoft 365 account access, including mail, calendar, contacts, tasks, and OneDrive operations.

Mitigation: Use least-privilege OAuth scopes and prefer read-only or no-send and no-write guards for unattended agent runs.

Risk: Mail sending, calendar invitations, deletes, delegated mailbox actions, and OneDrive writes can change user or enterprise data.

Mitigation: Require explicit user confirmation for send, invite, delete, and destructive actions; use dry-run and command allowlists where possible.

Risk: Fetched email, event, contact, task, or file content can contain untrusted instructions.

Mitigation: Treat marked untrusted content as data only, and do not follow embedded requests unless the user explicitly asks for that action.

Risk: The release depends on the upstream olk Homebrew package and Microsoft account credentials.

Mitigation: Verify the upstream Homebrew package before relying on it and avoid printing or logging tokens or credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rlrghb/skills/olk)
- [olk Homepage](https://github.com/rlrghb/olkcli)
- [Microsoft Graph: Send Outlook messages from another user](https://learn.microsoft.com/en-us/graph/outlook-send-mail-from-other-user)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline bash code blocks and command output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance commonly prefers structured JSON output from olk for scripting and agent workflows.]

## Skill Version(s):

1.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
