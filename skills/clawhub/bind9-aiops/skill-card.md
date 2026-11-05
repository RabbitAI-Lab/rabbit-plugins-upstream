## Description:

Governed BIND 9 DNS service, zone, DNSSEC and SOA diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DNS administrators use the skill to inspect BIND 9 service and zone health, diagnose DNS and DNSSEC issues, compare primary and secondary SOA serials, and request guarded maintenance operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live reload, refresh, retransfers, notifications, and cache flushes can affect DNS service; some changes have no safe undo.

Mitigation: Restrict RNDC permissions, confirm the target, review dry-run results, and inspect BIND state before retrying an operation whose result is unknown.

Risk: Runtime safeguards are documented claims and are not verified by the supplied artifact files.

Mitigation: Review the external package and version before installation, and verify safeguards against the source implementation before relying on them.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/BIND9-AIops)
- [ClawHub release](https://clawhub.ai/zw008/skills/bind9-aiops)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Operational guidance, Configuration guidance]

**Output Format:** [Concise text and structured DNS diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on BIND availability, target configuration, and operator permissions.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
