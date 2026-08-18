## Description:

Provides model-agnostic feature attribution for individual predictions, including global permutation importance, local ablation, counterfactual feature changes, and readable rationales.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and reviewers use this skill to explain why a classifier or regressor produced a specific prediction, identify influential features, and explore counterfactual changes for debugging, compliance, or trust review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The attribution script executes the supplied --predict Python file as trusted code.

Mitigation: Use only reviewed prediction files from trusted sources, and run attribution in an isolated environment when handling unfamiliar code.

Risk: The learner module can persist notes, preferences, and operational history in the selected skill directory.

Mitigation: Use learner.py only when persistent local learning is intended, and review or clear learned_patterns.json before sharing the skill directory.

Risk: Attribution results can be unstable for small datasets, greedy counterfactuals, or nested feature structures.

Mitigation: Validate explanations with adequate sample sizes, treat counterfactuals as approximate, and flatten nested inputs before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/interpretable-attribution)
- [ClawHub publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON attribution results with human-readable rationale text and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include global importance scores, local importance scores, the local prediction, counterfactual steps, and a concise rationale.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
