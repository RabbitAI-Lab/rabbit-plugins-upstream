## Description:

AI-era career planning skill for China-focused career advice, education and major selection, career transitions, AI impact assessment, and personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to discuss career planning, career advice, major selection, and work transitions in the context of AI-driven labor-market change. The agent gathers career, education, interest, location, and goal information, then produces personalized recommendations, AI risk ratings, salary context, learning paths, and action plans.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Career advice may be incomplete, stale, or overconfident because labor-market demand, salary data, and AI impact forecasts change over time.

Mitigation: Treat recommendations, salary figures, and AI risk ratings as planning inputs, and verify important decisions against current job listings, employer requirements, and local market sources.

Risk: The skill may ask users to share personal career, education, interests, city, and work-goal information during planning.

Mitigation: Share only information needed for the planning task, avoid unnecessary sensitive personal details, and do not persist profiles unless the user explicitly opts in.

Risk: Optional exports, memory, email delivery, subscriptions, live data lookup, and insurance-company recommendations can create privacy, contact, or commercial-suitability concerns.

Mitigation: Keep optional external actions off unless explicitly requested, review generated reports before sending or saving them, and independently compare any insurance-company suggestions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career planning workflow](references/flow_engine.md)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary reference data](references/salary_data.md)
- [Detailed salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md)
- [Insurance broker company data](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text and structured Markdown career planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include career fit analysis, Holland/RIASEC and MBTI-style assessments, AI impact ratings, salary references, learning paths, insurance-industry company suggestions when relevant, and next-step action plans.]

## Skill Version(s):

2.2.392 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
