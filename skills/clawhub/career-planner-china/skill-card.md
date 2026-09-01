## Description:

Career Planner China helps users explore career plans for the AI era using conversational assessment, China-focused salary and job-demand references, AI impact ratings, and structured personalized recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to collect career background, assess interests and values, compare AI-era career risk, and receive a China-focused career plan with recommended directions, salary context, learning paths, and next actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask for personal career details and preferences.

Mitigation: Collect only information needed for the requested career plan and avoid saving or exporting it unless the user explicitly asks.

Risk: Career, salary, and AI-impact guidance can be uncertain or become outdated.

Mitigation: Present recommendations as planning support rather than predictions, and encourage users to verify salary, demand, certification, and hiring information before acting.

Risk: The skill can optionally export reports, save tracking records, send email, subscribe to updates, or use live recruiting data.

Mitigation: Perform those actions only after explicit user authorization and only when the host environment supports them.

Risk: Insurance-company recommendations may influence financial or employment decisions.

Mitigation: Keep recommendations informational and advise users to independently compare companies before choosing a role or provider.

## Reference(s):

- [Skill definition](SKILL.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career assessment framework](references/assessment.md)
- [MBTI career reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [Conversation flow engine](references/flow_engine.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md)
- [Technology career module](references/industries/tech_career.md)
- [Healthcare career module](references/industries/healthcare.md)
- [Finance career module](references/industries/finance.md)
- [Education career module](references/industries/education.md)
- [Creative career module](references/industries/creative.md)
- [Manufacturing career module](references/industries/manufacturing.md)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Optional integrations](references/integrations.md)
- [Optional tracking system](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code]

**Output Format:** [Markdown career-planning report with structured recommendations; optional Markdown report file when export is explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled reference data by default; optional external actions, tracking, email, subscriptions, live recruiting data, and report export require user request and host support.]

## Skill Version(s):

2.2.386 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
