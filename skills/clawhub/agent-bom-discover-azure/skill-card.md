## Description:

Discovers Azure-hosted AI agent and MCP-relevant assets, writes canonical agent-bom inventory JSON, and can scan it without exposing long-lived Azure credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security engineers use the skill to inventory Azure-hosted AI and workload resources for agent-bom analysis, using operator-approved subscriptions and read-only identities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because a referenced local path was missing, so its benign assessment has medium confidence.

Mitigation: Review the skill setup and confirm that Azure access is limited to the subscriptions and read-only permissions you intend to use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure)
- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands]

**Output Format:** [Canonical agent-bom inventory JSON and optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; credential-like values are redacted before persistence or export.]

## Skill Version(s):

0.115.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
