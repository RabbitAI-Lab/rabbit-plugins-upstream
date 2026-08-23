## Description:

Career Planner China helps users navigate AI-era career planning by collecting background details, assessing career interests and values, evaluating AI impact risk, and producing a personalized career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users, students, and career changers use this skill to explore China-focused career directions, education paths, salary expectations, job-demand trends, and AI-era replacement risk. The agent produces structured, actionable guidance rather than taking external actions by default.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask for personal education, work history, preferences, and career-goal details.

Mitigation: Share only details needed for the planning task and avoid unnecessary sensitive personal information.

Risk: Optional report export, memory tracking, email sending, subscriptions, or live recruitment-data lookup may store, transmit, or retrieve user data.

Mitigation: Approve optional actions only when explicitly desired and supported by the host environment.

Risk: Insurance-company recommendations and contact details may be incomplete, outdated, or unsuitable for a user's circumstances.

Mitigation: Independently verify insurance-company details and compare options before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career-planning conversation flow](references/flow_engine.md)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchor reference](references/career_anchor.md)
- [MBTI career personality reference](references/mbti.md)
- [Salary data reference](references/salary_data.md)
- [Detailed salary database](references/salary_database.json)
- [Job-demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Optional integrations reference](references/integrations.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese conversational text or Markdown career-planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include career-fit assessments, AI impact ratings, salary ranges, learning paths, and next-step action lists.]

## Skill Version(s):

2.2.325 (source: server release evidence; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
