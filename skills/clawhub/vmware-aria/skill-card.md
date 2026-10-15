## Description:

Helps agents monitor VMware Aria Operations, investigate alerts and anomalies, assess capacity, generate reports, and manage supported alerts and maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to inspect Aria Operations metrics, alerts, capacity, and platform health, and to perform authorized alert, report, and maintenance tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change alert state, reports, or maintenance status.

Mitigation: Prefer a read-only service account and expose read-only MCP tools unless writes are needed; require authorization before changes.

Risk: Aria credentials could be exposed if stored in local plaintext configuration.

Mitigation: Use a secret manager or injected environment variables for production passwords.

Risk: Disabling TLS verification could expose operational data and credentials.

Mitigation: Keep TLS verification enabled.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-aria)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-Aria)
- [Setup guide](references/setup-guide.md)
- [Operations playbooks](references/ops-playbooks.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include metrics, alert details, capacity estimates, and report links.]

## Skill Version(s):

2.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
