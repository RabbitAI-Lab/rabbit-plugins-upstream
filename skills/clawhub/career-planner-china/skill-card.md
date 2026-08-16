## Description:

A China-focused AI-era career planning skill that helps users assess interests, values, AI career impact, salary ranges, job-demand trends, and education paths to produce personalized career guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to explore career paths in China, including student major selection, early-career planning, workplace transition, and AI-era reskilling. The skill gathers career context conversationally and returns actionable recommendations with AI-impact ratings, salary references, learning paths, and next steps.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks users for personal career context, education background, goals, and location details.

Mitigation: Collect only information needed for the current planning task and avoid saving, sharing, emailing, or subscribing the user unless they explicitly request it.

Risk: Career, salary, AI-impact, and company recommendations can become outdated or may not fit an individual user's circumstances.

Mitigation: Present recommendations as planning guidance, include uncertainty where appropriate, and encourage users to compare options and verify current details before making employment, education, or insurance decisions.

Risk: Optional integrations can email reports, subscribe users to updates, write memory, fetch live data, or run report-generation scripts.

Mitigation: Use optional integrations only after explicit user authorization and only when the host environment supports the requested action.

## Reference(s):

- [Career Planning Workflow](references/flow_engine.md)
- [Assessment Framework](references/assessment.md)
- [MBTI Career Reference](references/mbti.md)
- [Career Anchor Reference](references/career_anchor.md)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Job Demand Trends](references/job_demand.md)
- [Industry Trends](references/industry_trends.md)
- [Education Paths](references/education_paths.md)
- [2026 Emerging Careers China](references/emerging_industries/2026_careers.md)
- [Insurance Broker Companies](references/insurance_broker_companies.json)
- [Optional Integrations](references/integrations.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Text, Markdown]

**Output Format:** [Conversational text or structured Markdown career-planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include career direction rankings, AI-impact ratings, salary references, learning paths, risk notes, and optional user-authorized report export.]

## Skill Version(s):

2.2.303 (source: evidence.release.version; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
