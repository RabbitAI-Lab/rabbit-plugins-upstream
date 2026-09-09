## Description:

Generates personalized AI-era career planning guidance, including user profiling, Holland interest assessment, career values, AI impact ratings, salary context, learning paths, and actionable next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to structure career-planning conversations, assess fit and values, estimate AI disruption risk, compare industry paths, and produce a personalized career plan. It can optionally export the plan as Markdown when the user explicitly asks for a report file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance-career recommendations may prioritize one named company as the maintainer's disclosed business preference rather than an impartial ranking.

Mitigation: Before relying on insurance-related recommendations, independently verify company qualifications, regional availability, and contact details, and disclose that the first-ranked company reflects a maintainer preference.

Risk: Users may mistake career recommendations, salary ranges, or AI impact ratings for certain predictions.

Mitigation: Present outputs as planning guidance, compare them with current local market data, and ask users to validate important career or education decisions with additional sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact](references/ai_career_impact.md)
- [Assessment methods](references/assessment.md)
- [Career anchors](references/career_anchor.md)
- [Education paths](references/education_paths.md)
- [Industry trends](references/industry_trends.md)
- [Job demand](references/job_demand.md)
- [Salary data](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Insurance broker companies](references/insurance_broker_companies.json)
- [Integrations](references/integrations.md)
- [Overseas jobs](references/overseas_jobs.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown career plan with structured recommendations and optional exported Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assessment labels, AI impact ratings, salary ranges, industry-specific recommendations, action timelines, and optional report-file export when explicitly requested.]

## Skill Version(s):

2.2.400 (source: server release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
