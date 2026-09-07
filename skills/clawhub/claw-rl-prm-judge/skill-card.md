## Description:

Scores AI agent turns across six dimensions so developers can diagnose quality regressions, compare agent versions, and produce structured reward signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanmeng9527](https://clawhub.ai/user/huanmeng9527)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to evaluate non-trivial agent turns, user-corrected responses, tool-use failures, quality regressions, RL rollouts, and A/B comparisons with per-dimension scores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent traces and tool records may contain user data, tool outputs, credentials, or other sensitive information that could be exposed to a remote judge model.

Mitigation: Use redacted traces, avoid sending raw tool results or credentials to remote judge models, and prefer a local or privacy-controlled judge for sensitive work.

Risk: Normal user corrections may unintentionally activate evaluation behavior when broad triggers are enabled.

Mitigation: Narrow or manually control activation when routine corrections should not start PRM evaluation mode.

Risk: LLM-as-judge scores can reflect judge-model bias or calibration drift.

Mitigation: Validate scores against human review periodically and recalibrate the rubric for the deployment domain.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huanmeng9527/skills/claw-rl-prm-judge)
- [PRM six-dimension rubric](artifact/references/dimensions.md)
- [PRM scores storage schema](artifact/references/storage-schema.md)
- [LLM judge prompt template](artifact/examples/judge-prompt.md)
- [Sample evaluation JSON](artifact/examples/sample-evaluation.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with JSON evaluation templates and examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces six independent score fields, a composite reward score, a primary failure mode, and a short summary or rationale.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
