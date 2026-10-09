## Description:

Discovers Snowflake AI and workload assets and produces canonical agent-bom inventory for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Snowflake operators use this skill to inventory Cortex, Snowpark, notebooks, Streamlit, MCP, and AI-observability assets with their own read-only credentials, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery uses the operator's Snowflake authentication context.

Mitigation: Use only approved accounts and a least-privilege, read-only Snowflake role; do not share credentials in chat.

Risk: Generated inventory may reveal internal Snowflake assets even when credential-like values are redacted.

Mitigation: Choose the inventory output path and review the JSON before sharing or scanning it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown instructions and canonical JSON inventory; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.108.3 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
