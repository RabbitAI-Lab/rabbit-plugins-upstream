## Description:

Operate Svix through an OOMOL-connected account to inspect schemas and manage applications, endpoints, event types, and messages with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Svix webhook infrastructure from an agent session, including reading account data, creating or updating resources, and dispatching messages after inspecting live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage piping a remote installer response directly into Bash or PowerShell.

Mitigation: Review the installer path first and prefer a verified, versioned package or inspected installer before installing the oo CLI.

Risk: Write and destructive Svix actions can create, update, dispatch, or delete webhook resources.

Mitigation: Require the agent to show the exact action, target, and JSON payload, then get explicit user approval before write or destructive execution.

## Reference(s):

- [ClawHub Svix skill page](https://clawhub.ai/oomol/skills/oo-svix)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Svix homepage](https://www.svix.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Svix connection setup](https://console.oomol.com/app-connections?provider=svix)
- [OOMOL billing recharge](https://console.oomol.com/billing/token-recharge)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing request payloads and to confirm write or destructive actions with the user.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
