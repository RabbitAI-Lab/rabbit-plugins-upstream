## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security or platform engineers use this skill to inventory Snowflake AI and Cortex infrastructure with operator-controlled read-only Snowflake access. It writes schema-valid agent-bom inventory JSON and can run a local scan when the operator explicitly asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snowflake credentials or secret material could be exposed if pasted into chat or written into inventory artifacts.

Mitigation: Use the operator's existing Snowflake SSO, OAuth, or key-pair authentication context; avoid pasting passwords, private keys, passphrases, or OAuth tokens into chat.

Risk: Inventory results can contain sensitive Snowflake resource and workload metadata.

Mitigation: Use a read-only Snowflake role and review the generated local inventory before scanning or sharing it.

Risk: Running discovery against unintended Snowflake accounts or scopes could collect more inventory than intended.

Mitigation: Run only against operator-approved Snowflake accounts, warehouses, databases, schemas, and roles.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom GitHub Repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI Package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and local JSON inventory or findings files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery output is written to an operator-selected local path; scan output is generated only when requested.]

## Skill Version(s):

0.100.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
