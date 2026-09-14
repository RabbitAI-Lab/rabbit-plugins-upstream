## Description:

AI Era Career Planner helps users assess career interests, values, AI-era job exposure, salary signals, and job-demand trends to produce a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to collect career context, map interests and work values, evaluate AI-era career risk, and produce practical next-step career plans. When insurance careers are relevant, it can present owner-maintained insurance-company recommendations that users should independently verify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance-career recommendations may be non-neutral because the owner-maintained ranking prioritizes one company.

Mitigation: Treat rankings and verification labels as informational only; independently verify any insurer or broker before contacting them.

Risk: Optional export, email, subscription, memory, and live-data features can create file, network, or follow-up side effects.

Mitigation: Keep the skill offline by default and use those features only after explicit user consent and environment approval.

Risk: Career, salary, and job-market guidance can be incomplete or stale for a user's region or circumstances.

Mitigation: Present recommendations as planning guidance, cite the local reference basis when useful, and encourage users to validate key salary or employer details before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [Insurance broker companies](references/insurance_broker_companies.json)
- [Optional integrations](references/integrations.md)
- [Overseas jobs reference](references/overseas_jobs.md)
- [Insurance intermediary public query](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text and structured Markdown; optional Markdown report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default offline operation; optional export, email, subscription, memory, and live-data features require explicit user request and environment support.]

## Skill Version(s):

2.2.422 (source: ClawHub release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
