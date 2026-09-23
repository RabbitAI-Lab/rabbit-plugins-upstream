## Description:

AI-Era Career Planner helps users plan careers for an AI-shaped labor market by collecting career-stage context, applying career-interest and values assessments, rating AI impact risk, and producing personalized planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to generate AI-era career guidance, including career-direction recommendations, Holland/MBTI/career-anchor style assessments, salary and demand context, education paths, and next-step action plans. It is especially oriented toward Chinese-language career planning, school major selection, career transitions, and AI displacement or opportunity questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance-company suggestions may function as commercial guidance, including a preferred company and phone-number display path.

Mitigation: Verify insurance-company qualifications and compare alternatives independently before acting on any recommendation or contacting a company.

Risk: Packaged salary, job-demand, and company datasets may be incomplete, stale, or weakly sourced for some regions and roles.

Mitigation: Treat salary and demand figures as planning context and confirm important decisions against current local market sources.

Risk: Optional emailing, subscriptions, networking, memory, and report export create side effects when explicitly requested.

Mitigation: Use optional integrations only after an explicit user request and confirm destination, persistence, and export path before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](references/ai_career_impact.md)
- [Career assessment framework](references/assessment.md)
- [Salary quick reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [Insurance broker company dataset](references/insurance_broker_companies.json)
- [Overseas jobs reference](references/overseas_jobs.md)
- [Integration behavior reference](references/integrations.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)
- [Kore1 AI engineer salary guide](https://www.kore1.com/ai-engineer-salary-guide)
- [DataCamp machine learning engineer salary guide](https://www.datacamp.com/blog/machine-learning-engineer-salaries-in-2023)
- [Coursera cloud architect salary guide](https://www.coursera.org/articles/cloud-architect-salary)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration, shell commands]

**Output Format:** [Markdown career-planning report with optional exported Markdown file on explicit request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default behavior is conversational and offline; optional report export uses a constrained local exports directory, and optional integrations require explicit user request and host support.]

## Skill Version(s):

2.2.440 (source: server release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
