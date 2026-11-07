## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and platform engineers use this skill to inventory Snowflake Cortex and related AI and workload assets as canonical agent-bom JSON, then optionally scan the saved inventory when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented inventory workflow depends on an adapter that is missing from this package.

Mitigation: Obtain and review the missing adapter from a trusted, fixed release before running it.

Risk: Snowflake inventory output may include sensitive information.

Mitigation: Use a narrowly scoped read-only Snowflake role, write to a protected operator-selected path, and check the inventory for sensitive information before sharing it.

Risk: Credential protection and redaction are documented promises that could not be verified from this package.

Mitigation: Use operator-managed authentication and review the generated inventory for credential material before sharing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [Project homepage (declared metadata)](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [Canonical inventory JSON; optional scan findings JSON; Markdown instructions with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and should occur only when requested.]

## Skill Version(s):

0.113.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
