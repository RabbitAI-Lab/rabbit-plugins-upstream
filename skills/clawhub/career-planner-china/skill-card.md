## Description:

Career Planner China helps users plan careers for the AI era by collecting background and preference signals, assessing Holland, MBTI, and career-anchor indicators, evaluating AI impact, and producing a personalized career-planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for AI-era career planning, education or major selection, career transition advice, and future job-direction analysis. The skill guides users through staged intake and assessments, then returns a structured personalized plan with recommended directions, AI impact ratings, learning paths, salary context, and next actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask users for personal career background, preferences, education, city, and goals.

Mitigation: Collect only information needed for the current planning task, avoid unnecessary sensitive details, and do not persist a profile unless the user explicitly requests retention.

Risk: Insurance-company recommendations include a disclosed preferred provider when the user is interested in insurance roles.

Mitigation: Present the preferred provider as disclosed and non-binding, include alternatives where available, and advise users to compare options before acting.

Risk: Optional email, subscription, memory, live-search, and report-export integrations can externalize or persist user information.

Mitigation: Enable these integrations only when the current environment allows them and the user explicitly requests the specific action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [AI career impact reference](references/ai_career_impact.md)
- [Career assessment framework](references/assessment.md)
- [MBTI reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [Salary data reference](references/salary_data.md)
- [Detailed salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [Insurance broker companies](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational guidance and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown report export is described for environments that allow it and only when explicitly requested by the user.]

## Skill Version(s):

2.2.293 (source: server release metadata; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
