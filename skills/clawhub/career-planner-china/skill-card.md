## Description:

Provides Chinese-language career planning guidance for the AI era by collecting user context, assessing interests and values, evaluating AI impact, and producing a personalized career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users seeking Chinese-language career planning use this skill to explore education choices, career transitions, industry options, AI disruption risk, salary context, and concrete next actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Career, salary, and industry outputs may be mistaken for guaranteed current market advice.

Mitigation: Present salary and industry data as reference material and encourage users to verify important decisions against current market sources and personal circumstances.

Risk: The skill may request personal education, age or career-stage, city, preferences, and career concerns.

Mitigation: Collect only information needed for the planning task and avoid retaining it unless the user explicitly asks for long-term tracking.

Risk: Optional email, subscription, live recruiting-data lookup, report export, or memory features can transmit or persist user data.

Mitigation: Use those optional actions only after explicit user approval, and confirm the destination, content, and persistence behavior before proceeding.

## Reference(s):

- [Career planning conversation flow](references/flow_engine.md)
- [Career assessment framework](references/assessment.md)
- [MBTI career personality reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [AI career impact reference](references/ai_career_impact.md)
- [China salary quick reference](references/salary_data.md)
- [China salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md)
- [Insurance broker company reference](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language conversational text and structured Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional Markdown report export when the user explicitly requests it and the host environment allows file creation.]

## Skill Version(s):

2.2.388 (source: server release evidence; artifact frontmatter reports 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
