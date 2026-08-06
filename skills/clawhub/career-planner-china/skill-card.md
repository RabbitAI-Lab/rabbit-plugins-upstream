## Description:

Career Planner China helps users in China explore education, career planning, career transitions, AI-era job risk, salary ranges, and personalized next-step plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to collect career background, assess interests and work values, compare AI-era career impact, and produce a personalized career planning report for China-focused education and job-market decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may request personal career background, education history, goals, location, and work preferences.

Mitigation: Collect only details needed for the current planning request, avoid unnecessary persistence, and use memory or tracking only after explicit user consent.

Risk: Salary ranges, job demand, emerging-career claims, and company recommendations can become stale or may not match a user's local market.

Mitigation: Treat recommendations as planning support, cite the packaged data source when used, and ask users to verify salary and company information independently before acting.

Risk: Insurance-company suggestions could be interpreted as financial or sales advice.

Mitigation: Provide them only when the user expresses interest in insurance careers, keep the recommendations comparative, and preserve the artifact's disclaimer that users should compare options themselves.

Risk: Optional integrations can send email, subscribe users to updates, persist records, or perform live recruiting lookup.

Mitigation: Enable those actions only when the environment supports them and the user explicitly requests the specific action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Salary database](artifact/references/salary_database.json)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Education paths](artifact/references/education_paths.md)
- [Insurance broker company data](artifact/references/insurance_broker_companies.json)
- [Optional integrations](artifact/references/integrations.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational text and structured Markdown career planning reports; optional Markdown report files when export is explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local reference data by default; optional export, memory, email, subscription, or live lookup features require explicit user request and host support.]

## Skill Version(s):

2.2.279 (source: server release evidence; artifact frontmatter lists 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
