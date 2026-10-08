## Description:

Discovers Snowflake AI and workload assets and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inventory Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets using their own read-only access. They can optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery uses the operator's Snowflake authentication context and may read local connection configuration.

Mitigation: Use a least-privilege read-only role, keep credentials in the operator environment, and approve the account and output path before running discovery.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON inventory, JSON findings]

**Output Format:** [Markdown guidance with shell commands; JSON files at operator-selected paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory discovery is the default; findings are produced only on request.]

## Skill Version(s):

0.108.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
