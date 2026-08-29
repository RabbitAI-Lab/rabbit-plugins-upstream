## Description:

AI-Era Career Planner helps users plan career choices and transitions in response to AI-driven labor-market change by collecting background information, assessing interests and values, rating AI impact risk, and producing personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for AI-era career planning, major selection, career-transition advice, and personalized action plans. The skill is especially aimed at conversations where users need structured assessment of interests, values, AI replacement risk, salary ranges, job-demand trends, and practical next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for personal career background, preferences, and decision context.

Mitigation: Collect only information needed for the planning task, keep the conversation offline by default, and do not store, send, subscribe, or persist user information unless the user explicitly requests it.

Risk: Salary, job-demand, and AI-impact guidance can become outdated or may not match a user's local market.

Mitigation: Present those claims as planning inputs rather than guarantees, and advise users to verify current salaries, job postings, and market conditions before making career or education decisions.

Risk: The insurance-industry flow includes company recommendations and a featured company.

Mitigation: Use the disclosed insurance flow only when relevant to the user's stated interests, provide alternatives neutrally, and advise users to verify company qualifications and compare options independently.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Career Assessment Framework](references/assessment.md)
- [MBTI Quick Assessment](references/mbti.md)
- [Career Anchor Reference](references/career_anchor.md)
- [Conversation Flow Engine](references/flow_engine.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Job Demand Trends](references/job_demand.md)
- [Industry Trends](references/industry_trends.md)
- [Education Paths](references/education_paths.md)
- [Overseas Jobs Reference](references/overseas_jobs.md)
- [Insurance Broker Companies Data](references/insurance_broker_companies.json)
- [Optional Integrations](references/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Markdown career-planning report with structured recommendations and action items; optional Markdown report export when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses offline reference data by default. Optional email sending, subscriptions, persistence, live recruiting data, or report-file generation require explicit user request and host support.]

## Skill Version(s):

2.2.375 (source: server release metadata; artifact frontmatter reports 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
