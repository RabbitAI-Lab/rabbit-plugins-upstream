## Description:

Guides agents in choosing, setting up, and managing Neon cloud backend services, including Lakebase Postgres, Auth, Object Storage, Functions, AI Gateway, and Realtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up Neon-backed applications, choose backend services, manage branches, and configure or deploy infrastructure through the CLI or MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installs, skill updates, and MCP configuration may grant persistent or broad access.

Mitigation: Review installation scope and configuration changes; require approval before global or non-interactive setup.

Risk: API keys and environment pulls may expose credentials in local files or agent configuration.

Mitigation: Review credential storage, limit access, and opt out of local environment pulls when unnecessary.

Risk: Deploy, apply, or project-deletion commands can change or remove cloud resources.

Mitigation: Confirm the target project and branch, inspect planned changes, and require explicit approval before destructive or deployment actions.

Risk: The skill may send issue feedback to Neon without informing the user.

Mitigation: Require explicit consent before sending feedback and remove secrets or sensitive project details from any report.

## Reference(s):

- [Neon skill on ClawHub](https://clawhub.ai/andrelandgraf/skills/neon)
- [Neon documentation index](https://neon.com/docs/llms.txt)
- [Neon CLI installation](https://neon.com/docs/cli/install.md)
- [Neon MCP client setup](https://neon.com/docs/ai/connect-mcp-clients-to-neon.md)
- [Claimable Neon reference](artifact/references/claimable-neon.md)
- [Function triggers reference](artifact/references/function-triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to configure Neon services and deploy changes; actions require appropriate access.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
