## Description:

Discovers Snowflake AI and workload assets, writes canonical agent-bom inventory JSON, and optionally scans that inventory for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and Snowflake operators use this skill to inventory approved Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets with read-only access. They can request a local scan of the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery uses the operator's Snowflake authentication context.

Mitigation: Use an approved account and read-only role; keep passwords, private keys, and tokens out of chat.

Risk: Generated inventory may contain information about Snowflake assets.

Mitigation: Choose the output path yourself and review the inventory before sharing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom Python package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance and shell commands; JSON inventory and optional JSON scan findings when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.108.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
