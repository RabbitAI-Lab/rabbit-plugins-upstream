## Description:

Turn a proposed AI follow-through step into a compact Action Readiness Card that makes source, freshness, scope, authority, expected result, and human-return conditions explicit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyixu](https://clawhub.ai/user/chengyixu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and agent operators use this skill to decide whether an AI should prepare a bounded, reviewable next step from remembered Context. It is meant for readiness review, not account access, tool execution, messaging, commitments, or authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Action Readiness Card could be mistaken for permission to execute a real-world action.

Mitigation: Treat the card as a review checklist only; return to a person for new access, material judgment, external commitments, or conflicting Context.

Risk: A user could provide sensitive source material while describing the proposed step.

Mitigation: Ask only for short, redacted summaries and avoid credentials, full recordings, private transcripts, client data, financial data, health data, or other sensitive material.

Risk: Stale or incomplete remembered Context could lead to an unsuitable preparation plan.

Mitigation: Use Refresh Context when the source is missing, stale, contradictory, incomplete, or insufficiently traceable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chengyixu/skills/klik-action-readiness)
- [Klik pre-launch direction](https://pre.hiklik.ai/?utm_source=clawhub&utm_medium=companion_skill&utm_campaign=kickstarter_prelaunch&utm_content=action_readiness)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown Action Readiness Card]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Non-executing review output with readiness, source, freshness, allowed preparation, unauthorized actions, expected result, and human-return conditions.]

## Skill Version(s):

1.0.1 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
