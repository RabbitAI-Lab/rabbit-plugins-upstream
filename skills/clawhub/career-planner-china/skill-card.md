## Description:

AI-era career planning skill for China-focused career guidance, including staged user intake, Holland interest assessment, career values analysis, AI impact assessment, and personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect career-planning context, assess interests and values, evaluate AI-era career risk, and generate actionable China-focused career recommendations. It can also support optional report export, tracking, email, subscriptions, or live job-data lookup only when explicitly requested.

### Deployment Geography for Use:

China-focused content; global deployment unless restricted by the consuming platform or reviewer.

## Known Risks and Mitigations:

Risk: The skill may ask for personal education, career, city, values, and goals to create tailored advice.

Mitigation: Collect only information needed for the requested guidance, avoid unnecessary sensitive details, and do not persist user information unless explicitly requested.

Risk: Optional report export, tracking, email, subscriptions, and live job-data lookup can introduce privacy or data-sharing concerns.

Mitigation: Run those features only after explicit user request and when the host environment allows them; disclose the action before sending, storing, or looking up user-related data.

Risk: Insurance-company suggestions may be incomplete or mistaken for an endorsement.

Mitigation: Present insurance-company entries as career-entry guidance only and tell users to compare independently before contacting any listed company.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Skill definition](artifact/SKILL.md)
- [Career planning dialogue flow](artifact/references/flow_engine.md)
- [Career assessment framework](artifact/references/assessment.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [2026 emerging careers in China](artifact/references/emerging_industries/2026_careers.md)
- [Optional integrations](artifact/references/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Code, Shell commands, Configuration]

**Output Format:** [Conversational text and structured Markdown reports, with optional generated Markdown files when export is explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bundled reference data for assessments, salary ranges, industry trends, learning paths, and insurance-company entry guidance.]

## Skill Version(s):

2.2.317 (source: server release metadata and target metadata; artifact frontmatter lists 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
