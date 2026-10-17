## Description:

Discovers Snowflake AI and workload assets using the operator's read-only access and writes canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inventory Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets with their own read-only Snowflake access. They can optionally scan the resulting inventory for findings on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery can expose Snowflake inventory beyond the intended scope.

Mitigation: Use only approved accounts and a least-privilege read-only role.

Risk: Authentication secrets or inventory may be disclosed through chat or unintended files.

Mitigation: Keep credentials in the operator's environment, never paste secrets into chat, and write inventory only to an operator-selected path.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Canonical inventory JSON at an operator-selected path; optional JSON scan findings and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery only by default; inventory is schema-validated before any operator-requested scan.]

## Skill Version(s):

0.109.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
