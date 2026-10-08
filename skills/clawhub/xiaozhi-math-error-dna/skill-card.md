## Description:

Analyzes Chinese-language secondary-school math mistakes to identify recurring root causes, related error types, and focused next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking middle- and high-school students and their educators use this skill to understand recurring math mistakes, plan targeted practice, and request weakness summaries. It analyzes mistakes passed from a separate correction notebook rather than collecting or counting them itself.

### Deployment Geography for Use:

Mainland China by default; localize crisis contacts and curriculum assumptions before use elsewhere.

## Known Risks and Mitigations:

Risk: A student's error history and emotional information could be shared or retained without consent.

Mitigation: Confirm profile, parent-sharing, emotion-sharing, cross-skill sharing, and reminder settings before use; do not create a long-term profile or share across skills without consent.

Risk: Math guidance or weakness trends may be inaccurate when error records are sparse or generated practice items are wrong.

Mitigation: Check generated math items before presenting them, label low-confidence trends, and use recorded notebook counts rather than inventing progress data.

Risk: Mainland China crisis contacts and curriculum assumptions may not suit students in other regions.

Mitigation: Confirm the student's region and localize crisis contacts and curriculum assumptions before deployment outside mainland China; refer serious safety signals to appropriate human help.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Math error dimension table](references/math-error-dimension-table.md)
- [Concept confusion map](references/concept-confusion-map.md)
- [Reading habits guide](references/reading-habits.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational text and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes error subtype analyses, targeted practice suggestions, and on-request weakness maps or monthly reports; confidence depends on available error records.]

## Skill Version(s):

2.11.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
