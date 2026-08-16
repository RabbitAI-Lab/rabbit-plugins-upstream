## Description:

AI-era career planning skill that helps users assess career interests, values, AI exposure, salary expectations, job demand, and education paths to produce personalized career planning guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users, students, job seekers, and workers in career transition use this skill to discuss goals, interests, education background, and market context, then receive personalized career direction recommendations and action plans. The skill is especially focused on how AI changes career risk, opportunity, skill needs, and job-market positioning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for personal career goals, education, preferences, and location to tailor advice.

Mitigation: Share only information needed for the planning conversation, and use optional tracking or memory features only after explicit user authorization.

Risk: Salary, job-demand, and insurance-company references may be incomplete, stale, or unsuitable for a specific user decision.

Mitigation: Treat those references as planning inputs, verify important facts independently, and avoid treating company listings as endorsements.

Risk: Optional exports, email delivery, subscriptions, memory, or live data lookup can transmit or persist user-provided information.

Mitigation: Enable those actions only when the user explicitly requests them and the host environment supports the requested operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary data quick reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Optional integrations](references/integrations.md)
- [Career tracking system](references/tracker_system.md)
- [KORE1 AI engineer salary guide](https://www.kore1.com/ai-engineer-salary-guide)
- [DataCamp machine learning engineer salary article](https://www.datacamp.com/blog/machine-learning-engineer-salaries-in-2023)
- [Robert Half cloud architect salary reference](https://www.roberthalf.com/us/en/job-details/networkcloud-architect)
- [Coursera cloud architect salary article](https://www.coursera.org/articles/cloud-architect-salary)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational text and structured Markdown career planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled reference data by default; optional report export, email, subscriptions, memory, or live data lookup are only used when explicitly requested and supported by the host environment.]

## Skill Version(s):

2.2.298 (source: server release metadata; artifact frontmatter lists 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
