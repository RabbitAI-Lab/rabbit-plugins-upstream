## Description:

Office 365 / Outlook connector for email (read/send), calendar (read/write), and contacts (read/write) using resilient OAuth authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[offthericta](https://clawhub.ai/user/offthericta)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, consultants, and developers use this skill to connect an agent to Microsoft 365 mail, calendar, and contacts across one or more authenticated accounts. It supports reading and sending mail, viewing calendar events, cancelling events, and managing account authentication through Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Microsoft Graph delegated permissions, including read/write access to mail, calendars, contacts, permission to send mail, and offline refresh access.

Mitigation: Grant only the reduced Azure permission set needed for the features in use, review consent before installation, and revoke the Azure app if access is no longer needed.

Risk: Local account configuration and OAuth tokens can expose Microsoft 365 access if files under ~/.openclaw/auth are disclosed.

Mitigation: Keep the auth directory private, preserve owner-only file permissions, avoid committing credentials or token files, rotate client secrets, and revoke tokens or the Azure app after suspected exposure.

Risk: Send-mail and calendar write operations can make user-visible changes as the authenticated Microsoft account.

Mitigation: Use separate accounts or least-privilege app registrations for different workflows, review commands before execution, and monitor Microsoft Entra sign-in and Graph activity logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/offthericta/skills/office365-connector)
- [Microsoft Graph Azure App Registration Setup Guide](artifact/references/setup-guide.md)
- [Microsoft Graph Permissions Reference](artifact/references/permissions.md)
- [Multi-Account Guide](artifact/MULTI-ACCOUNT.md)
- [Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Auth Concepts](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)
- [Microsoft Graph Throttling Guidance](https://learn.microsoft.com/en-us/graph/throttling)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal text with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes Node.js scripts that call Microsoft Graph after local OAuth configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
