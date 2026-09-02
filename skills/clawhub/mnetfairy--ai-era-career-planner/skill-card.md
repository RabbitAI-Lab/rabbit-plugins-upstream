## Description:

AI Era Career Planner helps users explore career paths in the AI era by collecting profile details, assessing interests and values, evaluating AI impact risk, and producing personalized career-planning guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for career planning, major selection, job-transition decisions, and AI-era employment direction. The agent guides a staged conversation, applies career-interest and value frameworks, and returns concrete recommendations with AI impact ratings, salary context, learning paths, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Embedded insurance-company recommendations may be informationally stale or commercially biased.

Mitigation: Treat insurance-company entries as informational only, disclose the limitation, and verify company details before contacting or recommending a provider.

Risk: Career, salary, and labor-market guidance can become outdated or may not fit a user's region or personal circumstances.

Mitigation: Present recommendations as planning guidance rather than guarantees, cite the local reference data basis when useful, and encourage users to verify time-sensitive salary, hiring, and credential details.

Risk: Optional export, tracking, email, subscription, or external-data features could persist or transmit user career information if used casually.

Mitigation: Use those features only after explicit user request and confirmation, minimize stored data, and let users control any destination or follow-up behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](references/ai_career_impact.md)
- [Career assessment framework](references/assessment.md)
- [Career anchors reference](references/career_anchor.md)
- [Conversation flow engine](references/flow_engine.md)
- [Industry trends reference](references/industry_trends.md)
- [Job demand trends](references/job_demand.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Overseas jobs reference](references/overseas_jobs.md)
- [Optional integrations reference](references/integrations.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, text, configuration]

**Output Format:** [Conversational text and Markdown career-planning reports; optional Markdown file export when explicitly requested by the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured career recommendations, assessment labels, AI impact ratings, salary ranges, learning paths, and action plans.]

## Skill Version(s):

2.2.383 (source: server release metadata and target metadata; artifact frontmatter lists 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
