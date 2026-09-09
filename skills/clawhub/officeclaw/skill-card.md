## Description:

Connect to personal Microsoft accounts via Microsoft Graph API to manage email, calendar events, and tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danielithomas](https://clawhub.ai/user/danielithomas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use OfficeClaw to let an agent work with a personal Microsoft account for Outlook mail, calendar scheduling, and Microsoft To Do task management through Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Microsoft account email, calendar, task, and attachment data through Microsoft Graph.

Mitigation: Install in a dedicated environment, grant only the Microsoft Graph scopes required for the intended workflow, and keep account access scoped to the user's needs.

Risk: Send and delete operations can disclose information, contact unintended recipients, or change mailbox, calendar, and task state.

Mitigation: Keep send and delete disabled unless required, require user confirmation for destructive or outbound actions, and configure recipient allowlists before enabling outbound mail or calendar invitations.

Risk: Attachment handling can read local files for outbound mail or write downloaded files to disk.

Mitigation: Configure allowed attachment directories, safe sender checks, file size and type controls, and destination restrictions before allowing an agent to send or download attachments.

Risk: OAuth tokens provide ongoing account access if mishandled.

Mitigation: Protect the token cache, run the skill under a dedicated user environment, refresh or revoke access when needed, and avoid logging private message or calendar content.

## Reference(s):

- [OfficeClaw ClawHub page](https://clawhub.ai/danielithomas/skills/officeclaw)
- [OfficeClaw project homepage](https://github.com/danielithomas/officeclaw)
- [OfficeClaw on PyPI](https://pypi.org/project/officeclaw/)
- [Microsoft Graph API](https://docs.microsoft.com/graph/)
- [Microsoft app registration guide](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)
- [OpenClaw documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to use the officeclaw CLI, JSON mode, OAuth setup, allowlists, and safety gates.]

## Skill Version(s):

1.1.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
