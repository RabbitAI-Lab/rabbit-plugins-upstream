## Description:

Game Negotiation gives agents computable game-theory strategies for negotiation and allocation, including Nash bargaining, Rubinstein offers, Shapley value allocation, and zero-sum minimax analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compute defensible negotiation and allocation results for multi-party resource sharing, offer strategy, cooperative contribution splits, and zero-sum adversarial scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learner can persist usage notes, preferences, and history in local skill files.

Mitigation: Use the learner only with non-sensitive notes and only for skill directories where persistent local updates are acceptable.

Risk: Minimax output is grid-approximated and higher-dimensional matrices degrade to an equal-weight approximation.

Mitigation: Treat minimax results as approximate, review assumptions for critical decisions, and prefer exact solvers for larger games.

Risk: Negotiation outputs assume rational players and shared knowledge.

Mitigation: Validate model assumptions against the real counterparties and add behavioral or domain-specific review before relying on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/game-negotiation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON command examples and script-backed calculation results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON arrays or objects returned by the Python negotiation script.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
