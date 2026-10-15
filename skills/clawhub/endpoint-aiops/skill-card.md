## Description:

Helps operators assess managed-endpoint fleet health, investigate login delays and configuration drift, and perform guarded profile changes or reboots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Endpoint administrators and IT operations teams use this skill to inventory and assess managed devices, investigate login storms and patch drift, and carry out approved profile assignments or reboots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can reconfigure or reboot managed endpoints without a built-in read-only mode or approval gate.

Mitigation: Start with a read-only management account; require external approval before granting write access, and preview writes with dry-run. Treat audit logs as accountability, not authorization.

Risk: A reboot cannot be undone, and live server behavior has not yet been verified.

Mitigation: Verify connectivity and read-only workflows first; check the target device and schedule a recovery plan before rebooting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/endpoint-aiops)
- [Project homepage (listed in skill metadata)](https://github.com/AIops-tools/Endpoint-AIops)
- [Capabilities](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fleet results may be capped; inspect truncation flags and full-fleet totals.]

## Skill Version(s):

0.12.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
