## Description:

复习规划师 helps Chinese-language K12 teachers turn review requests into spaced, interleaved review plans with knowledge maps, key-point priorities, review schedules, classroom activities, and pre-exam state guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 teachers use this skill to plan unit, midterm, final, and pre-exam review cycles. It produces teacher-reviewed plans for what to revisit, when to revisit it, and which easily confused knowledge points should be interleaved, without producing full homework sets or exam papers.

### Deployment Geography for Use:

Global, with localization required for curriculum assumptions, privacy expectations, and crisis referral channels outside the intended Chinese-language K12 context.

## Known Risks and Mitigations:

Risk: The skill may read aggregate class learning data to prioritize review topics.

Mitigation: Tell the teacher what class data will be read and why, use aggregate knowledge-point signals, and save review plans only after explicit teacher confirmation.

Risk: Saved review plans could expose student identity or performance if they include personal details.

Mitigation: Use aliases or student IDs and avoid storing real names, individual scores, rankings, or score-band positions in reviewPlans.

Risk: Pre-exam state support can surface severe distress or safety concerns that exceed review planning.

Mitigation: Stop the review workflow when crisis signals appear, explain the AI boundary, and use localized crisis referral guidance; ask the user's region before giving region-specific contacts.

Risk: Any generated example or variant item used in review activities may contain errors.

Mitigation: Run the AI item self-check, label generated items for teacher verification, and route full homework sets or exam papers to the appropriate downstream skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [Review strategy](references/review-strategy.md)
- [Key-points checklist template](references/key-points-checklist-template.md)
- [Knowledge map example](references/knowledge-map-example.md)
- [Review activity library](references/review-activity-library.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown review plans, tables, calendars, checklists, and classWorkspace.reviewPlans entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before saving reviewPlans; saved plans should avoid real names, individual scores, rankings, and score-band positions.]

## Skill Version(s):

2.3.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
