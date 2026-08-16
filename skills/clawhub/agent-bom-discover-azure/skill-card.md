## Description:

Discovers Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emits canonical agent-bom inventory JSON, and can scan that inventory without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory approved Azure OpenAI, Container Apps, AKS, Functions, ML, and other agentic Azure infrastructure with an operator-controlled read-only Azure identity. It supports local discovery and optional agent-bom scanning of the generated inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the operator's existing Azure identity and may read sensitive local Azure credential cache files during authentication.

Mitigation: Use a read-only Azure role for approved subscriptions, prefer short-lived or managed credentials, and do not paste or print secrets.

Risk: Generated inventory may reveal Azure resource names, service metadata, or other environment details.

Mitigation: Review the operator-selected output path and avoid sharing generated inventory unless the metadata is approved for disclosure.

Risk: Running scans before inventory validation can produce unreliable findings.

Mitigation: Validate the schema-valid inventory JSON first and run agent-bom scanning only when the operator requests findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom GitHub project](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash commands; generated workflows write JSON inventory and findings files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default behavior is discover-only. Inventory is written to an operator-selected path and scanning runs only when requested.]

## Skill Version(s):

0.100.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
