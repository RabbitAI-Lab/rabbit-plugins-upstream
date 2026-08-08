## Description:

This Chinese-language career-planning skill gathers user background, applies interest and values assessments, evaluates AI-era career impact, and produces personalized career direction reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for China-oriented career planning, major selection, career-transition guidance, AI substitution-risk assessment, and structured next-step planning. The skill is also useful to advisors who need a guided conversation flow and bundled reference data for career reports.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Career recommendations, salary estimates, AI-risk labels, and insurance-company suggestions may be outdated, incomplete, or unsuitable for a user's local circumstances.

Mitigation: Present them as planning inputs, encourage independent verification against current local market data, and avoid treating them as guarantees.

Risk: The skill may ask for personal career background, education, goals, location, and preference information.

Mitigation: Ask only for details needed for the planning task and avoid storing user profiles unless the user explicitly requests it.

Risk: Optional email, subscription, memory, realtime lookup, or report-export actions could send or persist user information.

Mitigation: Perform those actions only after explicit user authorization and only when the host environment allows them.

## Reference(s):

- [Skill instructions](artifact/SKILL.md)
- [Career assessment framework](artifact/references/assessment.md)
- [MBTI career reference](artifact/references/mbti.md)
- [Career anchor reference](artifact/references/career_anchor.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Salary database](artifact/references/salary_database.json)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Education paths](artifact/references/education_paths.md)
- [2026 emerging careers in China](artifact/references/emerging_industries/2026_careers.md)
- [Insurance broker company data](artifact/references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational guidance and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown report file when explicitly requested and host environment allows script execution.]

## Skill Version(s):

2.2.283 (source: server release metadata; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
