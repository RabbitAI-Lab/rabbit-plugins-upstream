## Description:

Provides AI-era career planning guidance by collecting user profile details, assessing career interests and values, estimating AI impact on career options, and producing a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to explore career direction, education choices, career changes, and AI-era job risk. It produces structured recommendations, learning paths, salary and demand context, and next-step action plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a built-in preference in insurance-company recommendations.

Mitigation: Treat insurance-company rankings as the publisher's preference, not an independent comparison; verify company licensing, fit, and contact details before acting.

Risk: Optional report export may write or overwrite a same-day report file.

Mitigation: Export only to a user-controlled directory where overwriting an existing report is acceptable.

Risk: Career, salary, and job-demand recommendations can be outdated or incomplete.

Mitigation: Use the report as planning guidance and validate important career, salary, licensing, and hiring information against current primary sources before making decisions.

## Reference(s):

- [AI Career Impact Reference](references/ai_career_impact.md)
- [Career Assessment Framework](references/assessment.md)
- [Career Dialogue Flow Engine](references/flow_engine.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Job Demand Trends](references/job_demand.md)
- [Industry Trends](references/industry_trends.md)
- [Insurance Broker Company Data](references/insurance_broker_companies.json)
- [Optional Integrations](references/integrations.md)
- [Career Planning Tracker](references/tracker_system.md)
- [Overseas Jobs Reference](references/overseas_jobs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Conversational text and structured Markdown career planning reports; optional Markdown export when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local reference data by default; optional network or messaging integrations require explicit user request and host support.]

## Skill Version(s):

2.2.392 (source: server release metadata; artifact frontmatter lists 2.2.251)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
