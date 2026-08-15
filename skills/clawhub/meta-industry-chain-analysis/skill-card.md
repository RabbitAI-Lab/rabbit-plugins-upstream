## Description:

Meta Industry Chain Analysis guides agents through industry-chain research by decomposing supply chains, identifying supply-side bottlenecks, validating conclusions with counterexamples, and maintaining traceable research notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to structure industry-chain and sector research, focusing on scarce supply links, evidence quality, red-team disconfirmation, and follow-up tracking. The skill is intended for research workflow guidance and explicitly avoids stock recommendations, target prices, or trading instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner can persist usage history and preference notes in learned_patterns.json.

Mitigation: Do not store sensitive notes in learner fields; inspect or delete learned_patterns.json periodically.

Risk: The learner accepts a skill directory argument and can write learning data outside the intended skill if pointed elsewhere.

Mitigation: Run the learner only against this skill's own directory or another explicitly approved skill directory.

Risk: Industry-chain analysis can be mistaken for investment advice if conclusions are overextended.

Mitigation: Keep outputs framed as research workflow guidance and preserve the skill's prohibition on recommendations, target prices, and position sizing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-industry-chain-analysis)
- [Distillation report](artifact/distillation_report.md)
- [Skill source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown research workflow guidance with structured analysis sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include source dates and evidence quality labels when making research claims; financial advice, buy/sell calls, price targets, and position sizing are out of scope.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
