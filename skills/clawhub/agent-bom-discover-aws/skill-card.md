## Description:

Discovers AWS-hosted AI agent and MCP-relevant assets using operator-approved credentials and creates canonical agent-bom inventory JSON for optional local scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security teams use this skill to inventory AI agents and related workloads in selected AWS accounts and regions, with optional operator-approved local scanning and export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS inventory access could exceed the intended account, region, or service scope.

Mitigation: Confirm the selected account, regions, and services; use narrowly scoped read-only IAM permissions and short-lived credentials.

Risk: Optional scan, export, or push could share inventory beyond the discovery-only workflow.

Mitigation: Review and approve each optional command and its destination before any handoff; keep the default inventory local.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON inventory]

**Output Format:** [Markdown guidance and canonical JSON inventory file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Schema-validated inventory at an operator-selected path; local scan and export only on request.]

## Skill Version(s):

0.107.2 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
