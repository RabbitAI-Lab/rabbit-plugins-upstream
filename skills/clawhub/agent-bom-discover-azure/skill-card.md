## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, cloud engineers, and security reviewers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, and related agentic Azure infrastructure as canonical agent-bom inventory without handing long-lived Azure credentials to agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure discovery can expose credential material or use broader cloud access than intended.

Mitigation: Use the operator's existing Azure identity chain, prefer read-only short-lived credentials scoped to selected subscriptions, and do not request or print client secrets, access tokens, or connection strings.

Risk: Generated inventory can contain sensitive cloud metadata about Azure resources.

Mitigation: Write inventory only to an operator-selected local path, keep credential-like values redacted, and store generated JSON where sensitive infrastructure metadata is permitted.

Risk: Best-effort or prose summaries could misrepresent the Azure environment.

Mitigation: Use schema-validated canonical inventory JSON as evidence and stop to fix inventory when schema validation fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI project](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON inventory or findings files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes canonical Azure inventory to an operator-selected local path and can optionally produce local agent-bom scan findings.]

## Skill Version(s):

0.102.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
