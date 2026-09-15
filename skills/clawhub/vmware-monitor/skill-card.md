## Description:

Use this skill for safe, read-only queries of VMware infrastructure, including health summaries, inventory, alarms, events, performance, capacity, and object investigation drill-downs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and operations teams use this skill to inspect VMware vCenter/ESXi environments without making changes. It supports triage, inventory lookup, alarm and event review, capacity checks, performance sampling, and object-centered investigations before any remediation is routed to other tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles VMware credentials and operational infrastructure data.

Mitigation: Use a dedicated VMware service account with the built-in Read-Only role and inject secrets through a secret manager or launch-time environment rather than storing passwords in ~/.vmware-monitor/.env.

Risk: Optional Slack or Discord webhooks can disclose hostnames, IP addresses, usernames, alarms, events, or other operational details.

Mitigation: Enable webhooks only for approved recipients and treat those channels as destinations for sensitive operational data.

Risk: Installing from an untrusted package source could expose VMware environments to supply-chain risk.

Mitigation: Install only from package sources that the operator trusts and can verify before production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [VMware Monitor Homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Read-Only Enforcement Test](https://github.com/vmware-skills/VMware-Monitor/blob/main/tests/eval/regression/test_read_only_enforcement.py)
- [Capabilities (Read-Only)](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Cluster Health Summary Display Template](references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured VMware monitoring summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VMware results may contain operational data; list outputs can be paginated, and performance or capacity readings are point-in-time samples.]

## Skill Version(s):

1.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
