## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and cloud operators use this skill to inventory AWS-hosted agentic infrastructure and optionally pass the resulting canonical inventory to agent-bom for local findings, graph, policy, or export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the operator's AWS SDK credential chain and can collect sensitive cloud inventory data.

Mitigation: Use a least-privilege, short-lived audit profile, confirm the AWS account and regions before running, and keep generated inventory files access-controlled.

Risk: Optional handoff to agent-bom or exports can move collected inventory into another local workflow or destination.

Mitigation: Use discover-only mode by default and perform scans, pushes, or exports only after the operator explicitly approves the destination, auth method, and retained evidence classes.

Risk: External agent-bom package or repository code is executed when the operator runs the workflow.

Mitigation: Review the external agent-bom package or repository adapter before executing it in the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [Publisher profile](https://clawhub.ai/user/msaad00)
- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON files]

**Output Format:** [Markdown guidance with inline bash commands and generated canonical inventory JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write operator-selected inventory and export files; agent-bom scanning is optional and operator-approved.]

## Skill Version(s):

0.104.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
