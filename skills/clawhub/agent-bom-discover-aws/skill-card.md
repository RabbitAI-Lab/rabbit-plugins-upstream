## Description:

Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security engineers use this skill to inventory AWS-hosted AI-agent and workload resources as canonical JSON, with optional operator-approved local scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS inventory can contain sensitive account and workload details, and this artifact review does not verify the external adapter's implementation or claimed redaction.

Mitigation: Use a reviewed adapter release with scoped, short-lived read-only credentials, confirm the target account and services, protect the generated inventory, and share or scan it only with separate approval.

## Reference(s):

- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands]

**Output Format:** [Canonical inventory JSON; optional JSON or SARIF scan exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Written to an operator-selected path; scanning or sharing requires separate operator approval.]

## Skill Version(s):

0.110.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
