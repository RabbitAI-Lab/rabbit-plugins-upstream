## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security engineers use this skill to inventory selected AWS AI agent and workload services with operator-approved read-only AWS credentials, produce canonical agent-bom inventory JSON, and optionally run local scans or exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS discovery can expose cloud account, service, and infrastructure metadata.

Mitigation: Use only operator-approved read-only AWS profiles or short-lived roles and limit service scope to the intended inventory.

Risk: Generated inventory files may contain sensitive operational details even when credential patterns are redacted.

Mitigation: Write inventory to an operator-selected local path, review it before sharing, and only approve exports when the destination and retained data are understood.

Risk: Optional scans, exports, or handoffs can move inventory data beyond the local workflow.

Mitigation: Use discover-only mode by default and require explicit operator approval for scans, exports, destinations, authentication, and retained evidence classes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands; generated inventory and optional scan/export outputs are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory only to an operator-selected path; scan and export handoffs are optional and operator-approved.]

## Skill Version(s):

0.100.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
