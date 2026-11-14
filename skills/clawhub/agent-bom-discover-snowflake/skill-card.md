## Description:

Discover Snowflake Cortex, Snowpark, notebook, Streamlit, MCP, and AI-observability assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Snowflake credentials. Use when a user asks to inventory Snowflake AI or Cortex infrastructure as canonical inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and platform engineers use this skill to discover Snowflake AI and workload assets and save a schema-valid inventory for local analysis with agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because Skillspector could not resolve a referenced local Python path, so the scan does not describe that path's contents.

Mitigation: Inspect the referenced local path before relying on the clean verdict or deploying the skill.

Risk: Snowflake discovery uses operator credentials and may read a configured private key path.

Mitigation: Use an operator-approved read-only role with SSO, OAuth, or key-pair authentication, and keep passwords, private keys, passphrases, and tokens out of chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-snowflake)
- [Project homepage (listed in skill metadata)](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Files, Analysis]

**Output Format:** [Canonical agent-bom inventory JSON; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; credential-like values are redacted before persistence or export.]

## Skill Version(s):

0.114.0 (source: frontmatter; server release metadata agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
