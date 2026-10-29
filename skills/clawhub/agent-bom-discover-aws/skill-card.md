## Description:

Discovers AWS-hosted AI agent and MCP-relevant assets, writes canonical inventory JSON, and optionally scans that inventory without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AWS-hosted AI agents and workloads as canonical JSON, then optionally run agent-bom scans on that inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated AWS inventory may contain sensitive account and workload details.

Mitigation: Use a narrowly scoped, read-only AWS role, confirm the account, region, services, and output path, and protect the inventory as sensitive.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Files, Scan findings]

**Output Format:** [Canonical JSON inventory; optional agent-bom scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scanning is optional.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
