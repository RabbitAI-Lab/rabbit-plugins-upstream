## Description:

Helps NSX administrators manage distributed firewall policies, security groups, VM tags, microsegmentation, traceflow diagnostics, and IDS/IPS visibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

NSX security administrators and engineers use this skill to inspect and manage distributed firewall rules, security groups, and VM tags, and to check enforcement with traceflow and IDS/IPS status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firewall changes can block legitimate traffic or permit unwanted access.

Mitigation: Limit installation to authorized NSX administrators, use least-privileged credentials, and review previews before confirming writes.

Risk: Stored NSX passwords may be exposed or misused.

Mitigation: Prefer secret-manager injection over persistent .env passwords in production.

Risk: Skipping authentication checks can hide access problems.

Mitigation: Avoid --skip-auth except for diagnostics.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project homepage (linked in release metadata)](https://github.com/vmware-skills/VMware-NSX-Security)
- [Setup guide](references/setup-guide.md)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results and previews can inform proposed policy changes; writes require operator approval.]

## Skill Version(s):

1.17.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
