## Description:

Organizes claims and their cited evidence into a reviewable evidence chain, scores evidence quality, and flags claims that lack independently verifiable support without determining whether the claims are true.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theoretical text: All rights reserved

## Use Case:

Agents and their users can organize evidence for AI-generated claims, identify unsupported conclusions, and decide which original sources need human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The evidence-quality score may be mistaken for proof that a claim is true or for a professional determination.

Mitigation: Treat the score as an organizing aid, check original sources, and seek qualified review for consequential decisions.

Risk: Broad trigger wording may invoke the skill for tasks that do not require an evidence-chain review.

Mitigation: Invoke it deliberately for claim-evidence tasks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-chain-builder)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown evidence-chain report or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists evidence source types, an evidence-quality score, and a warning when verifiable support is insufficient.]

## Skill Version(s):

1.0.2 (source: ClawHub release; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
