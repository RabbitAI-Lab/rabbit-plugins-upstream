## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory Snowflake AI, Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets as canonical agent-bom inventory. It supports discover-only local collection and optional scanning when the operator requests findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snowflake credentials or credential-adjacent values could be exposed if copied into chat or stored in the wrong place.

Mitigation: Use the operator's existing Snowflake SSO, OAuth, or key-pair authentication context and do not paste passwords, private keys, passphrases, or OAuth tokens into chat.

Risk: Inventory JSON may contain sensitive infrastructure metadata even when credential material is redacted.

Mitigation: Use a read-only Snowflake role, run only against operator-approved accounts, and choose the output path deliberately.

Risk: The discovery workflow contacts Snowflake account and regional endpoints using operator-provided credentials.

Mitigation: Limit execution to approved Snowflake accounts and roles, and review the disclosed network endpoints before running.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash commands and JSON inventory file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes operator-selected canonical inventory JSON and optional JSON scan findings.]

## Skill Version(s):

0.104.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
