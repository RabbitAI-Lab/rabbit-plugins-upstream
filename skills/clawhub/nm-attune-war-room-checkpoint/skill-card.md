## Description:

Assesses decision reversibility and risk at critical checkpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill inside higher-level commands to assess the reversibility, blast radius, and confidence of consequential decisions before continuing or escalating to a War Room deliberation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checkpoint and War Room details may be saved locally under ~/.claude, including affected files and decision rationale.

Mitigation: Avoid using the skill on highly confidential projects unless that local audit trail is acceptable or separately controlled.

Risk: The skill may provide incorrect or misleading decision guidance if the supplied context is incomplete or inaccurate.

Mitigation: Review checkpoint outputs before acting on escalations, recommendations, or auto-continue decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-war-room-checkpoint)
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)
- [Publisher profile](https://clawhub.ai/user/athola)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Configuration, Guidance]

**Output Format:** [Structured Markdown with YAML-style response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include escalation mode, reversibility score, confidence, recommendation or orders, and whether user confirmation is required.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
