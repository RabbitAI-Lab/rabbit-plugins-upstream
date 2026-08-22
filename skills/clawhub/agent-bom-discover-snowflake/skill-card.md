## Description:

Discovers Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emits canonical agent-bom inventory JSON, and scans it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security reviewers use this skill to inventory approved Snowflake AI and workload assets as schema-valid agent-bom JSON. It supports local discovery and optional local scanning while keeping Snowflake credentials in the operator-controlled environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to Snowflake accounts and may collect sensitive inventory metadata.

Mitigation: Run it only against operator-approved accounts with a read-only Snowflake role, and review the generated inventory JSON before sharing or pushing it elsewhere.

Risk: Credential exposure could occur if secrets are pasted into chat or written into generated artifacts.

Mitigation: Use SSO, OAuth, or key-pair authentication from the operator environment and do not request or display passwords, private key contents, passphrases, or OAuth tokens.

Risk: The generated inventory could be misleading if schema validation fails or discovery is incomplete.

Mitigation: Treat schema-valid inventory JSON as the evidence source and stop to fix invalid inventory before scanning or reporting findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [ClawHub publisher profile](https://clawhub.ai/user/msaad00)
- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with bash command blocks; generated artifacts are JSON inventory and optional scan findings files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory only to an operator-selected path; optional scan output is produced only when requested.]

## Skill Version(s):

0.101.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
