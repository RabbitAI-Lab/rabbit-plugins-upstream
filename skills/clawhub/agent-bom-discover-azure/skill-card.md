## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and security reviewers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, and related agentic Azure infrastructure as canonical agent-bom inventory. It supports discovery-first workflows that keep Azure credentials in the operator's environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enumerate Azure resource metadata using the operator's Azure identity, and the generated inventory may reveal sensitive cloud-environment information.

Mitigation: Use a read-only Azure account or role, approve the subscription scope explicitly, choose the output path yourself, and treat generated inventory and scan findings as sensitive files.

Risk: Credential material could be exposed if operators paste secrets or print token values during setup.

Mitigation: Use the existing Azure identity chain or short-lived credentials, do not ask users to paste client secrets, and do not print credential values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom GitHub homepage](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON inventory outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes operator-selected local inventory JSON and optional scan findings JSON.]

## Skill Version(s):

0.101.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
