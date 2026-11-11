## Description:

Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security practitioners use this skill to inventory Azure AI and workload resources as canonical agent-bom data, then optionally scan that inventory when findings are requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial and flags a missing local reference, leaving some evidence incomplete.

Mitigation: Before installation, check that the missing example is available and matches the documented read-only workflow.

Risk: The workflow uses the operator's Azure identity to read subscription resources and writes an inventory file.

Mitigation: Use only operator-approved subscriptions and read-only identities, never paste or display secrets, and write inventory only to an operator-selected path.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Canonical inventory JSON and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scanning is optional and performed only when requested.]

## Skill Version(s):

0.114.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
