## Description:

Discovers Azure-hosted AI agent and MCP-relevant assets from an operator-controlled Azure environment, emits canonical agent-bom inventory JSON, and can scan that inventory without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and security reviewers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, Azure ML, and related agentic Azure infrastructure as canonical agent-bom inventory. It supports discover-only collection with optional local scanning when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Azure credentials to discover cloud resources, so an overly broad or unintended identity could expose more inventory than the operator intended.

Mitigation: Use an operator-controlled read-only Azure identity, confirm the subscription before discovery, and prefer Azure CLI, workload identity, managed identity, or short-lived service principal credentials.

Risk: Long-lived secrets or token values could be exposed if copied into prompts, terminal output, or generated files.

Mitigation: Do not ask users to paste client secrets, do not print credential values, and rely on the operator environment's Azure identity chain.

Risk: Inventory may be written to an unintended location or scanned before the operator has approved the output.

Mitigation: Write inventory only to an operator-selected path and run the optional agent-bom scan only when the operator explicitly requests findings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom GitHub Repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI Project](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local, operator-selected inventory JSON and optional JSON scan findings; credential-like values are expected to be redacted before persistence or export.]

## Skill Version(s):

0.103.2 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
