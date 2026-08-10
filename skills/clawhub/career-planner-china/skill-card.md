## Description:

Career Planner China helps users explore career planning, major selection, career transitions, and AI-era job-market risks through progressive information gathering, career-interest assessment, values analysis, and a personalized career-planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to receive conversational career-planning guidance tailored to China-focused career paths, salary references, industry trends, and AI impact ratings. It can also produce a structured Markdown career-planning report when the user explicitly asks for an exportable report.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask for personal career background, education, preferences, and goals.

Mitigation: Collect only information needed for the requested career guidance and do not persist, email, or share user details unless the user explicitly requests that behavior.

Risk: Career, salary, hiring-demand, and AI-impact guidance can become stale or may not fit a user's exact location or circumstances.

Mitigation: Present recommendations as advisory planning support and encourage users to verify material decisions against current job postings, schools, employers, or qualified professionals.

Risk: Optional export, email, subscription, realtime lookup, and memory features may transmit or persist user data.

Mitigation: Use those integrations only after an explicit user request and only when the host environment permits the action.

Risk: Insurance-company suggestions could be perceived as a financial or employment endorsement.

Mitigation: Keep insurance-company listings neutral, disclose that they are references only, and advise users to compare options independently.

## Reference(s):

- [Career Planning Conversation Flow](references/flow_engine.md)
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
- [Insurance Broker Companies](references/insurance_broker_companies.json)
- [Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Publisher Profile](https://clawhub.ai/user/mnetfairy)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Conversational text and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional report export, email, subscription, realtime lookup, and memory tracking behaviors are only for explicit user requests in environments that allow them.]

## Skill Version(s):

2.2.287 (source: server release evidence; artifact frontmatter shows 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
