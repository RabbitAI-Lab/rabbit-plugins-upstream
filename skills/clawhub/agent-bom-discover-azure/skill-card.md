## Description:

Discovers Azure-hosted AI agent and MCP-relevant assets in operator-approved subscriptions and writes canonical agent-bom inventory JSON for optional local scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory Azure AI and workload assets in approved subscriptions, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery uses the operator's existing Azure credentials and can access subscription inventory.

Mitigation: Use a least-privilege, read-only identity and limit discovery to approved subscriptions.

Risk: Generated inventory may expose sensitive details if shared without review.

Mitigation: Write inventory only to an operator-selected path and review it before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom Python package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON inventory]

**Output Format:** [Markdown instructions with shell commands; canonical inventory JSON written to an operator-selected path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSON scan findings only when requested; credential-like values are redacted from inventory.]

## Skill Version(s):

0.109.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
