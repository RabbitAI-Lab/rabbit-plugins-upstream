## Description:

Provides Chinese-language AI-era career planning guidance, including profile collection, Holland/MBTI/career-anchor assessment, AI impact ratings, salary and demand references, and personalized career plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this agent for China-focused career planning, school or major selection, career transition advice, and AI-era job risk assessment. The skill produces structured recommendations, learning paths, salary and demand context, and next-step action plans.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Insurance-company recommendations may not be neutral.

Mitigation: Review the insurance recommendation path before installing or using the skill, and treat listed companies as options to compare rather than unbiased endorsements.

Risk: Optional report export, email sending, memory writes, tracking, or network-backed job lookup may write or transmit user career-profile data.

Mitigation: Allow these behaviors only after confirming the destination, retained data, execution environment, and explicit user consent.

Risk: Career, salary, and job-demand guidance can become stale or overconfident.

Mitigation: Use the report as planning support, verify high-impact career or education decisions against current market sources, and preserve uncertainty in recommendations.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Assessment methods](artifact/references/assessment.md)
- [Career anchors](artifact/references/career_anchor.md)
- [Education paths](artifact/references/education_paths.md)
- [Flow engine](artifact/references/flow_engine.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Job demand](artifact/references/job_demand.md)
- [MBTI reference](artifact/references/mbti.md)
- [Salary data summary](artifact/references/salary_data.md)
- [Salary database](artifact/references/salary_database.json)
- [Insurance broker companies](artifact/references/insurance_broker_companies.json)
- [Integration notes](artifact/references/integrations.md)
- [Tracker system](artifact/references/tracker_system.md)
- [2026 emerging careers](artifact/references/emerging_industries/2026_careers.md)
- [Tech career industry reference](artifact/references/industries/tech_career.md)
- [Healthcare industry reference](artifact/references/industries/healthcare.md)
- [Finance industry reference](artifact/references/industries/finance.md)
- [Education industry reference](artifact/references/industries/education.md)
- [Creative industry reference](artifact/references/industries/creative.md)
- [Manufacturing industry reference](artifact/references/industries/manufacturing.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [ClawHub publisher profile](https://clawhub.ai/user/mnetfairy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational guidance and structured Markdown career-planning reports; optional Markdown file export when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to offline reference-based guidance; optional email, memory, tracking, or network-backed job lookup should be used only after explicit user consent.]

## Skill Version(s):

2.99.99 (source: ClawHub release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
