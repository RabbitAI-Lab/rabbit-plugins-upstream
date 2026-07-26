## Description: <br>
Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to inventory Snowflake AI and Cortex infrastructure into schema-valid agent-bom JSON, then optionally scan that inventory for findings when requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may use the operator's existing Snowflake authentication context to query inventory. <br>
Mitigation: Use a least-privilege, read-only Snowflake role and only operator-approved accounts, warehouses, databases, and schemas. <br>
Risk: Snowflake passwords, private keys, passphrases, or OAuth tokens could be exposed if pasted into chat. <br>
Mitigation: Use SSO, OAuth, or key-pair authentication from the local environment and do not paste credential material into chat. <br>
Risk: Generated inventory files may contain sensitive infrastructure details. <br>
Mitigation: Write inventory only to an operator-selected path and review the local JSON before sharing or scanning it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake) <br>
- [agent-bom project homepage](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operator-selected local inventory JSON and optional agent-bom findings JSON; credential-like values are redacted before persistence or export.] <br>

## Skill Version(s): <br>
0.98.0 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
