## Description:

Screens transactions for structuring, rapid in-and-out activity, cross-border transfers without KYC, and unreported large amounts using local rule-based checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Financial operations teams and developers can screen transaction records for specified AML risk patterns and review the resulting risk scores and rule matches. Results are screening signals, not regulatory determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested tools and stated permissions disagree with the skill's file and execution behavior around sensitive financial records.

Mitigation: Review the skill before installation, limit access to necessary transaction files, and reconcile tool permissions with actual use before handling real financial data.

Risk: Documentation describes alert-system push and logging paths that the local checker does not implement.

Mitigation: Do not rely on automated alert delivery; verify local outputs and arrange a reviewed alerting workflow separately.

## Reference(s):

- [AML Sentinel release on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/aml-sentinel)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Terminal risk summary or JSON results with matched rules, scores, and risk levels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [High-risk results return exit code 1; other results return 0; invalid arguments return 2.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release; bundled skill text says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
