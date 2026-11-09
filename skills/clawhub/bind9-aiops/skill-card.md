## Description:

Use this skill when a user needs to inspect a BIND 9 DNS server, validate zones, diagnose SERVFAIL, inspect DNSSEC and stale-answer status, compare SOA serials, or request a zone reload, refresh, secondary retransfer, NOTIFY resend or name-specific cache flush. It requires local rndc, named-checkconf and dig utilities and appropriate server-side permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DNS administrators use the skill to inspect BIND 9 service and zone health, troubleshoot DNS and DNSSEC behavior, and request governed zone or cache operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reload, refresh, retransfer, NOTIFY, or cache-flush operations can affect live DNS service or answers.

Mitigation: Use dry-run where available, confirm the target and scope, and grant the process only the RNDC permissions needed for intended operations.

Risk: A timed-out or accepted-but-unproven write may have taken effect, so retrying immediately can repeat an operation.

Mitigation: Inspect BIND zone status and SOA state before retrying an operation with an unknown outcome.

## Reference(s):

- [BIND 9 AIops project homepage](https://github.com/AIops-tools/BIND9-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/bind9-aiops)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured DNS diagnostic results with concise natural-language summaries and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report unknown or incomplete results when a probe or write outcome cannot be confirmed.]

## Skill Version(s):

0.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
