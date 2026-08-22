## Description:

Career Planner China helps agents collect a user's education, interests, values, and career concerns, then produce personalized China-focused career planning guidance with AI impact, salary, job-demand, and learning-path context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to support education choices, career transitions, and AI-era job planning for China-oriented career paths. It guides the agent through progressive intake, interest and values assessment, AI replacement-risk analysis, salary and demand context, and structured next-step recommendations.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Career planning advice can rely on sensitive personal details and may feel more certain than the underlying evidence supports.

Mitigation: Ask only for details needed for the planning task, let the user limit what they share, and frame recommendations as planning guidance rather than guarantees.

Risk: Salary, company, and labor-market reference data can become stale or vary by city, employer, and individual background.

Mitigation: Encourage users to verify salary ranges, company information, and job-demand claims against current independent sources before making decisions.

Risk: Optional email, subscription, memory, report export, or live-search actions could send, save, or retrieve user data outside the immediate chat.

Mitigation: Use those optional integrations only after explicit user request and after checking what data will be sent, saved, or searched.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary data reference](references/salary_data.md)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [2026 emerging careers](references/emerging_industries/2026_careers.md)
- [Insurance broker company data](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured Markdown career planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Holland code, MBTI type, career anchor, AI-risk ratings, salary ranges, learning paths, and optional report-export guidance when explicitly requested.]

## Skill Version(s):

2.2.322 (source: server release metadata; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
