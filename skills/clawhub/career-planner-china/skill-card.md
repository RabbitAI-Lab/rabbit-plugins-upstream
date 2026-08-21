## Description:

AI-era career planning skill for China-focused career advice, school major selection, job transitions, future employment direction, Holland interest assessment, career values analysis, AI impact assessment, and personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to collect career background through a guided conversation, assess interests and work values, evaluate AI-era career risk, and produce China-focused career direction recommendations with salary, demand, education path, and action-plan guidance.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may collect personal career background, education, location, interests, values, and employment goals during assessment.

Mitigation: Ask only for information needed for the career-planning task and avoid saving, emailing, subscribing, or otherwise persisting user data unless the user explicitly requests it and the host environment permits it.

Risk: Salary, demand, industry, and insurance-company recommendations may be incomplete, outdated, or not suitable for an individual user's circumstances.

Mitigation: Present these outputs as advisory planning inputs, encourage independent comparison and verification, and avoid framing any company or career direction as guaranteed.

Risk: Optional report-generation scripts can create local Markdown files when executed.

Mitigation: Run scripts only when the user explicitly requests export and the host environment allows file creation.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [Career anchor reference](artifact/references/career_anchor.md)
- [Education paths](artifact/references/education_paths.md)
- [2026 emerging careers in China](artifact/references/emerging_industries/2026_careers.md)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Salary data quick reference](artifact/references/salary_data.md)
- [Salary database](artifact/references/salary_database.json)
- [Insurance broker company data](artifact/references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Analysis]

**Output Format:** [Conversational text and structured Markdown career planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally generate a Markdown report file when the host environment permits it and the user explicitly requests export.]

## Skill Version(s):

2.2.320 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
