## Description:

AI Era Career Planner is a Chinese-language career-planning agent that gathers user background, assesses career interests and values, evaluates AI impact risk, and produces personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to explore career choices, major selection, job transitions, and AI-era employability. It provides structured career recommendations, AI impact ratings, salary and demand context, and next-step action plans based on the user's profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on career, salary, or labor-market recommendations as definitive advice.

Mitigation: Present outputs as advisory planning support and encourage users to verify salary ranges, job demand, and education paths against current sources before making major decisions.

Risk: Bundled insurance-company data and recommendations may be incomplete or not fully verified.

Mitigation: Tell users to independently confirm company credentials, contact details, and suitability before contacting or choosing an insurance company.

Risk: Career planning conversations can include sensitive personal background.

Mitigation: Ask only for information needed for the planning task and avoid optional export, email, tracking, or subscription features unless the user explicitly requests them.

Risk: Optional export, email, web lookup, subscription, or tracking features can create side effects beyond normal chat guidance.

Mitigation: Keep the default posture offline and require explicit user intent plus host support before enabling those features.

## Reference(s):

- [Skill listing](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](references/ai_career_impact.md)
- [Assessment reference](references/assessment.md)
- [Career anchor reference](references/career_anchor.md)
- [MBTI reference](references/mbti.md)
- [Salary reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand reference](references/job_demand.md)
- [Industry trends reference](references/industry_trends.md)
- [Education paths reference](references/education_paths.md)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Integration behavior reference](references/integrations.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Conversational text and structured Markdown career-planning reports; optional Markdown export file when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default offline operation; optional export, email, web lookup, subscription, and tracking features require explicit user request and host support.]

## Skill Version(s):

2.2.436 (source: server release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
