## Description:

Career Planner China helps Chinese-speaking users evaluate interests, values, AI career impact, salary ranges, industry demand, and next steps for China-focused career planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in China use this skill for career planning, major selection, job transition advice, and AI-era occupation risk assessment. The agent produces personalized reports with recommended career directions, AI-readiness guidance, salary and demand context, and action plans.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Career recommendations may overstate salary, demand, or AI-impact certainty.

Mitigation: Treat reports as planning guidance, review the underlying references, and verify current education, labor-market, and compensation data before making consequential decisions.

Risk: Insurance-company suggestions may steer users toward specific providers.

Mitigation: Trigger insurance recommendations only when relevant to the user's stated interest, disclose the stated basis, compare multiple providers, and avoid showing contact details unless the user explicitly asks.

Risk: Optional email, memory, follow-up, scheduling, or outbound-network integrations can expose personal career information or create unwanted outreach.

Mitigation: Keep the skill offline by default and grant email, memory, scheduling, or network tools only after explicit user consent for that specific action.

## Reference(s):

- [Skill source](SKILL.md)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchor reference](references/career_anchor.md)
- [MBTI career personality reference](references/mbti.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [China emerging careers 2026](references/emerging_industries/2026_careers.md)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown career planning report with optional generated Markdown export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default response is conversational guidance; Markdown report export is optional and should run only when explicitly requested.]

## Skill Version(s):

2.99.99 (source: server release metadata; artifact frontmatter lists 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
