## Description:

Connect to personal Microsoft accounts via Microsoft Graph API to manage email, calendar events, and tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danielithomas](https://clawhub.ai/user/danielithomas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use OfficeClaw to connect an OpenClaw agent to a personal Microsoft account for Outlook mail, calendar, and Microsoft To Do workflows. It supports reading and managing mailbox content, creating or updating calendar events, and listing or updating tasks after OAuth setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs an external package that can handle sensitive Microsoft email, calendar, task, token, and attachment data.

Mitigation: Use a pinned, trusted OfficeClaw release, grant only the Microsoft Graph scopes needed, and confirm which package version provides the documented v1.1.0+ protections.

Risk: Agent-driven send or delete operations can affect real mailbox, calendar, and task data.

Mitigation: Keep send and delete disabled unless required, enable them only through explicit environment gates, and confirm destructive actions before execution.

Risk: Outbound email or attachment handling can expose files or messages beyond the intended workflow.

Mitigation: Configure recipient and attachment-directory allowlists before enabling agent-driven sends or attachment handling.

## Reference(s):

- [OfficeClaw ClawHub listing](https://clawhub.ai/danielithomas/skills/officeclaw)
- [OfficeClaw on GitHub](https://github.com/danielithomas/officeclaw)
- [OfficeClaw on PyPI](https://pypi.org/project/officeclaw/)
- [Microsoft Graph API](https://docs.microsoft.com/graph/)
- [Microsoft identity platform app registration guide](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)
- [OpenClaw documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can surface Microsoft Graph data through OfficeClaw CLI output; JSON mode wraps successes and failures in a status envelope.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
