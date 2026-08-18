## Description:

Career Planner China helps Chinese-speaking users plan careers for the AI era by collecting background information, assessing interests and values, estimating AI impact, and producing personalized career-planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to conduct guided career-planning conversations for students, career changers, and workers in China-focused contexts. It supports interest and value assessment, AI-disruption risk review, salary and job-trend context, career recommendations, and next-step action planning.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask for personal career background while building a planning profile.

Mitigation: Collect only information needed for the requested career-planning task and avoid retaining profile details unless the user explicitly asks for tracking or memory.

Risk: Optional report export, memory writing, email delivery, subscriptions, and live job-data APIs can affect privacy or create external side effects.

Mitigation: Use these capabilities only when the host environment supports them and the user has explicitly authorized the specific action.

Risk: Salary figures, job-demand trends, and insurance company recommendations may be incomplete or become outdated.

Mitigation: Present them as reference material and advise users to independently verify salary, hiring, and insurance information before acting on it.

Risk: Career planning is probabilistic and can influence consequential education or employment decisions.

Mitigation: Frame recommendations as options, include uncertainty and potential risks, and avoid aggressive employment advice unless the user specifically requests that analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchor reference](references/career_anchor.md)
- [MBTI career personality reference](references/mbti.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional report export, memory, email, subscriptions, and live job-data integrations are gated on explicit user authorization and host support.]

## Skill Version(s):

2.2.311 (source: server release evidence; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
