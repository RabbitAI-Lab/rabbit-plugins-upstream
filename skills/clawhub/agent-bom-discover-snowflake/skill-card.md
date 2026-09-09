## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory Snowflake AI, Cortex, Snowpark, notebook, Streamlit, MCP, and observability assets into canonical agent-bom JSON. It supports discovery-only workflows first, with optional local agent-bom scanning when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snowflake inventory may cover sensitive AI, Cortex, query history, and observability assets.

Mitigation: Install only for intended Snowflake inventory work and review the generated inventory JSON before sharing, scanning, or pushing it elsewhere.

Risk: Using broad Snowflake permissions could expose more account metadata than needed for discovery.

Mitigation: Use operator-approved Snowflake accounts, warehouses, databases, and read-only roles.

Risk: Long-lived credentials or secret values could be exposed if pasted into chat or persisted in outputs.

Mitigation: Prefer SSO, OAuth, or key-pair authentication, keep credentials in the operator environment, and do not request or display passwords, private keys, passphrases, or OAuth tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON files]

**Output Format:** [Markdown guidance with bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes an operator-selected inventory JSON file and can optionally write JSON scan findings.]

## Skill Version(s):

0.103.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
