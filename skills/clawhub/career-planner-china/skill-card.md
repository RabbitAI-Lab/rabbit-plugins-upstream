## Description:

AI-era career planning skill for China-focused users that gathers career context, assesses interests and values, evaluates AI disruption risk, and produces personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to plan education, career direction, job transitions, and AI-era skill development with China-focused salary, demand, industry, and learning-path references. The skill is intended to produce practical career recommendations, next actions, and optional report exports when the user requests them.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask for personal career context.

Mitigation: Users should provide only details needed for planning and avoid unnecessary sensitive personal information.

Risk: Career, salary, and company recommendations may be biased, dated, or incomplete.

Mitigation: Users should treat recommendations as planning support, compare salary and company suggestions independently, and verify insurance-company options before acting.

Risk: Optional exports, email delivery, subscriptions, memory, live-data lookups, or tracking can persist or transmit user information.

Mitigation: Run these actions only when the user explicitly requests and approves the specific export, email, subscription, memory, or live-data action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Skill Definition](artifact/SKILL.md)
- [AI Career Impact Reference](artifact/references/ai_career_impact.md)
- [Career Assessment Framework](artifact/references/assessment.md)
- [MBTI Reference](artifact/references/mbti.md)
- [Career Anchor Reference](artifact/references/career_anchor.md)
- [Salary Data Reference](artifact/references/salary_data.md)
- [Salary Database](artifact/references/salary_database.json)
- [Job Demand Trends](artifact/references/job_demand.md)
- [Industry Trends](artifact/references/industry_trends.md)
- [Education Paths](artifact/references/education_paths.md)
- [Insurance Broker Company Data](artifact/references/insurance_broker_companies.json)
- [2026 Emerging Careers](artifact/references/emerging_industries/2026_careers.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown career planning report with structured recommendations and optional Markdown export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include user-profile summaries, career fit assessments, AI-impact ratings, salary ranges, learning paths, action checklists, and optional user-approved export or integration guidance.]

## Skill Version(s):

2.2.369 (source: server release evidence; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
