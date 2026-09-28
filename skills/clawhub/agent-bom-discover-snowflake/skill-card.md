## Description:

Discovers Snowflake AI and workload assets and produces canonical agent-bom inventory JSON using operator-controlled, read-only credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inventory Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets. An optional local scan produces findings when the operator requests it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery could access more Snowflake data than intended.

Mitigation: Use only operator-approved accounts and read-only roles.

Risk: Snowflake credentials or inventory could be exposed.

Mitigation: Keep credentials in the operator environment, do not paste secrets into chat, and verify the inventory output path before running.

Risk: Incomplete inventory could produce misleading scan findings.

Mitigation: Validate inventory against its schema and scan only when the operator requests findings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project (skill metadata link; provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON inventory]

**Output Format:** [Markdown guidance and commands; canonical inventory JSON when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery writes to an operator-selected path; an optional scan can produce JSON findings.]

## Skill Version(s):

0.106.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
