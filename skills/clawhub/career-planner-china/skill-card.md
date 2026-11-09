## Description:

Provides China-focused career planning by gathering a user profile, assessing interests and values, evaluating AI's likely career impact, and producing a personalized planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

For people in China exploring study choices, career direction, or a career transition. It uses a gradual interview, interest and values assessments, and local career references to produce a structured, personalized plan.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan flags filesystem write paths and long-term profile storage; its review of the salary database is incomplete.

Mitigation: Restrict writes to approved locations and use export or tracking only when explicitly requested. Review the salary database separately before relying on its contents.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career assessment and planning workflow](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary data guidance](references/salary_data.md)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education pathways](references/education_paths.md)
- [Insurance broker company data](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured personalized career-planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill defaults to offline use. Report export and persistent tracking are opt-in. Insurance recommendations disclose a maintainer-selected priority; career and salary assessments are advisory.]

## Skill Version(s):

2.3.7 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
