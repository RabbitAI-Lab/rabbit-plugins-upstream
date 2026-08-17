## Description:

Meta Game Negotiation helps agents structure game-theoretic negotiation tasks with distilled workflows for Nash bargaining, Rubinstein bargaining, Shapley allocation, minimax analysis, self-checking, and reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide negotiation analysis, choose an appropriate game-theory framing, and produce traceable reasoning for proposed allocations or strategies. Outputs should be independently checked when they affect business, financial, or legal decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims self-verification, orchestration, and continuous evolution features that may be stronger than the implemented artifact supports.

Mitigation: Treat those features as prompting and workflow guidance unless independently verified; check important negotiation outputs against known formulas or a trusted domain review.

Risk: The learner script can write notes to a local learned_patterns.json file.

Mitigation: Avoid recording sensitive negotiation details in learner notes and review the local JSON file before sharing or packaging the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-game-negotiation)
- [Skill definition](artifact/SKILL.md)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional code or shell-command snippets and JSON records from the learner script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No external API calls, hidden access, exfiltration, destructive behavior, or unsafe automatic execution are evidenced; the local learner script can update a JSON stats file when run.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
