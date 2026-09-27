## Description:

Analyzes recurring math mistakes for middle- and high-school learners, identifying specific error patterns and suggesting focused next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, educators, and guardians use this skill to understand persistent math errors, review weak-area reports, and plan targeted practice. It builds on error records supplied by the companion correction notebook rather than collecting or counting errors independently.

### Deployment Geography for Use:

Mainland China; localize curriculum, crisis contacts, and minors' consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Persistent learner profiles or parent and cross-skill sharing may disclose a minor's learning or emotional information.

Mitigation: Enforce profile, sharing, parent-summary, and reminder consent controls in the host platform; honor pause, correction, export, and deletion requests.

Risk: Mainland China-specific crisis resources, curriculum, and consent assumptions may be inappropriate elsewhere.

Mitigation: Confirm the learner's region and localize emergency contacts, educational standards, and minors' consent rules before deployment outside Mainland China.

Risk: Missing cross-session records can make precise trend counts or monthly comparisons misleading.

Mitigation: Use only available correction-notebook statistics; otherwise describe a preliminary trend without invented historical counts.

## Reference(s):

- [ClawHub release: 数学错误DNA](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [Math error dimension table](references/math-error-dimension-table.md)
- [Concept confusion map](references/concept-confusion-map.md)
- [Reading habits](references/reading-habits.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language text and structured Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes error-pattern analysis, weak-area summaries, and on-request monthly reports; historical counts require available records.]

## Skill Version(s):

2.7.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
