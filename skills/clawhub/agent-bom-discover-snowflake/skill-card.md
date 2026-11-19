## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and security teams use this skill to discover Snowflake AI and workload assets and save them as canonical agent-bom inventory. They can request a scan of that inventory when they need findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because a referenced local path was missing, so related behavior was not fully assessed.

Mitigation: Review the missing reference and its behavior before installation. Limit discovery to operator-approved Snowflake accounts and read-only roles, and keep credentials in the operator's environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, JSON, Guidance]

**Output Format:** [Canonical JSON inventory; optional JSON scan findings and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path. Scanning is performed only when requested.]

## Skill Version(s):

0.115.4 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
