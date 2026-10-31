## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to discover Snowflake AI and workload assets with an operator-approved read-only account and write a canonical inventory file. They can scan that inventory locally when they request findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required Snowflake discovery adapter is not included, so its credential handling could not be checked.

Mitigation: Obtain and review the adapter from a verified release before running it; use a dedicated read-only Snowflake role and protect the inventory output.

## Reference(s):

- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Canonical agent-bom inventory JSON; optional scan findings JSON; Markdown instructions with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scan findings are produced only when requested.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
