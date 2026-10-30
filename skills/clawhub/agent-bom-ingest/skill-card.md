## Description:

Validates operator-generated agent-bom inventory JSON and supports local findings, graph, policy, provenance, and auditor-ready exports without requiring direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use the skill to validate canonical inventory JSON from existing cloud, data platform, CMDB, or endpoint collectors, scan it locally, inspect findings and graphs, and create auditor-ready exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory files and exported reports may contain sensitive infrastructure details.

Mitigation: Protect inventory files and reports with access controls appropriate to their contents.

Risk: Optional control-plane push sends inventory to the configured destination.

Mitigation: Upload only to a destination you control, and configure any token outside chat.

Risk: Optional vulnerability lookups contact OSV and GitHub Advisory services.

Mitigation: Enable these lookups only when the environment permits the associated network requests.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with shell commands; inventory findings and exports can be JSON, SARIF, HTML, or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to an operator-selected path.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
