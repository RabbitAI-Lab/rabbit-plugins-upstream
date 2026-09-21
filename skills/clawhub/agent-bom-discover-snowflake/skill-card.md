## Description:

Discovers Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emits canonical agent-bom inventory JSON, and can scan it on request without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to inventory Snowflake AI and Cortex infrastructure as canonical agent-bom inventory. It supports discover-only local output by default, with optional scanning when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow inventories Snowflake assets and may expose environment metadata if run against the wrong account or role.

Mitigation: Run it only for operator-approved Snowflake accounts, warehouses, databases, and read-only roles.

Risk: Snowflake passwords, tokens, private keys, or passphrases could be exposed if pasted into chat or logs.

Mitigation: Use the operator's existing SSO, OAuth, or key-pair environment and do not request or display credential material.

Risk: Inventory output could be written somewhere unintended or shared before review.

Mitigation: Verify the operator-selected output path, keep output local by default, and inspect or redact inventory before sharing.

## Reference(s):

- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-selected local inventory JSON and, when requested, local agent-bom scan findings JSON.]

## Skill Version(s):

0.105.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
