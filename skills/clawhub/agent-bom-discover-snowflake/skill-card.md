## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and platform engineers use this skill to inventory Snowflake Cortex and related AI workloads as canonical agent-bom JSON, then scan that inventory when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snowflake inventory exports may contain sensitive account or workload metadata even after credential values are redacted.

Mitigation: Use a dedicated read-only role, choose an approved account scope and restricted output path, and treat exported inventory as sensitive.

Risk: A referenced adapter run with operator credentials may collect data outside the intended scope if its behavior or target is not checked.

Mitigation: Verify the adapter and select the Snowflake account scope yourself before running discovery.

## Reference(s):

- [agent-bom Project Repository](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and canonical JSON inventory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scanning is performed only when requested.]

## Skill Version(s):

0.110.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
