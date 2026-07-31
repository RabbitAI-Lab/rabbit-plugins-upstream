## Description: <br>
Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, data platform engineers, and security reviewers use this skill to inventory Snowflake AI and Cortex infrastructure as canonical agent-bom JSON. It supports discover-only local collection and optional scan findings while keeping Snowflake credentials in the operator environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Snowflake discovery can expose sensitive account, workload, and AI asset metadata if run with overbroad access or shared carelessly. <br>
Mitigation: Use a least-privilege read-only Snowflake role and review the generated inventory JSON before sharing or pushing it anywhere. <br>
Risk: Long-lived or pasted Snowflake credentials could be mishandled during setup. <br>
Mitigation: Prefer SSO, OAuth, or key-pair authentication and keep credentials in the operator environment rather than pasting secrets into chat. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake) <br>
- [agent-bom project homepage](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and JSON file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes operator-selected inventory JSON and, when requested, optional scan findings JSON with credential-like values redacted.] <br>

## Skill Version(s): <br>
0.98.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
