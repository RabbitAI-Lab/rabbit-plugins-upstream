## Description:

把学习目标拆成可执行的 30 天方案（小学高段用周计划版），并在学生开启后跟进执行偏差。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 students, guardians, and study-support agents use this skill to convert a student's goals, grade band, weak-area summary, available time, and consent settings into a weekly or 30-day learning plan. The skill can also produce student-facing progress summaries, parent-visible dashboards, and reminder handoff items when the required consent gates are enabled.

### Deployment Geography for Use:

Global; designed for Mainland China Chinese-language K12 study-planning contexts, with crisis contacts, curriculum assumptions, consent rules, and localization reviewed before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill handles sensitive student planning data and may use learning profile summaries, parent-visible dashboards, and reminder enrollment.

Mitigation: Keep profile access, parent dashboard generation, cross-skill sharing, and reminder enrollment disabled by default, and require explicit student or guardian consent for each relevant action.

Risk: The skill is designed for Chinese K12 study planning, and its curriculum assumptions, guardian consent expectations, and crisis contacts may not fit other regions.

Mitigation: Localize language, curriculum assumptions, minor-consent rules, and crisis referral channels before deployment outside Mainland China.

Risk: Study plans can become misleading or counterproductive if they overstate available time, invent historical statistics, or ignore grade-band limits.

Mitigation: Use the student's current input or consented profile summary, mark uncertain historical patterns, ask for missing dates or time estimates, and apply grade-band defaults from the bundled references.

Risk: Parent-visible summaries could expose sensitive student information or hide urgent safety signals.

Mitigation: Generate parent-visible content only after checking consent, omit emotional judgments unless separately allowed, and switch to the crisis referral protocol when safety signals appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [plan-templates.md](artifact/references/plan-templates.md)
- [handover-protocol.schema.json](artifact/shared/handover-protocol.schema.json)
- [platform-conventions.md](artifact/shared/platform-conventions.md)
- [crisis-exception.md](artifact/shared/crisis-exception.md)
- [crisis-referral-protocol.md](artifact/shared/crisis-referral-protocol.md)
- [grade-bands.md](artifact/shared/grade-bands.md)
- [vocab.md](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown-style Chinese study plans, dashboard text, review summaries, and structured handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses grade-band defaults, consent gates, and crisis-referral rules; reminder outputs are queue handoffs rather than direct reminder delivery.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
