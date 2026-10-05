## Description:

Discovers Snowflake AI and workload assets, writes canonical agent-bom inventory JSON, and optionally scans that inventory without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inventory Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets with their own read-only credentials. They can optionally scan the resulting inventory for findings when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snowflake metadata discovery may expose information beyond the intended scope.

Mitigation: Use only operator-approved accounts and a least-privilege read-only Snowflake role.

Risk: Inventory files may contain sensitive operational metadata if shared or scanned without review.

Mitigation: Choose the output path yourself and review the generated inventory before scanning or sharing it.

Risk: Snowflake authentication material could be exposed during setup.

Mitigation: Use an existing operator-managed auth context; do not paste passwords, private keys, or tokens into chat.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom Python package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON inventory, JSON scan findings, Shell commands, Guidance]

**Output Format:** [JSON files and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; findings are produced only when scanning is requested.]

## Skill Version(s):

0.108.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
