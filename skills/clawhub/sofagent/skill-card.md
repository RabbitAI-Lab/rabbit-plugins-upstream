## Description:

FDE Skill guides frontline deployment engineers through enterprise AI deployment by constraining agent behavior, auditing changes, capturing operational knowledge, and sustaining optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, frontline deployment engineers, and enterprise AI teams use this skill to diagnose workflows, identify AI-suitable nodes, build knowledge and ontology artifacts, and deliver governed enterprise agent deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad installation and MCP enablement can expose high-impact tools in enterprise environments.

Mitigation: Confirm the install source and enable only the MCP roles needed for the deployment.

Risk: Persistent daemon or cron behavior can continue acting after initial setup.

Mitigation: Review daemon and cron settings before installation and require human approval for persistence.

Risk: Remote execution, cloud or SSH training, browser actions, PR merge permissions, and data query or push tools can move data or change systems.

Mitigation: Disable unused high-impact tools and require explicit human approval for deployment, remote execution, data movement, and merge actions.

Risk: Device registration and enterprise data access may introduce privacy or data-sovereignty exposure.

Mitigation: Verify device registration behavior and data query or push defaults in a controlled enterprise environment before use.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Publisher profile](https://clawhub.ai/user/kongfangxun)
- [Skill entrypoint](artifact/SKILL.md)
- [Agent and MCP overview](artifact/AGENTS.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and structured deployment guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to run audits, MCP tools, installation checks, workflow setup, and human approval gates when those capabilities are available.]

## Skill Version(s):

1.5.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
