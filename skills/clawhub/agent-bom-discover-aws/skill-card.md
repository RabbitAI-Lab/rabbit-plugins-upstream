## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to discover AI and workload assets in their AWS environment and save them as canonical inventory JSON. They can optionally run agent-bom against that inventory when they request findings or exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS credentials used for discovery could expose inventory beyond the operator's intended scope if their permissions or selected services are too broad.

Mitigation: Use short-lived AWS SSO, WebIdentity, or STS credentials with read-only permissions limited to the intended services, and review the incomplete scan references before installation.

## Reference(s):

- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [Canonical JSON inventory file with optional shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning and export are optional and operator-chosen.]

## Skill Version(s):

0.114.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
