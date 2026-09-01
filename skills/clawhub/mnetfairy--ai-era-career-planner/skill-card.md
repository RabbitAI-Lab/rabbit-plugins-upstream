## Description:

AI-era career-planning skill that collects user context, assesses career interests and values, evaluates AI impact risk, and produces a personalized career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for AI-era career planning, school or major selection, career transitions, and job-direction decisions. It guides a staged conversation, applies career-interest and values frameworks, adds salary and demand references, and returns practical next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for personal career background and preferences.

Mitigation: Collect only information needed for the planning task and do not persist user details unless the user explicitly requests it.

Risk: Career, salary, job-demand, and overseas-market references may become outdated or may not fit a user's location or circumstances.

Mitigation: Present recommendations as planning guidance and encourage users to verify current market, education, visa, certification, and compensation details before acting.

Risk: Insurance-company recommendations could be mistaken for endorsement or sales advice.

Mitigation: Keep insurance-company information informational, disclose limitations, and advise users to compare options and confirm company qualifications before contact.

Risk: Optional file generation, external service use, subscriptions, email delivery, or memory/tracking workflows could expose user information or create unwanted follow-up.

Mitigation: Use those features only after explicit user authorization and only when the current host environment supports the requested action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](references/ai_career_impact.md)
- [Career assessment framework](references/assessment.md)
- [Career anchor reference](references/career_anchor.md)
- [Education paths](references/education_paths.md)
- [Conversation flow engine](references/flow_engine.md)
- [Industry trends](references/industry_trends.md)
- [Job demand trends](references/job_demand.md)
- [MBTI career reference](references/mbti.md)
- [Overseas jobs reference](references/overseas_jobs.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Kore1 AI engineer salary guide](https://www.kore1.com/ai-engineer-salary-guide)
- [DataCamp machine learning engineer salary article](https://www.datacamp.com/blog/machine-learning-engineer-salaries-in-2023)
- [Coursera cloud architect salary article](https://www.coursera.org/articles/cloud-architect-salary)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code]

**Output Format:** [Markdown career-planning report with structured recommendations, ratings, salary references, and action lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional Markdown report files or local tracking content only when the user explicitly requests them and the host environment allows it.]

## Skill Version(s):

2.2.381 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
