## Description:

Discover Snowflake Cortex and AI assets, create a canonical agent-bom inventory, and optionally scan it using the operator's existing read-only access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and platform engineers use this skill to inventory Snowflake AI and workload assets as canonical agent-bom JSON, then scan the saved inventory when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review coverage was incomplete because a referenced local path could not be resolved.

Mitigation: Review the unresolved path and skill contents before installation.

## Reference(s):

- [Project repository](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [JSON inventory and findings files, with shell commands and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning is optional and performed when requested.]

## Skill Version(s):

0.115.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
