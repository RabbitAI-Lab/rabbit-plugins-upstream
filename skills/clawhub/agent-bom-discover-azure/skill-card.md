## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, Azure ML, and related agentic infrastructure as canonical agent-bom inventory. It supports local discovery with operator-controlled read-only Azure credentials and optional local scanning when findings are requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can access Azure credential caches and use the operator's existing Azure identity for read-only discovery.

Mitigation: Use a least-privilege Azure role and an operator-approved identity such as Azure CLI, workload identity, managed identity, or a short-lived service principal.

Risk: Generated Azure inventory can contain sensitive infrastructure metadata.

Mitigation: Write inventory only to an operator-selected path, review the generated JSON before sharing it, and treat exported inventory as sensitive data.

Risk: Credential-like values could be exposed if discovery outputs are handled carelessly.

Mitigation: Do not request or print raw client secrets, access tokens, or connection strings; rely on the skill's redaction and schema validation expectations.

## Reference(s):

- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands that produce canonical inventory JSON and optional scan findings JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory only to an operator-selected path; exported inventory and Azure credential caches should be treated as sensitive.]

## Skill Version(s):

0.105.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
