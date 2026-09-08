## Description:

AI Era Career Planner helps users assess career interests, values, AI disruption risk, salary signals, industry trends, and next steps, then produces a personalized career-planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Students, workers, and career switchers use this skill for Chinese-language career planning in the AI era. It guides a conversation, combines interest and values assessments with local reference data, and returns career directions, AI impact ratings, salary context, skill priorities, and an action plan.

### Deployment Geography for Use:

Global; strongest coverage is for Chinese-language users and China-market career data.

## Known Risks and Mitigations:

Risk: The insurance-company ordering includes a maintainer-selected preferred placement that could be mistaken for an independent endorsement.

Mitigation: Present the placement as publisher-maintained information, disclose that users should compare options independently, and verify company licensing, regional coverage, compensation terms, and contact details before acting.

Risk: Optional report export can create local Markdown files containing personal career information.

Mitigation: Export only after an explicit user request, use a trusted local export directory, and avoid sharing exported reports without user consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](references/ai_career_impact.md)
- [Assessment methods](references/assessment.md)
- [Career anchor reference](references/career_anchor.md)
- [Conversation flow engine](references/flow_engine.md)
- [Industry trends](references/industry_trends.md)
- [Job demand trends](references/job_demand.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Insurance company data](references/insurance_broker_companies.json)
- [Optional integrations](references/integrations.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Conversational text and structured Markdown career reports; optional local Markdown file export when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default offline operation using bundled reference files; optional network, email, subscription, memory, and export behavior requires explicit user request and host support.]

## Skill Version(s):

2.2.398 (source: server release metadata; artifact frontmatter: 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
