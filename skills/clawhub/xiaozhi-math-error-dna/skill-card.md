## Description:

Analyzes recurring errors in Chinese middle-school math, identifies specific root causes, and suggests focused follow-up practice and progress summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese middle-school students and their educators use this skill to understand patterns behind repeated math mistakes, target persistent weak areas, and request a monthly math progress report. It builds on errors classified by a separate mistake notebook rather than serving as a stand-alone question recorder or tutor.

### Deployment Geography for Use:

Chinese middle-school context; mainland China defaults require localization elsewhere

## Known Risks and Mitigations:

Risk: Long-term learning profiles, parent summaries, reminders, or sharing between skills can expose minors' learning information without appropriate consent.

Mitigation: Confirm the relevant consent settings before retaining profiles, sending reminders, preparing parent summaries, or sharing records; use only the current conversation when consent is absent.

Risk: Crisis-support contacts and child-consent defaults may be unsuitable outside mainland China.

Mitigation: Localize crisis contacts and consent requirements to the student's location before use outside mainland China; escalate crisis signals to trusted adults and local emergency services.

Risk: Invented historical counts or overconfident error diagnoses may mislead students about their progress.

Mitigation: Use the mistake notebook as the source for historical counts, avoid precise cross-session figures when unavailable, and label tentative patterns as preliminary.

## Reference(s):

- [ClawHub release: 数学错误DNA](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [Math error dimensions and subtypes](references/math-error-dimension-table.md)
- [Concept confusion map](references/concept-confusion-map.md)
- [Reading habits and error prevention](references/reading-habits.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Chinese-language text and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes error subtype and root-cause explanations, targeted practice suggestions, and on-request monthly summaries; historical counts depend on available records.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
