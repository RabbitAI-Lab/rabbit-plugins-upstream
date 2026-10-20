## Description:

Analyzes an agent action trace for excessive steps and repeated actions, then reports loop risk and suggested intervention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect a saved action trace for step-limit violations, repeated calls, and possible lack of progress before deciding whether to intervene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation describes automatic monitoring and circuit-breaking that the supplied checker does not implement.

Mitigation: Treat results as advisory analysis of a supplied trace; implement and review a separate control path before relying on automatic interruption.

## Reference(s):

- [Agent Loop Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-loop-guard)
- [LGD theory background](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text or JSON diagnosis from the local checker; Markdown guidance from the skill]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports trace step count, risk level, advice, and a brief diagnosis; does not halt an agent.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
