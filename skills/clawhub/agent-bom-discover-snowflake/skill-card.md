## Description:

Discovers Snowflake AI and workload assets and writes canonical agent-bom inventory JSON for optional local scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inventory Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets using their existing read-only Snowflake access. They can optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery can expose sensitive Snowflake inventory to anyone who receives the output file.

Mitigation: Use a least-privilege read-only role and review the generated inventory before sharing it.

Risk: The Snowflake adapter runs from the separately installed agent-bom package, not from this skill file.

Mitigation: Review the installed adapter and use only an operator-approved Snowflake account and authentication context.

## Reference(s):

- [Agent-BOM project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [Agent-BOM Python package (skill metadata)](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON inventory files, JSON scan findings, Guidance]

**Output Format:** [Markdown instructions and local JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is the default output; scan findings are generated only on request.]

## Skill Version(s):

0.107.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
