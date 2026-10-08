## Description:

Helps operators discover AWS-hosted AI agents and related workloads, create canonical agent-bom inventory JSON, and optionally scan the inventory on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AWS AI agents and associated infrastructure with an approved read-only AWS profile. They can optionally request local scanning or export of the resulting inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS inventory collection exposes infrastructure metadata and requires access to an AWS account.

Mitigation: Use an operator-approved, least-privilege read-only profile or short-lived role, and limit collection to the intended account, regions, and services.

Risk: Generated inventory may reveal sensitive infrastructure details if shared or exported.

Mitigation: Review the local inventory before sharing it, and separately approve any scan, export, or remote handoff.

## Reference(s):

- [agent-bom project and AWS inventory adapter](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON inventory]

**Output Format:** [Markdown guidance with shell commands; operator-selected inventory JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery-only by default; local scan and export require separate operator approval.]

## Skill Version(s):

0.108.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
