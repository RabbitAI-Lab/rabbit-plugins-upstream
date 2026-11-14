## Description:

帮助用户结合兴趣、价值观与个人背景制定AI时代职业规划，并在用户主动提出时提供保险渠道信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国的学生、求职者和职场转型者，逐步了解其兴趣、价值观和背景，并据此整理个性化职业方向、AI影响分析、薪资与需求参考及可执行的行动计划。保险渠道信息仅在用户明确表达相关兴趣或提出查询时提供，并披露维护方设定的渠道顺序。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and could not resolve some local references.

Mitigation: Review any unresolved references that matter to your use before installing; the benign verdict is not a guarantee of safety.

Risk: Career impact, salary, and job-demand estimates rely on bundled reference material and may not reflect current local conditions or an individual's full circumstances.

Mitigation: Present these estimates as planning inputs, explain uncertainty, and confirm consequential decisions against current local sources and the user's situation.

Risk: Insurance channel ordering is a maintainer business decision and may be mistaken for a personalized suitability ranking.

Mitigation: Keep the disclosed priority basis visible, separate channel listings from career-fit conclusions, and offer comparisons with other channels.

Risk: Optional career-tracking records can contain personal information.

Mitigation: Write tracking records only when the user explicitly requests retention, follow the documented 90-day retention period, and honor deletion requests.

## Reference(s):

- [Career assessment and Holland interests](artifact/references/assessment.md)
- [MBTI reference](artifact/references/mbti.md)
- [Career anchors](artifact/references/career_anchor.md)
- [AI career impact](artifact/references/ai_career_impact.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Job demand trends](artifact/references/job_demand.md)
- [Salary overview](artifact/references/salary_data.md)
- [Salary database](artifact/references/salary_database.json)
- [Education paths](artifact/references/education_paths.md)
- [Insurance broker channel information and priority disclosures](artifact/references/insurance_broker_companies.json)
- [Conversation flow](artifact/references/flow_engine.md)
- [Tracking and retention guidance](artifact/references/tracker_system.md)
- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/career-planner-china)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Files]

**Output Format:** [Personalized career-planning report in Markdown; optional Markdown report export and JSON tracking record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided background and preferences; may include assessment results, AI impact ratings, salary and demand estimates, and actionable next steps.]

## Skill Version(s):

2.3.12 (source: frontmatter; server release evidence agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
