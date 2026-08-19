## Description:

Career-planner-china helps agents conduct China-focused AI-era career planning conversations, including user intake, career-interest and values assessment, AI impact rating, salary and demand references, and personalized career plan reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to structure career-planning conversations for students, job seekers, and career changers in China. It produces personalized career direction recommendations with AI-era risk ratings, learning paths, salary context, and next-step action plans.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask personal career, education, preference, and location questions.

Mitigation: Collect only information needed for the planning conversation and avoid sharing or storing personal details unless the user explicitly requests an optional integration.

Risk: Optional report generation, memory, email, subscription, and live job data features can write or send user information outside the chat.

Mitigation: Keep optional actions disabled unless the user explicitly requests them and the destination or data handling is clear.

Risk: Career, salary, and AI-impact guidance can be incomplete or time-sensitive.

Mitigation: Present recommendations as planning guidance, encourage users to compare current market sources, and avoid framing career outcomes as guaranteed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Skill instructions](artifact/SKILL.md)
- [Career assessment framework](artifact/references/assessment.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [China emerging careers 2026](artifact/references/emerging_industries/2026_careers.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Education paths](artifact/references/education_paths.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown career-planning report and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured career recommendations, AI impact ratings, salary ranges, learning paths, and action lists.]

## Skill Version(s):

2.2.315 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
