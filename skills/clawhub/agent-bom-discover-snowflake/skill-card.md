## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI observability assets, emit canonical agent-bom inventory JSON, and optionally scan that inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to inventory Snowflake AI and workload assets as canonical agent-bom inventory, then optionally scan that inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced Snowflake adapter and its dependencies are missing from the package, so their credential handling and redaction are unverified.

Mitigation: Obtain and inspect the adapter and dependencies before supplying authentication.

Risk: Exported Snowflake inventory may contain sensitive information.

Mitigation: Use a dedicated read-only role, choose the output location, and protect the exported inventory.

## Reference(s):

- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions]

**Output Format:** [Canonical inventory JSON and optional JSON scan findings, with shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path.]

## Skill Version(s):

0.112.1 (source: artifact frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
