## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security engineers use this skill to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, and related agentic AWS infrastructure as canonical agent-bom inventory. It supports discover-only collection by default, with local scanning or export only when the operator explicitly requests it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enumerate selected AWS services using operator-approved credentials.

Mitigation: Use a dedicated read-only AWS role or profile, choose regions and services explicitly, and avoid broad or long-lived credentials.

Risk: Generated inventory may contain sensitive environment or cloud account details.

Mitigation: Inspect the local inventory JSON before sharing it and keep outputs at operator-selected paths.

Risk: Local scans and exports may hand generated inventory to additional tooling when requested.

Mitigation: Run scans or exports only after explicit operator approval and verify the agent-bom package source before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes canonical inventory JSON to an operator-selected path and may produce local scan findings or exports when explicitly requested.]

## Skill Version(s):

0.102.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
