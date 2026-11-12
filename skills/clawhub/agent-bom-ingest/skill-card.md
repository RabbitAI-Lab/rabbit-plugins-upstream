## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from cloud, CMDB, and endpoint sources to produce local findings, graphs, policies, provenance, and audit-ready exports without requiring direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill when they already have canonical inventory JSON from an operator, endpoint collector, CMDB, or agent workflow. It validates the inventory, supports local scanning and analysis, and creates exports for human review, automation, or audit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because a referenced local path was unavailable; the benign verdict has medium confidence and is not a guarantee of zero risk.

Mitigation: Review the complete skill and its runtime environment before relying on its results, especially when processing sensitive inventories.

Risk: An optional control-plane push sends inventory to the operator-provided destination and uses an API token.

Mitigation: Use only a trusted operator-owned destination, configure credentials outside chat, and do not print or expose the token.

Risk: Optional vulnerability enrichment makes external requests to OSV and GitHub Advisory endpoints.

Mitigation: Enable those lookups only when external package queries are acceptable for the environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-ingest)
- [Declared project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands, Guidance]

**Output Format:** [Shell commands and JSON, SARIF, HTML, or Markdown inventory reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports are written to an operator-selected path.]

## Skill Version(s):

0.114.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
