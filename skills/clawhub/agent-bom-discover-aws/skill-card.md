## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security teams use this skill to inventory AWS-hosted AI agents and workloads with operator-controlled, read-only AWS credentials. They can optionally scan the generated inventory locally with agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated inventory may contain sensitive account, workload, or agent details.

Mitigation: Protect the inventory, restrict access, and review its contents before exporting or sharing it.

Risk: The external adapter and agent-bom implementation were not included in this review, so their permissions, redaction, and network behavior are unverified.

Mitigation: Before running, verify the adapter and agent-bom versions and use a narrowly scoped read-only AWS role; confirm the account and services being inventoried.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Canonical JSON inventory file, with Markdown instructions and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes to an operator-selected path; scanning or exporting is optional and operator-chosen.]

## Skill Version(s):

0.113.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
