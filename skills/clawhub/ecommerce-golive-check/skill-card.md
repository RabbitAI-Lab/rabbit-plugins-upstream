## Description:

Checks an ecommerce store’s pre-launch readiness across checkout, order handling, compliance, usability, search visibility, and release hygiene, then produces an evidence-backed launch gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clarezoe](https://clawhub.ai/user/clarezoe)

### License/Terms of Use:

MIT

## Use Case:

Developers and store operators use this skill to assess whether an ecommerce site is ready for launch. It organizes specialist checks and compiles evidence, blockers, remediation steps, and any explicit waivers into a launch gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transaction checks may cause real charges or order side effects if run against a production store.

Mitigation: Use an isolated store in payment test mode, disable fulfillment and customer notifications, and explicitly authorize production charges or order changes.

Risk: A launch gate may approve incomplete results if required checks or waiver approvals are missing.

Mitigation: Inspect delegated skills, confirm every required check ran with evidence, and independently verify waiver approvals before relying on LAUNCH-READY.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clarezoe/skills/ecommerce-golive-check)
- [Block catalog](artifact/references/block-catalog.md)
- [Gate schema](artifact/references/gate-schema.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown launch gate with a summary table and remediation list; JSON intake and verdict data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes evidence, severity, explicit waivers, and a legal disclaimer; unresolved blocking items result in NOT LAUNCH-READY.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
