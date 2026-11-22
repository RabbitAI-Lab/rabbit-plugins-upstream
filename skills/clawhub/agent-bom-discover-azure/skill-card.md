## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, and related agent infrastructure as canonical agent-bom inventory. They can request a local scan of that inventory when findings are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied partial security scan flags references to Azure credential files and leaves the referenced adapter path unresolved.

Mitigation: Review the skill and confirm its credential handling before installing; use only operator-approved Azure subscriptions and read-only identities.

Risk: Azure identity material may be present in the operator environment used for discovery.

Mitigation: Use the operator's existing identity chain, never paste or display secrets or tokens, and confirm credential-like values are redacted from persisted or exported inventory.

## Reference(s):

- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Canonical agent-bom inventory JSON, with optional JSON scan findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scanning is performed only when requested.]

## Skill Version(s):

0.115.5 (source: frontmatter; server release 0.115.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
