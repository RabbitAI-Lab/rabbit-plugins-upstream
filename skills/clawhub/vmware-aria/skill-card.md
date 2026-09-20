## Description:

vmware-aria helps agents inspect VMware Aria Operations and VCF Operations data for metrics, alerts, capacity, anomalies, reports, maintenance, and platform health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to monitor VMware Aria Operations environments, investigate alerts and anomalies, plan capacity, generate reports, and perform confirmation-gated administrative actions such as alert handling and maintenance windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use real VMware Aria Operations credentials and perform administrative write actions.

Mitigation: Install with a least-privilege Aria Operations account, prefer read-only RBAC unless write tools are needed, and store passwords through a secret manager or runtime environment injection.

Risk: Alert, report, alert-definition, and maintenance writes can affect operational state.

Mitigation: Review confirmation prompts and blast-radius previews before approving writes; rely on the skill's audit logging and do not use --yes unless the change is already reviewed.

Risk: Skipping authentication checks can be mistaken for successful authorization.

Mitigation: Treat --skip-auth only as a local or network diagnostic and run normal authentication checks before relying on operational results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aria)
- [Project homepage](https://github.com/vmware-skills/VMware-Aria)
- [Operating vmware-aria with a local / small model](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Investigation Protocol - Causal Chain Root Cause Analysis](references/investigation-protocol.md)
- [Ops Playbooks - Troubleshooting Paths with vmware-aria](references/ops-playbooks.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include list-result envelopes, diagnostic findings, and blast-radius previews for confirmation-gated write operations.]

## Skill Version(s):

1.16.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
