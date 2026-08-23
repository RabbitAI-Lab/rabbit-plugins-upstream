## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, engineers, and security operators use this skill to inventory AWS-hosted AI agents, MCP-relevant assets, and related workloads into canonical agent-bom JSON, then optionally scan or export findings locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses operator-approved AWS access and generated inventory may describe cloud infrastructure, services, and principals.

Mitigation: Use a read-only, short-lived AWS profile or role, start with a narrow region and service scope, and treat generated inventory files as sensitive.

Risk: AWS credentials are required in the operator environment for local discovery.

Mitigation: Use the existing AWS SDK credential chain, prefer AWS SSO, WebIdentity, or STS assumed-role credentials, and do not paste or print access keys or tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [Publisher profile](https://clawhub.ai/user/msaad00)
- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON inventory paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-approved commands for local AWS discovery, scan, and export workflows; inventory is written to an operator-selected JSON output path.]

## Skill Version(s):

0.101.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
