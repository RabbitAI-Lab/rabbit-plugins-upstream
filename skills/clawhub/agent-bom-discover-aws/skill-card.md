## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and cloud operators use this skill to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, and related agentic infrastructure as canonical agent-bom JSON. The workflow supports local scanning and exports only when the operator explicitly asks for those follow-on actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inventory AWS environments through authenticated AWS SDK calls.

Mitigation: Use only operator-approved read-only short-lived AWS profiles or assumed roles for AWS accounts and regions the operator intends to inventory.

Risk: Generated inventory can contain sensitive infrastructure details even when credential-like values are redacted.

Mitigation: Write inventory only to an operator-selected path, review it before sharing, and require explicit approval before any scan export or remote handoff.

Risk: Optional local scans and exports can broaden where inventory evidence is stored.

Mitigation: Default to discover-only mode and run scan, export, push, or managed handoff commands only after the operator explicitly requests them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [agent-bom source](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with bash command examples and operator-selected JSON inventory or scan output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.11+, agent-bom, and operator-controlled AWS credentials; inventory files are written only to operator-selected paths.]

## Skill Version(s):

0.103.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
