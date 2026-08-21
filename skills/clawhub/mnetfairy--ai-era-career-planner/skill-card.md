## Description:

A Chinese-language AI-era career-planning skill that collects user career background, applies Holland, MBTI, and career-anchor assessments, evaluates AI impact, and produces personalized career-planning guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for career planning, major selection, job-transition decisions, and AI-era employability planning. The skill guides a staged conversation, assesses interests and career values, and returns career direction recommendations with AI-impact ratings, learning paths, salary references, and next actions.

### Deployment Geography for Use:

Global, with reference data strongest for China and selected overseas technology roles.

## Known Risks and Mitigations:

Risk: The skill asks users for personal career background, preferences, and career concerns.

Mitigation: Collect only information needed for the career plan and avoid saving, exporting, or sending it unless the user explicitly asks.

Risk: Insurance-company contact information could be mistaken for an endorsement or sales recommendation.

Mitigation: Present it only when insurance careers are relevant, keep the disclosure visible, and tell users to verify company credentials before contacting providers.

Risk: Optional integrations can send email, create subscriptions, write memory, look up live data, or export files.

Mitigation: Use optional integrations only after explicit authorization for the specific action the user requested.

Risk: Career, salary, and AI-impact guidance can become outdated or inaccurate.

Mitigation: Treat recommendations as planning support, surface the bundled data basis where useful, and encourage users to verify current market data before major decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Skill instructions](artifact/SKILL.md)
- [Career planning conversation flow](artifact/references/flow_engine.md)
- [Assessment framework](artifact/references/assessment.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Salary database](artifact/references/salary_database.json)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Insurance company reference data](artifact/references/insurance_broker_companies.json)
- [Optional integration guidance](artifact/references/integrations.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational guidance and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally produce a Markdown report file when the host permits export and the user explicitly asks for it.]

## Skill Version(s):

2.2.315 (source: server release metadata; artifact frontmatter reports 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
