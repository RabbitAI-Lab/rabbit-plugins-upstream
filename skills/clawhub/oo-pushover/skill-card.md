## Description:

Provides Pushover operations for reading, creating, updating, and deleting notifications and related account data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Pushover notifications and account objects through an OOMOL-connected Pushover account. It supports sending notifications, managing groups and team users, inspecting receipts and limits, and handling Open Client flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose application or Team API tokens and can persist a Team API token.

Mitigation: Avoid token-returning or token-storing actions unless credential administration is explicitly required, and review outputs for secrets before sharing or logging them.

Risk: Some untagged actions are described as safe reads even though authentication and token-related actions can handle sensitive credentials.

Mitigation: Treat authentication, token retrieval, and token storage actions as sensitive even when they are not labeled write or destructive.

Risk: The setup instructions document installing the oo CLI by piping a remote script into a shell.

Mitigation: Install the oo CLI through a verifiable method, such as reviewing the install guide or script before execution.

Risk: Write and destructive actions can modify Pushover groups, users, licenses, receipts, devices, and notifications.

Mitigation: Confirm the exact action, target, and payload with the user before running write or destructive commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pushover)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Pushover Homepage](https://pushover.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the Pushover connector through the oo CLI and may return JSON responses, base64 image content, or execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
