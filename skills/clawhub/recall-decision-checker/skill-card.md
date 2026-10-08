## Description:

A Chinese-language decision-support skill that estimates medical-device recall levels under China's recall rules and returns structured JSON for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Medical-device compliance teams in China can use this skill to draft a recall-level checklist from an assessed harm level. A qualified person must check the result against current official rules and authority decisions before taking action.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: A suggested recall level or deadline could be mistaken for a binding regulatory decision.

Mitigation: Treat the output as a checklist aid; have a qualified reviewer verify current NMPA or provincial authority rules and decisions before acting.

Risk: An unsupported harm level may still produce a Level III result.

Mitigation: Accept only severe, reversible, or none as harm-level inputs and have a human confirm the underlying harm assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/recall-decision-checker)
- [LGD theory overview](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a proposed recall level, notification timeframe, obligations, warnings, and a result code.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; bundled source identifies itself as 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
