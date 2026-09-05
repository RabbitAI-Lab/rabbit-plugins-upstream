## Description:

把“从头再讲一遍”变成有间隔、有交叉、有取舍的复习排期。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 teachers use this skill to plan unit, midterm, final, and pre-exam review schedules from class weakness data. It helps produce knowledge maps, key-point checklists, spaced review calendars, interleaving groups, review activities, and exam-day study-state guidance.

### Deployment Geography for Use:

China Mainland by default; deployment in other regions should localize curriculum alignment, privacy assumptions, and crisis-support resources before student-facing use.

## Known Risks and Mitigations:

Risk: The skill is designed around Chinese K12 curriculum, privacy assumptions, and crisis-resource defaults.

Mitigation: Confirm the intended Chinese K12 teacher workflow before use, and localize curriculum, privacy rules, and crisis-support resources before deploying outside mainland China.

Risk: A generated review plan could be inappropriate for the actual class schedule or student needs if accepted without review.

Mitigation: Require the teacher to review the full plan and explicitly confirm before any reviewPlans entry is saved.

Risk: Class data used for planning could expose student identity, scores, or rankings.

Mitigation: Save only de-identified, knowledge-point-level planning data; use pseudonyms or groups and exclude individual scores, ranks, and score-band positions.

Risk: Student anxiety or safety signals may exceed ordinary study-support needs.

Mitigation: Stop the review-planning workflow for crisis signals, avoid diagnosis, and direct the user to trusted adults and localized emergency or youth-support channels.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [Review Strategy](references/review-strategy.md)
- [Knowledge Map Example](references/knowledge-map-example.md)
- [Key Points Checklist Template](references/key-points-checklist-template.md)
- [Review Activity Library](references/review-activity-library.md)
- [Platform Conventions](shared/platform-conventions.md)
- [Crisis Exception](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown tables, plain-language guidance, and structured review plan fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review plans are proposals until teacher confirmation; saved entries use de-identified, knowledge-point-level data.]

## Skill Version(s):

2.1.6 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
