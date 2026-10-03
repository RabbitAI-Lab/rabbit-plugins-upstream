## Description:

Discovers Snowflake AI and workload assets using operator-approved read-only access and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Snowflake operators use this skill to inventory Cortex, Snowpark, notebooks, Streamlit, MCP, and AI-observability assets. They can optionally scan the generated inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery accesses a Snowflake account and could expose sensitive inventory details.

Mitigation: Use an approved account and least-privilege read-only role; review the inventory before sharing or pushing it.

Risk: Authentication material or an unverified external package could compromise the operator environment.

Mitigation: Prefer SSO, OAuth, or key-pair authentication, never paste secrets into chat, and verify the agent-bom package before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project (skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell commands; inventory and optional findings in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and requires operator request.]

## Skill Version(s):

0.107.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
