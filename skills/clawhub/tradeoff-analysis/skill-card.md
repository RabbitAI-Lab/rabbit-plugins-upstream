## Description:

Helps agents compare concrete options using weighted criteria, evidence-backed scores, sensitivity checks, and reversibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ysskrishna](https://clawhub.ai/user/ysskrishna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other decision-makers use this skill to compare a small set of concrete options and explain a defensible choice using weighted criteria, sensitivity, and switching costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Casual comparison requests may trigger a detailed decision matrix when brainstorming or a brief opinion was intended.

Mitigation: Specify whether you want brainstorming, a quick opinion, or a full weighted comparison.

Risk: Unverified scores or assumptions can make a recommendation appear better supported than it is.

Mitigation: Check score evidence, flag estimates, and test whether plausible changes reverse the recommendation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ysskrishna/skills/tradeoff-analysis)
- [Worked tradeoff example](references/example.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown decision matrix and recommendation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies estimated scores, sensitivity to assumptions, and reversibility.]

## Skill Version(s):

2026.10.5 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
