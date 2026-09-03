## Description:

This skill helps Chinese-speaking users plan careers for the AI era by collecting career context, assessing interests and values, evaluating AI disruption risk, and producing a personalized career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to guide Chinese career-planning conversations, assess Holland, MBTI, and career-anchor signals, compare AI impact and labor-market data, and produce practical next-step plans.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks users for personal career context such as age or stage, education, interests, values, goals, and city.

Mitigation: Collect only information needed for the planning task and avoid storing or sharing it unless the user explicitly authorizes that behavior.

Risk: Salary figures, job-demand trends, and insurance-company recommendations may be incomplete, stale, or advisory rather than definitive.

Mitigation: Tell users to verify salary, hiring, and financial-service information independently before making career or financial decisions.

Risk: Optional email, subscription, memory, tracking, or real-time-search integrations can send, store, refresh, or follow up on user information externally.

Mitigation: Use optional integrations only after explicit user request and only when the host environment permits them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career-planning conversation flow](references/flow_engine.md)
- [Career assessment framework](references/assessment.md)
- [MBTI career personality reference](references/mbti.md)
- [Career-anchor reference](references/career_anchor.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary data reference](references/salary_data.md)
- [Detailed salary database](references/salary_database.json)
- [Job-demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Optional integration notes](references/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese conversational guidance and structured Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include salary ranges, AI impact ratings, learning paths, action plans, and optional Markdown report files when explicitly requested.]

## Skill Version(s):

2.2.390 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
