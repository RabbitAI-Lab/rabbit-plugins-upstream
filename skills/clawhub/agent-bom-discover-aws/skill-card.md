## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and optionally scan that inventory without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and cloud operators use this skill to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, and agentic AWS infrastructure as canonical agent-bom inventory. It supports discovery-only operation by default, with local scanning or export only when the operator asks for those follow-on steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enumerate AWS resources using operator-approved cloud credentials, and generated inventory may contain sensitive infrastructure data.

Mitigation: Confirm the AWS profile, region, service scope, and output path before execution; prefer short-lived read-only credentials and protect generated inventory as sensitive data.

Risk: Authenticated AWS API calls are required for discovery across enabled services.

Mitigation: Use the existing AWS SDK credential chain with AWS SSO, WebIdentity, or STS assumed-role credentials, and avoid pasting or printing raw access keys or tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [Agent BOM source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and operator-selected JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses operator-approved AWS credentials, writes inventory to an operator-selected path, and only scans or exports inventory when explicitly requested.]

## Skill Version(s):

0.105.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
