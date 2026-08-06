## Description:

Discovers AWS-hosted AI agent and MCP-relevant assets from an operator's environment, emits canonical agent-bom inventory JSON, and can scan that inventory without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud security engineers, and platform operators use this skill to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, and related agentic infrastructure as canonical agent-bom JSON. It supports local discovery and optional local scanning or export when the operator explicitly requests it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enumerates AWS resources in the selected account and region.

Mitigation: Use operator-approved read-only AWS credentials, prefer short-lived assumed roles, and limit discovery to the required services and regions.

Risk: Generated inventory may contain sensitive cloud configuration or resource metadata.

Mitigation: Write inventory only to an operator-selected local path and review it before sharing, exporting, or scanning beyond the local environment.

Risk: Optional scan, export, or push steps can move inventory into another workflow.

Mitigation: Run those steps only after explicit operator approval and make the destination, authentication method, and retained evidence classes clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with bash commands and operator-selected JSON inventory or scan output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local inventory JSON only to an operator-selected path; telemetry and persistence are reported as disabled.]

## Skill Version(s):

0.99.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
