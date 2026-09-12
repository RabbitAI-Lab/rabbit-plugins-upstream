## Description:

Career Planner China helps Chinese-speaking users assess career interests, values, AI-era job exposure, salary context, and industry pathways to produce personalized career-planning guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users, students, and workers in China use this skill to explore majors, career transitions, job recommendations, AI impact ratings, salary ranges, and practical next steps. It can also provide China-focused industry modules and optional insurance-industry onboarding information when relevant.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may process sensitive personal career-profile details.

Mitigation: Collect only information needed for the requested planning task, keep outputs user-visible, and avoid persistence unless the user explicitly asks for it.

Risk: Optional integrations could email, subscribe, look up realtime data, write memory, or export a report.

Mitigation: Require explicit user confirmation before each integration, confirm any destination or recipient, and keep the default workflow offline.

Risk: Insurance company rankings and verified labels may be perceived as neutral or regulator-validated recommendations.

Mitigation: Present insurance entries as informational, disclose the stated priority basis, hide contact details until the user consents, and advise users to compare options independently.

Risk: Report export can create files through the bundled report-generation script.

Mitigation: Run report export only when the user explicitly requests it and confirm the output location before generating a file.

## Reference(s):

- [AI Career Impact](references/ai_career_impact.md)
- [Assessment](references/assessment.md)
- [Career Anchor](references/career_anchor.md)
- [Education Paths](references/education_paths.md)
- [Flow Engine](references/flow_engine.md)
- [Industry Trends](references/industry_trends.md)
- [Job Demand](references/job_demand.md)
- [MBTI](references/mbti.md)
- [Salary Data](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Insurance Broker Companies](references/insurance_broker_companies.json)
- [Integrations](references/integrations.md)
- [Tracker System](references/tracker_system.md)
- [2026 Careers](references/emerging_industries/2026_careers.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown career-planning report with structured recommendations, ratings, salary context, and action lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional report-export instructions only when the user explicitly requests an exported report.]

## Skill Version(s):

2.2.417 (source: server release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
