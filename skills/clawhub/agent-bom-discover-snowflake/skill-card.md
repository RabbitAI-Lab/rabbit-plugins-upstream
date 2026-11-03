## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and platform engineers use this skill to discover Snowflake Cortex and related AI and workload assets, save them as canonical agent-bom inventory, and optionally scan that inventory when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required Snowflake adapter is missing from the package, and its runtime behavior could not be verified.

Mitigation: Obtain and review the adapter source before execution. Use an approved read-only Snowflake role, choose the output location, and check the inventory for sensitive information before sharing it.

## Reference(s):

- [agent-bom project page](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Canonical agent-bom inventory JSON, with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented workflow writes inventory to an operator-selected path; scanning is optional and performed when requested.]

## Skill Version(s):

0.113.0 (source: artifact frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
