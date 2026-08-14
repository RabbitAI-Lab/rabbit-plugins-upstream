## Description:

AI-era career planning skill for Chinese-language users that gathers user background, applies Holland interest, MBTI, career-anchor, and values assessments, evaluates AI career impact, and produces a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for Chinese-language career planning, major selection, career transition decisions, and AI-era job risk analysis. The skill guides the conversation, uses bundled assessment and labor-market references, and returns practical career directions, skill-building advice, and next actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional email, subscription, memory, and live hiring-data integrations can save, send, or expose user career details outside the immediate conversation.

Mitigation: Enable those features only after an explicit user request and after confirming the host environment supports the requested action.

Risk: Insurance-company recommendations could be interpreted as financial advice or a neutral market ranking.

Mitigation: Present insurance recommendations as informational only, preserve the artifact disclaimer, and encourage users to compare options independently.

Risk: Career planning and AI impact ratings can be incorrect, outdated, or overly deterministic for an individual user.

Mitigation: Frame recommendations as planning guidance, explain uncertainty, and encourage users to validate choices with current job-market data and personal constraints.

## Reference(s):

- [Skill Definition](artifact/SKILL.md)
- [AI Career Impact](artifact/references/ai_career_impact.md)
- [Assessment Framework](artifact/references/assessment.md)
- [Career Anchor](artifact/references/career_anchor.md)
- [MBTI](artifact/references/mbti.md)
- [Salary Data](artifact/references/salary_data.md)
- [Salary Database](artifact/references/salary_database.json)
- [Job Demand](artifact/references/job_demand.md)
- [Industry Trends](artifact/references/industry_trends.md)
- [Education Paths](artifact/references/education_paths.md)
- [2026 Emerging Careers](artifact/references/emerging_industries/2026_careers.md)
- [Insurance Broker Companies](artifact/references/insurance_broker_companies.json)
- [Integrations](artifact/references/integrations.md)
- [Tracker System](artifact/references/tracker_system.md)
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown career-planning report with structured sections and optional tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are normally conversational and offline-first; optional report export, email, subscription, memory, and live hiring-data features require explicit user request and host support.]

## Skill Version(s):

2.2.297 (source: server release metadata; artifact frontmatter says 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
