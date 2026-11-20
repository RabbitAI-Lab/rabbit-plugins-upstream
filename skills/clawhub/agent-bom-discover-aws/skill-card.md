## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use this skill to inventory AWS-hosted AI agents and workloads, including Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, and EC2. They can save a canonical JSON inventory and optionally ask agent-bom to scan it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory collection uses authenticated AWS access and can reveal account resources.

Mitigation: Use an operator-approved profile or short-lived credentials with read-only permissions, and do not paste or display credential values.

Risk: The security review is medium-confidence and partial because two referenced paths were not matched to bundled files.

Mitigation: Review the missing referenced material and the skill's AWS access requirements before installation.

## Reference(s):

- [Project repository (listed in skill metadata)](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [Canonical JSON inventory with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes to an operator-selected path; scanning or handoff is optional and operator-directed.]

## Skill Version(s):

0.115.4 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
