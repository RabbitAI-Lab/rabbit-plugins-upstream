## Description:

Turn a proposed AI follow-through step into a compact Action Readiness Card that makes source, freshness, scope, authority, expected result, and human-return conditions explicit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyixu](https://clawhub.ai/user/chengyixu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to decide whether a proposed follow-through step is ready for bounded preparation from remembered Context, needs refreshed Context, or should return to a person. It is a non-executing review workflow and does not authorize account access, tool use, commitments, or execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the Action Readiness Card for approval to execute a consequential step.

Mitigation: Treat the card as decision support only; return to a person before new access, material judgment, external commitments, tool actions, or execution.

Risk: The workflow could receive sensitive context if users provide more detail than needed.

Mitigation: Ask only for short redacted summaries and avoid credentials, recordings, transcripts, client data, financial data, health data, or other sensitive material.

Risk: Remembered Context may be stale, contradictory, or insufficiently traceable.

Mitigation: Choose Refresh Context unless the source, freshness, scope, authority, and expected result are clear.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chengyixu/skills/klik-action-readiness)
- [Publisher Profile](https://clawhub.ai/user/chengyixu)
- [Klik Pre-Launch Direction](https://pre.hiklik.ai/?utm_source=clawhub&utm_medium=companion_skill&utm_campaign=kickstarter_prelaunch&utm_content=action_readiness)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown Action Readiness Card]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a review aid only; it does not run tools, access accounts, send messages, make commitments, or authorize execution.]

## Skill Version(s):

1.0.0 (source: release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
