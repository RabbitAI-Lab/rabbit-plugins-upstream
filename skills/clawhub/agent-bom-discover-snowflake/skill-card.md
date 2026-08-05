## Description: <br>
Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and Snowflake operators use this skill to discover Snowflake AI and workload assets, emit schema-valid agent-bom inventory JSON, and optionally scan that inventory for findings using local operator credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Snowflake credentials or key material could be exposed if pasted into chat or written into prompts. <br>
Mitigation: Use the operator's existing SSO, OAuth, or key-pair authentication context and keep passwords, private keys, passphrases, and tokens outside chat. <br>
Risk: Generated inventory may contain sensitive Snowflake environment details even when credential-like values are redacted. <br>
Mitigation: Write inventory only to an operator-selected local path and handle generated JSON and scan output as sensitive operational data. <br>
Risk: Overly broad Snowflake permissions could expose more account metadata than needed for discovery. <br>
Mitigation: Run discovery with an operator-approved read-only role limited to the accounts, warehouses, databases, and schemas in scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake) <br>
- [agent-bom project homepage](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON files] <br>
**Output Format:** [Markdown guidance with bash commands and generated JSON inventory files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Discovery writes inventory to an operator-selected local path; scan output is produced only when the operator asks for findings.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
