## Description:

Evaluates uncertain public claims against evidence, independent context, history, and operator policy to recommend whether a bounded action is supported without executing it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ales375](https://clawhub.ai/user/ales375)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to review uncertain claims before donations, approvals, purchases, referrals, or public endorsements. It compares supplied review findings with operator-defined limits and returns a decision-support disposition, not authorization to act.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A disposition may be mistaken for permission to take a costly or irreversible action.

Mitigation: Treat it as decision support only; apply operator authority and required checks before any transfer, approval, or endorsement.

Risk: Untrusted reviews or an old result may make an unsupported action appear eligible.

Mitigation: Supply trusted review JSON, use a dedicated output path, and require a successful fresh coordinator run before relying on its result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ales375/skills/credibility-action-gate)
- [Review lane contracts](references/lane_contracts.md)
- [Operator policy template](references/policy-template.json)
- [Zooidfund adapter](references/zooidfund_adapter.md)
- [Adapter evaluation scenarios](references/adapter-evaluation-scenarios.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [JSON disposition]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes action eligibility, confidence, size guidance, reasons, and missing reviews; does not execute actions.]

## Skill Version(s):

2.0.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
