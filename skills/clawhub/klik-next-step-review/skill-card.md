## Description:

Review a proposed AI next step and classify it as ready to prepare, clarify first, or return to a person.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyixu](https://clawhub.ai/user/chengyixu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and workflow reviewers use this skill to evaluate a short, redacted proposed AI next step and decide whether it is ready for a reviewable draft, needs clarification, or should return to a person.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may treat a Ready to prepare classification as authorization to execute an external action.

Mitigation: State that Ready to prepare only permits a reviewable draft or plan, and return access changes, judgment calls, or external commitments to a person.

Risk: Review inputs may include sensitive session details, client data, credentials, financial information, or health information.

Mitigation: Ask only for short, redacted summaries and avoid requesting credentials, full recordings, private transcripts, or other sensitive material.

Risk: Incomplete source, stale context, ambiguous scope, or unclear authority can produce a misleading next-step classification.

Mitigation: Use Clarify first until source, context, scope, authority, and expected outcome are clear enough to inspect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chengyixu/skills/klik-next-step-review)
- [Klik pre-launch direction](https://pre.hiklik.ai/?utm_source=clawhub&utm_medium=companion_skill&utm_campaign=kickstarter_prelaunch&utm_content=next_step_review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Compact Markdown review card]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selects one status and returns a concise reason, safe next move, and open question; Ready to prepare only permits a reviewable draft or plan.]

## Skill Version(s):

1.0.2 (source: server release evidence, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
