## Description:

Helps operators investigate VMware infrastructure and manage virtual machines, clusters, alarms, and guest operations through VMware vSphere and ESXi.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to diagnose vSphere issues and perform VM lifecycle, deployment, migration, guest, and cluster operations across vCenter and ESXi environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent actions can change or delete VMware resources.

Mitigation: Use a dedicated least-privilege vCenter/ESXi account, prefer read-only tools, review changes before approval, and configure deny rules for production.

Risk: Guest commands can run with privileges beyond the vCenter account.

Mitigation: Use least-privilege guest credentials and avoid providing high-privilege guest accounts.

Risk: Configured webhooks can expose infrastructure identifiers and event details.

Mitigation: Keep webhooks disabled unless needed and restrict destinations to trusted endpoints.

Risk: Local credential and audit files contain sensitive operational information.

Mitigation: Protect local .env and audit files and restrict access to authorized operators.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-AIops)
- [Setup guide](references/setup-guide.md)
- [Investigation protocol](references/investigation-protocol.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Conversational text and Markdown with CLI commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce offline HTML investigation snapshots when requested.]

## Skill Version(s):

2.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
