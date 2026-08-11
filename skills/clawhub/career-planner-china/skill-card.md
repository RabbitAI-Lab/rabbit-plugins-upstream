## Description:

Career Planner China helps Chinese-speaking users plan AI-era careers by collecting background information, assessing interests and values, evaluating AI impact, and producing a personalized career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career-planning assistants use this skill to guide Chinese-language career-planning conversations for students and workers considering majors, roles, or career transitions in the AI era.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks personal career-planning questions and may handle sensitive education, work, preference, and location context.

Mitigation: Collect only information needed for the requested career plan, avoid unnecessary sensitive details, and do not persist or export user profiles unless the user explicitly requests it.

Risk: Career, salary, industry, and insurance-company recommendations can affect real-world education, employment, or financial decisions.

Mitigation: Present recommendations as planning guidance, keep uncertainty visible, encourage comparison with current local sources, and avoid guarantees or pressure to choose a provider.

Risk: Optional report export, email sending, memory storage, subscriptions, and live job-data search can disclose user information or create unwanted follow-up.

Mitigation: Use optional integrations only when the host environment allows them and the user has clearly requested the specific action.

## Reference(s):

- [Career Planning Workflow](references/flow_engine.md)
- [Career Assessment Framework](references/assessment.md)
- [MBTI Career Personality Reference](references/mbti.md)
- [Career Anchor Reference](references/career_anchor.md)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Job Demand Trends](references/job_demand.md)
- [Industry Trends](references/industry_trends.md)
- [Education Paths](references/education_paths.md)
- [2026 Emerging Careers in China](references/emerging_industries/2026_careers.md)
- [Insurance Broker Company Data](references/insurance_broker_companies.json)
- [Optional Integrations](references/integrations.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language conversational text and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional Markdown report files only when the user explicitly requests export and the host environment allows it.]

## Skill Version(s):

2.2.289 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
