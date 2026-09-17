## Description:

Push by Techulus (push.techulus.com). Use this skill for ANY Push by Techulus request - reading, creating, and updating data. Whenever a task involves Push by Techulus, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Push by Techulus through an OOMOL-connected account, including sending notifications to device groups or all devices targeted by the account or team API key. The skill guides agents to inspect live connector schemas before constructing payloads and to confirm write actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags first-time setup guidance that pipes remote installer scripts directly into a shell.

Mitigation: Review setup commands before installation and prefer documented, versioned, and verifiable oo CLI installation methods.

Risk: Notification actions change Push by Techulus state by sending messages to users or device groups.

Mitigation: Confirm the exact notification payload and intended target with the user before running write actions.

## Reference(s):

- [Push by Techulus homepage](https://push.techulus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector schema and run commands; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
