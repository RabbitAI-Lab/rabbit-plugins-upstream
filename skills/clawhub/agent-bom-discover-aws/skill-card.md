## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials. Use when a user asks to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, or agentic AWS infrastructure as canonical inventory. Passing that inventory to agent-bom is optional and operator-chosen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security teams use this skill to discover AWS-hosted AI agents and workloads and create canonical inventory JSON for an operator-selected local workflow. They can optionally scan the inventory with agent-bom when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required external adapter is not included in this package, so its read-only behavior and redaction have not been verified.

Mitigation: Use a dedicated read-only AWS role and review the adapter and dependency versions before execution.

Risk: Inventory files may contain sensitive information about cloud assets and principals.

Mitigation: Write only to an operator-selected path and protect the resulting inventory file.

Risk: Sending inventory to an external service could expose retained evidence beyond the local workflow.

Mitigation: Approve any external upload separately and confirm its destination, authentication method, and retained evidence.

## Reference(s):

- [agent-bom project repository](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [Canonical inventory JSON file and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning or external handoff is optional and operator-chosen.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
