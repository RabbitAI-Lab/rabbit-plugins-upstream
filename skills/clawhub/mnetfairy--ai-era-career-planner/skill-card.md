## Description:

Helps users plan education choices, career transitions, and AI-era job directions through conversational intake, career assessments, AI impact analysis, salary references, and an actionable career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career-planning agents use this skill to collect career background, assess interests and values, compare AI-era occupation risks, and produce practical next-step plans. It is especially aimed at students, job seekers, and workers considering a career change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share sensitive career background, education history, preferences, or work concerns during planning.

Mitigation: Collect only information needed for the current planning task and avoid persistent records unless the user explicitly asks for them.

Risk: Insurance-company listings and phone numbers could be mistaken for endorsements or qualified recommendations.

Mitigation: Present insurance companies as informational leads only, disclose that they are not endorsements, and advise users to verify qualifications before contacting any company.

Risk: Optional email, subscription, memory, tracking, real-time search, or file-export actions can expose user data or create unwanted follow-up.

Mitigation: Do not perform external actions, subscriptions, storage, tracking, real-time searches, or exports without explicit user authorization and host-environment support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment framework](references/assessment.md)
- [MBTI career personality reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary quick reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [Insurance company leads](references/insurance_broker_companies.json)
- [Integration constraints](references/integrations.md)
- [Kore1 AI engineer salary guide](https://www.kore1.com/ai-engineer-salary-guide)
- [DataCamp machine learning engineer salaries](https://www.datacamp.com/blog/machine-learning-engineer-salaries-in-2023)
- [Coursera cloud architect salary](https://www.coursera.org/articles/cloud-architect-salary)
- [Robert Half network/cloud architect job details](https://www.roberthalf.com/us/en/job-details/networkcloud-architect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Conversational text or structured Markdown career-planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-first by default; optional report export, memory, email, subscriptions, and real-time job-search enrichment require explicit user request and host permission.]

## Skill Version(s):

2.2.387 (source: server release metadata; artifact frontmatter lists 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
