## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and operators use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, and agentic Azure infrastructure as canonical agent-bom inventory JSON. They can then optionally scan that inventory when findings are requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on external agent-bom code that may run with Azure credentials.

Mitigation: Trust and pin the exact agent-bom version or commit, inspect the referenced Azure adapter code, and use a dedicated Azure identity with minimum read-only permissions.

Risk: Credential-like Azure values or tokens could be exposed if handled carelessly.

Mitigation: Use the operator's existing Azure identity chain, avoid pasted secrets, do not print credential values, and rely on the skill's redaction expectations before persistence or export.

Risk: Discovery from an environment with broad Azure permissions could collect more inventory than intended.

Mitigation: Run only against operator-approved subscriptions with a read-only identity and write inventory only to an operator-selected output path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-selected local inventory JSON and optional local scan findings JSON.]

## Skill Version(s):

0.104.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
