## Description:

Discover AWS-hosted AI agent and MCP-related assets from the operator's environment, write canonical inventory JSON, and optionally scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use this skill to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, and related AI assets as canonical JSON. They can pass that inventory to agent-bom for a local scan when they choose.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced AWS inventory adapter is not bundled with this release, so its behavior cannot be verified from the package contents.

Mitigation: Review the separately obtained adapter and its dependencies before running it.

Risk: AWS inventory can expose sensitive account, principal, workload, and asset details.

Mitigation: Use a narrowly scoped read-only role, confirm the target account, region, and services, and treat generated inventory as sensitive; verify sanitization before sharing or uploading it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Canonical inventory JSON with discovery and optional local scan instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scanning and export are optional, operator-directed steps.]

## Skill Version(s):

0.113.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
