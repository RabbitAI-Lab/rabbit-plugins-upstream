## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, engineers, and security reviewers use this skill to inventory Snowflake AI, Cortex, and workload assets as canonical agent-bom JSON. It supports discovery-only collection with optional local scanning when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to Snowflake endpoints using operator-controlled credentials and can read account inventory.

Mitigation: Use a read-only Snowflake role, prefer SSO, OAuth, or key-pair authentication, and avoid pasting secrets into chat.

Risk: Generated inventory may contain sensitive account, workload, or AI-observability details.

Mitigation: Review the generated inventory before sharing or pushing it anywhere, and keep output paths operator selected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [Publisher profile](https://clawhub.ai/user/msaad00)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON inventory output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory only to an operator-selected output path; optional scan output is JSON.]

## Skill Version(s):

0.99.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
