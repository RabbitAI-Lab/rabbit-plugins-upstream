## Description:

Provides Chinese-language AI-era career planning guidance, including user intake, Holland, MBTI, and career-anchor assessment, AI job impact ratings, salary and demand context, and a personalized career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users seeking major selection, career planning, career transition, or AI-era job direction use this skill to receive Chinese-language assessments and personalized career recommendations. The skill can also generate a structured Markdown career planning report when the user explicitly asks for export.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Insurance career guidance may present a company ranking or recommendation as more neutral or verified than the evidence supports.

Mitigation: Review insurance recommendations before deployment, require neutral source support, and present company lists as informational options rather than endorsements.

Risk: Personal profile details, report export, email delivery, reminders, memory saving, or follow-up behavior can create privacy and consent risk.

Mitigation: Allow these actions only after explicit user consent, with a known destination or storage location, and avoid saving or sending profile details by default.

Risk: Career planning, salary, demand, and AI-impact guidance may be outdated or overconfident for an individual user's situation.

Mitigation: Frame recommendations as planning support, disclose uncertainty, and encourage users to verify salary, demand, and education requirements against current local sources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [AI Career Impact](references/ai_career_impact.md)
- [Assessment](references/assessment.md)
- [Career Anchor](references/career_anchor.md)
- [Education Paths](references/education_paths.md)
- [Flow Engine](references/flow_engine.md)
- [Industry Trends](references/industry_trends.md)
- [Job Demand](references/job_demand.md)
- [MBTI](references/mbti.md)
- [Salary Data](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Insurance Broker Companies](references/insurance_broker_companies.json)
- [Integrations](references/integrations.md)
- [Tracker System](references/tracker_system.md)
- [2026 Careers](references/emerging_industries/2026_careers.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text and structured Markdown career planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown file export is described by the artifact and should run only after explicit user request.]

## Skill Version(s):

2.2.397 (source: server release metadata; artifact frontmatter reports 2.2.256)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
