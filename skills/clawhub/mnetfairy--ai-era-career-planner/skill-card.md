## Description:

AI Era Career Planner helps users plan careers for an AI-shaped job market by collecting profile details, assessing career interests and values, estimating AI impact, and producing personalized career-planning guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to explore career directions, education paths, role fit, salary ranges, AI exposure, and next-step action plans. It is especially oriented toward Chinese-language career-planning conversations and bundled China labor-market reference data.

### Deployment Geography for Use:

Global, with China-specific bundled salary, industry, and insurance-company reference data.

## Known Risks and Mitigations:

Risk: The insurance-career path includes a stated business-priority company recommendation and non-neutral ranking/contact data.

Mitigation: Present the recommendation as publisher-maintained reference material, ask users to compare alternatives, and verify company status, contact details, licensing, and regional availability before acting.

Risk: Bundled salary, industry, and job-demand data may be stale, incomplete, or region-specific.

Mitigation: Use the data as planning context only and verify important career, compensation, education, or relocation decisions against current local sources.

Risk: Optional email, network, memory, subscription, and report-export paths can disclose or persist user career information if enabled.

Mitigation: Keep the default offline posture, enable optional integrations only after explicit user request, and confirm the destination, scope, and content before sending or saving anything.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](references/ai_career_impact.md)
- [Career assessment reference](references/assessment.md)
- [MBTI reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [Education paths reference](references/education_paths.md)
- [Job demand reference](references/job_demand.md)
- [Industry trends reference](references/industry_trends.md)
- [Salary data reference](references/salary_data.md)
- [Detailed salary database](references/salary_database.json)
- [Insurance company reference data](references/insurance_broker_companies.json)
- [Optional integrations reference](references/integrations.md)
- [Insurance intermediary public query portal](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [guidance, markdown, text]

**Output Format:** [Markdown career-planning report and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional Markdown report export when explicitly requested by the user and permitted by the host environment.]

## Skill Version(s):

2.2.412 (source: ClawHub release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
