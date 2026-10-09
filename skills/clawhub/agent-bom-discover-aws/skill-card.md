## Description:

Helps operators discover AWS-hosted AI agents and related workloads, produce canonical inventory JSON, and optionally scan that inventory with agent-bom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI agents and workloads in approved AWS accounts and regions. They can optionally request local agent-bom findings or exports after reviewing the generated inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS inventory can expose sensitive cloud architecture when shared or exported.

Mitigation: Review inventory before sharing or exporting it and keep generated files at an operator-selected location.

Risk: Broad AWS credentials or unintended account and region selection could expand the inventory scope.

Mitigation: Use a read-only profile or short-lived assumed role, and confirm the account, regions, and services before discovery.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [Project homepage (declared in skill metadata; source provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON inventory]

**Output Format:** [Markdown guidance and shell commands; canonical JSON inventory file when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery-only by default; local scans and JSON or SARIF exports require operator approval.]

## Skill Version(s):

0.108.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
