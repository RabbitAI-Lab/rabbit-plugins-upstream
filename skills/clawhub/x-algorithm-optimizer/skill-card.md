## Description:

Optimize posts for X's (Twitter's) For You feed algorithm, based on X's open-sourced ranking code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zfoong](https://clawhub.ai/user/zfoong)

### License/Terms of Use:

MIT

## Use Case:

External creators, social media operators, and agent users use this skill to draft, review, and improve X posts for legitimate reach using cited ranking weights, distribution mechanics, and negative-signal checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes negative-signal and suppression guidance that could be misused to improve spam, deceptive promotion, or content that should be restricted by platform rules.

Mitigation: Use only for genuine, policy-compliant content; decline spam, inauthentic behavior, ban evasion, fake engagement, and attempts to launder restricted content.

Risk: The optional critic produces directional heuristic scores and can be mistaken for an exact reach predictor.

Mitigation: Present scoring as a writing aid, explain that X's model uses embeddings, engagement counts, graph context, and freshness, and ground recommendations in the cited references.

Risk: Ranking weights and thresholds are based on a dated public-code snapshot and may drift over time.

Mitigation: State the snapshot limitation when exact values matter and refresh values from the current public algorithm source before relying on precise numbers.

## Reference(s):

- [Source Repository](https://github.com/zfoong/X-algorithm-optimizer)
- [X Open-Source Algorithm](https://github.com/twitter/the-algorithm)
- [Scoring Weights](references/scoring-weights.md)
- [Distribution Mechanics](references/distribution-mechanics.md)
- [Negative Signals and Suppression](references/negative-signals.md)
- [Account Playbooks](references/account-playbooks.md)
- [Before / After Examples](references/examples.md)
- [Myth-Busting](references/myths.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with revised post drafts, variants, rationale, audit notes, and optional shell commands for the local critic]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include directional heuristic scoring from the optional local-only Python critic; the score is not a simulator of X's ranking model.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
