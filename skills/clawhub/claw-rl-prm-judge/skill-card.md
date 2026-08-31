## Description:

Six-dimension Process Reward Model (PRM) evaluator for AI agent traces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanmeng9527](https://clawhub.ai/user/huanmeng9527)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent-evaluation teams use this skill to score AI agent turns across six dimensions for dashboards, audits, A/B comparisons, and downstream RL loops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent traces may include personal data, secrets, or sensitive tool outputs.

Mitigation: Review and redact traces before judging or storing them; avoid persisting raw traces unless retention and access controls are explicit.

Risk: LLM-as-judge scores can be biased or miscalibrated across domains.

Mitigation: Validate scores against human review periodically and recalibrate the rubric for each deployment.

Risk: A composite reward score can hide a low individual dimension.

Mitigation: Inspect per-dimension scores and investigate any dimension below the documented regression threshold.

Risk: The skill may be invoked on traces when evaluation was not intended.

Mitigation: Prefer explicit invocation for trace review and install only when agent-turn evaluation is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huanmeng9527/skills/claw-rl-prm-judge)
- [Six-dimension rubric](references/dimensions.md)
- [Storage schema](references/storage-schema.md)
- [Judge prompt template](examples/judge-prompt.md)
- [Sample evaluation](examples/sample-evaluation.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with JSON evaluation examples and templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces per-turn six-dimension scores, a composite reward score, a failure-mode label, and a concise rationale.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
