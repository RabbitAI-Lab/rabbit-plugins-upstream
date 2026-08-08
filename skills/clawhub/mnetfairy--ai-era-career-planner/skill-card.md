## Description:

AI-era career planning assistant for career advice, major selection, workplace transition, and future job direction, using progressive intake, Holland/RIASEC, MBTI, career anchors, AI impact ratings, salary references, and personalized planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to explore career direction in the AI era, including education choices, role transitions, industry fit, AI replacement risk, salary ranges, and concrete next actions. It is especially oriented toward Chinese-language career planning workflows with optional international technology job references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for personal education, work history, preferences, goals, and location to generate career advice.

Mitigation: Collect only information the user chooses to provide, avoid unnecessary sensitive details, and do not persist or export records unless the user explicitly asks.

Risk: Career, salary, AI-impact, and insurance-company recommendations may be incomplete, dated, or unsuitable for a user's local circumstances.

Mitigation: Present recommendations as planning guidance, encourage independent verification, and ask users to confirm company qualifications before contacting insurance providers.

Risk: Optional integrations can send reports, subscribe users to updates, perform live lookups, or save follow-up records.

Mitigation: Use these integrations only when the environment allows them and the user gives explicit approval for each external action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Skill definition](artifact/SKILL.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [Career anchor reference](artifact/references/career_anchor.md)
- [Conversation flow engine](artifact/references/flow_engine.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Salary database](artifact/references/salary_database.json)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Education paths](artifact/references/education_paths.md)
- [Insurance company reference data](artifact/references/insurance_broker_companies.json)
- [Optional integrations reference](artifact/references/integrations.md)
- [Optional tracking system reference](artifact/references/tracker_system.md)
- [Overseas jobs reference](artifact/references/overseas_jobs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration, shell commands]

**Output Format:** [Markdown career planning report with structured recommendations, ratings, salary notes, action lists, and optional generated Markdown export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically produces conversational guidance; optional report export writes a Markdown file only when the host environment allows it and the user explicitly requests it.]

## Skill Version(s):

2.2.278 (source: server release metadata; artifact frontmatter says 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
