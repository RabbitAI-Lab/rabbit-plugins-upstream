## Description:

Discovers Snowflake AI and workload assets using operator-approved read-only access, writes canonical agent-bom inventory JSON, and scans the inventory only on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and Snowflake operators use this skill to inventory Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets and optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery could expose sensitive Snowflake inventory or use broader access than intended.

Mitigation: Use an operator-approved account and read-only role, choose the output path, and keep secrets out of chat.

Risk: Locally installed discovery code may not match the reviewed skill.

Mitigation: Verify the agent-bom installation and its provenance before connecting to a real Snowflake account.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project homepage (skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON files]

**Output Format:** [Shell commands and canonical inventory JSON; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning occurs only when requested.]

## Skill Version(s):

0.108.4 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
