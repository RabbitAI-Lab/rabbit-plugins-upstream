## Description:

Discovers AWS-hosted AI agents and related workloads, writes canonical agent-bom inventory JSON, and optionally scans it at the operator's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory selected AWS AI agents and workloads with read-only credentials. They may then choose to scan or export the inventory locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS discovery could access unintended accounts, regions, or services.

Mitigation: Use an approved read-only role or profile and confirm the account, regions, and services before running discovery.

Risk: Generated inventory may contain sensitive infrastructure details.

Mitigation: Review inventory before sharing or exporting it, and keep any scan or external handoff operator-approved.

Risk: An unexpected package or adapter source could undermine trust in the local workflow.

Mitigation: Verify agent-bom and its AWS adapter come from the expected publisher before installation.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)

## Skill Output:

**Output Type(s):** [JSON inventory, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands; JSON inventory when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; scans and exports require explicit operator approval.]

## Skill Version(s):

0.108.4 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
