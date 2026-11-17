## Description:

Provides Chinese fortune-telling and divination readings grounded in classical texts, with chart calculations performed by bundled scripts and interpretations that state their school and sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request BaZi and Zi Wei Dou Shu chart readings, single-question divination, relationship compatibility, auspicious date selection, or a source-based review of a fortune-telling report. The skill explains readings with stated schools and textual references, and excludes medical, legal, and investment conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags privacy concerns related to saving personal birth information in reports.

Mitigation: Explain the use of birth details before collecting them, obtain consent, minimize identifying details, and check how reports are handled.

Risk: The security scan reports accuracy concerns with some readings.

Mitigation: Present readings as interpretive and uncertain; do not use them to make medical, legal, or investment decisions.

Risk: The security scan inspected only part of the package, leaving some components partially inspected.

Mitigation: Review the portions that were not fully inspected before deployment and treat the scan as incomplete.

## Reference(s):

- [ClawHub release](https://clawhub.ai/haiyangchenbj/skills/chinese-fortune-telling)
- [Interpretation boundaries](references/99-boundaries.md)
- [Classical schools and sources](references/00-schools-and-sources.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown narrative, structured readings, and tables where useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Readings state the interpretive school and sources, use qualified language, and avoid medical, legal, and investment advice.]

## Skill Version(s):

1.2.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
