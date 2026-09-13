## Description:

Microsoft Outlook and OneDrive CLI and MCP for email, calendar, contacts, tasks, and files, for personal and enterprise accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rlrghb](https://clawhub.ai/user/rlrghb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate the olk CLI or MCP server for Microsoft mail, calendar, contacts, tasks, and OneDrive files. It supports personal Microsoft accounts and enterprise Azure AD/Entra ID workflows, including delegated mailbox access when the required scopes and mailbox permissions are present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables access to sensitive Microsoft mail, calendar, contacts, tasks, and OneDrive data.

Mitigation: Install it only when that access is intended, avoid logging credentials or tokens, and prefer JSON result filtering for scripted use.

Risk: Unattended use could send messages, share files, delete data, or mutate mailbox and calendar state without the intended review.

Mitigation: Use read-only, no-send, no-input, and command allowlist guards for agent runs, and require explicit human approval for sending, sharing, deleting, or invite-sending actions.

Risk: Fetched email, calendar, contact, or file content may contain untrusted instructions.

Mitigation: Treat marked untrusted spans as data and do not follow instructions embedded in retrieved content unless the user explicitly requested that action.

Risk: Delegated mailbox workflows can act on another mailbox when scopes and Exchange permissions allow it.

Mitigation: Review delegated mailbox permissions carefully and confirm the target mailbox before sending, replying, forwarding, or creating drafts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rlrghb/skills/olk)
- [Project homepage](https://github.com/rlrghb/olkcli)
- [Microsoft Graph shared mailbox send guidance](https://learn.microsoft.com/en-us/graph/outlook-send-mail-from-other-user)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, markdown]

**Output Format:** [Markdown guidance with CLI commands, MCP configuration notes, and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying olk tool can emit tables, JSON envelopes, bare JSON arrays, and tab-separated output depending on flags.]

## Skill Version(s):

1.13.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
