## Description:

A Chinese-language career planning skill that gathers user background and preferences, assesses career interests and AI-era job impact, and produces personalized career direction reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors can use this skill to guide Chinese-language conversations about education choices, career transitions, AI exposure, salary expectations, and next-step action plans.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks for personal career, education, preference, and city information to produce tailored advice.

Mitigation: Collect only the information needed for the current planning conversation and avoid entering unnecessary sensitive details.

Risk: Salary figures and insurance-company recommendations may be incomplete, stale, or not suitable for a user's exact circumstances.

Mitigation: Independently verify salary data and insurance-company recommendations before making career or financial decisions.

Risk: Optional report export, memory storage, email sending, subscriptions, and live job-data lookup can expose user data or create follow-up actions.

Mitigation: Use optional exports and integrations only when the user explicitly requests them and the host environment permits the action.

## Reference(s):

- [Skill definition](SKILL.md)
- [Conversation flow engine](references/flow_engine.md)
- [Career assessment framework](references/assessment.md)
- [MBTI career fit reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Industry trends](references/industry_trends.md)
- [Job demand trends](references/job_demand.md)
- [Education paths](references/education_paths.md)
- [Salary quick reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Optional integrations](references/integrations.md)
- [Career tracking system](references/tracker_system.md)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Publisher profile](https://clawhub.ai/user/mnetfairy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Chinese-language conversational text and structured Markdown career planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown report export is available only when the host environment permits it and the user explicitly requests export.]

## Skill Version(s):

2.2.380 (source: server release metadata and target metadata; SKILL.md frontmatter lists 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
