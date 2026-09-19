## Description:

Microsoft Outlook and OneDrive CLI and MCP for email, calendar, contacts, tasks, and files, for personal and enterprise accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[offthericta](https://clawhub.ai/user/offthericta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and agents use this skill to operate Microsoft Outlook, calendar, contacts, tasks, and OneDrive through the olk CLI or MCP server. It supports personal Microsoft accounts and enterprise Azure AD or Entra ID accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Homebrew install points to an external, unpinned olk CLI that can access or modify Microsoft 365 mail, calendar, contacts, tasks, and files.

Mitigation: Install only from a trusted olk tap and project maintainer, review the installed CLI release separately, and use least-privilege OAuth scopes.

Risk: Unattended or agent-driven use could send mail, create meeting invites, modify data, or delete resources.

Mitigation: Use OLK_NO_WRITE=1 and OLK_NO_SEND=1 for read-only operation, keep OLK_NO_INPUT=1 for headless runs, and avoid --force unless the user explicitly intends the action.

Risk: Fetched email, event, contact, or file content may contain untrusted instructions.

Mitigation: Treat content wrapped in untrusted markers as data only and require an explicit user request before acting on embedded requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/offthericta/skills/olk)
- [olk project homepage](https://github.com/rlrghb/olkcli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents toward JSON, tabular, or plain-text olk command output depending on selected CLI flags.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
