## Description:

Chinese-first career-planning skill that helps users assess AI-era career risks and opportunities, collect personal career inputs, run Holland, MBTI, and career-anchor analyses, and produce a personalized career-planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for AI-era career planning, major selection, job-change planning, and industry-specific career recommendations. The skill generates conversational guidance and structured reports using local assessment, salary, industry trend, education path, and job-demand references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags a maintainer-directed insurance-company preference that needs review before installation.

Mitigation: Verify insurance-company recommendations independently before relying on them, and present them as informational options rather than a sales endorsement.

Risk: The skill may save personalized career reports locally when a user asks for export.

Mitigation: Keep exports inside a controlled directory, avoid storing unnecessary personal data, and delete exported reports when they are no longer needed.

Risk: Optional tracking or integration behavior may involve user career details, reports, messages, or subscriptions.

Mitigation: Use tracking, email, subscription, or realtime data integrations only after explicit user authorization and current-environment permission checks.

## Reference(s):

- [Skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](references/ai_career_impact.md)
- [Assessment reference](references/assessment.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Industry trends reference](references/industry_trends.md)
- [Job demand reference](references/job_demand.md)
- [Education paths reference](references/education_paths.md)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Optional integrations reference](references/integrations.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration]

**Output Format:** [Conversational text and structured Markdown reports; optional local Markdown export on explicit user request.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default operation is offline guidance. Local report export and external integrations are optional and require explicit user request.]

## Skill Version(s):

2.2.416 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
