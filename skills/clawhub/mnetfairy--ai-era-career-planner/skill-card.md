## Description:

AI-era Career Planner helps an agent collect career context, assess interests and values, evaluate AI impact on career paths, and produce personalized career-planning guidance with salary, industry, and learning-path context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career-planning assistants use this skill to guide students, job seekers, and career changers through structured career discovery, AI-era risk assessment, role recommendations, salary context, and next-step action planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users for personal career, education, preference, location, and planning information.

Mitigation: Collect only information needed for the current planning step and do not save profiles, tracking records, or memory unless the user explicitly asks for it.

Risk: Insurance-company recommendations may include source notes that are unverified or dated.

Mitigation: Present insurance company data as informational only, disclose that it is not an endorsement, and advise users to verify company credentials before contacting providers.

Risk: External email, subscriptions, live recruiting data, memory, or follow-up tracking could expose user data or create unwanted contact.

Mitigation: Use those integrations only after an explicit user request and confirmation for the specific action.

Risk: Career recommendations and AI-impact ratings can be uncertain or become stale as labor markets change.

Mitigation: Frame plans as probabilistic guidance, include concrete next steps, and encourage users to compare recommendations against current local market information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Skill instructions](SKILL.md)
- [Conversation flow engine](references/flow_engine.md)
- [Career assessment framework](references/assessment.md)
- [MBTI quick reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Optional integrations](references/integrations.md)
- [Optional tracking system](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational Markdown career-planning report; optional Markdown report file only when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled career, salary, assessment, industry, and insurance reference data; external sending, subscriptions, live data, memory, and tracking require explicit user request and approval.]

## Skill Version(s):

2.2.274 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
