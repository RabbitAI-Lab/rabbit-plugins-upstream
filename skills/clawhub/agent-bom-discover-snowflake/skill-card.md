## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security reviewers use this skill to inventory Snowflake AI and Cortex infrastructure as schema-valid agent-bom JSON. It supports discover-only collection first, with optional local scanning when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to operator-selected Snowflake accounts and can discover sensitive inventory metadata.

Mitigation: Use a least-privilege read-only Snowflake role and run discovery only against operator-approved accounts, warehouses, databases, and schemas.

Risk: Snowflake authentication material could be exposed if pasted into chat or written into shared files.

Mitigation: Use the operator's existing SSO, OAuth, or key-pair authentication context and do not paste passwords, private keys, passphrases, or OAuth tokens into chat.

Risk: Generated inventory JSON may contain environment-sensitive asset details.

Mitigation: Write inventory only to an operator-selected local path and review the JSON before sharing or pushing it elsewhere.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom Source Repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI Package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-selected inventory JSON and optional agent-bom findings JSON.]

## Skill Version(s):

0.102.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
