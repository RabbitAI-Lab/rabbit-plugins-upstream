## Description:

Career Planner China helps Chinese-speaking users build AI-era career plans with conversational intake, career-interest assessment, AI impact ratings, salary references, industry trends, and personalized action plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, students, and career changers use this skill to explore China-focused career directions, compare AI disruption risk, review salary and job-demand signals, and receive a personalized plan with near-term actions. Agents can also use it to generate a Markdown career-planning report when the user explicitly requests export.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask for personal career, education, location, and preference details.

Mitigation: Collect only details needed for the planning task and avoid storing a long-term profile unless the user explicitly asks for tracking.

Risk: Optional integrations can send email, subscribe the user to updates, persist memory, fetch realtime web data, or export a report file.

Mitigation: Use these integrations only when the current environment allows them and the user clearly approves the specific action.

Risk: Career, salary, and AI-disruption guidance can be uncertain or time-sensitive.

Mitigation: Present recommendations as planning support rather than guarantees, and encourage users to compare current local market evidence before making major decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career assessment framework](artifact/references/assessment.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Detailed salary database](artifact/references/salary_database.json)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [2026 emerging careers](artifact/references/emerging_industries/2026_careers.md)
- [Insurance broker companies](artifact/references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational text and structured Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-first by default; optional report export, email sending, memory tracking, subscriptions, and realtime web data require explicit user permission.]

## Skill Version(s):

2.2.301 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
