## Description:

Guides operators through read-only discovery of AWS-hosted AI agents and related workloads, producing canonical agent-bom inventory JSON for optional local scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory Bedrock agents and related AWS workloads in an approved account and region. They may choose to scan or export that inventory locally afterward.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS inventory discovery could access an unintended account, region, or service.

Mitigation: Confirm the account, regions, and services before running; use an approved read-only profile or short-lived role.

Risk: Generated inventory could expose sensitive infrastructure details if shared.

Mitigation: Keep inventory at an operator-selected local path and review it before sharing or exporting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [Agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [Agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON inventory]

**Output Format:** [Markdown instructions and commands; JSON inventory at an operator-selected path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery only by default; scanning and exports require an explicit operator request.]

## Skill Version(s):

0.108.1 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
