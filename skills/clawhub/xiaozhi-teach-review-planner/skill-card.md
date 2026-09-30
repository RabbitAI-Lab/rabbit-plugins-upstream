## Description:

Helps teachers plan spaced, interleaved review around knowledge gaps, exam timelines, and student readiness without generating assignments or exam papers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to organize unit and exam review into knowledge maps, prioritized topics, phased schedules, spaced revisits, and interleaved practice. It can propose a review plan for teacher approval before storing it in the class workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review plans draw on class learning data and could expose student information when stored or shared.

Mitigation: Obtain teacher confirmation before saving; use pseudonyms and omit individual scores, rankings, and unnecessary source data.

Risk: Chinese K12 curriculum assumptions, consent practices, and crisis contacts may not fit other regions.

Mitigation: Localize curricula and consent practices before deployment outside Mainland China; verify local support and emergency contacts before providing them.

Risk: Exam stress or student safety signals may require support beyond educational planning.

Mitigation: Do not diagnose or treat; pause planning for crisis signals and refer to trusted adults and appropriate local professional or emergency support.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [Review strategy](artifact/references/review-strategy.md)
- [Review activity library](artifact/references/review-activity-library.md)
- [Knowledge map example](artifact/references/knowledge-map-example.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [Chinese-language review plans and schedules in Markdown; optional structured review-plan entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Class workspace updates require teacher confirmation; stored plans omit real student names, individual scores, and rankings.]

## Skill Version(s):

2.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
