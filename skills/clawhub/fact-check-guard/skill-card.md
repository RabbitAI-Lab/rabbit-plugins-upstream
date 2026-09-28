## Description:

Helps agents check factual claims in draft content against supplied sources and label each claim as supported, dubious, or unsourced before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Writers, reviewers, and developers use this skill to check claims in agent-generated articles, reports, or responses before sharing them externally and to flag claims that need better sourcing or human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A source-text term match may label an inaccurate claim as supported.

Mitigation: Verify important claims against authoritative sources and have a person review them before publication, especially for regulated content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/fact-check-guard)
- [Publisher project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Per-claim labels and explanations in text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels are supported, dubious, or unsourced; a supported label does not establish that a claim is true.]

## Skill Version(s):

1.0.2 (source: ClawHub release; bundled skill declares 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
