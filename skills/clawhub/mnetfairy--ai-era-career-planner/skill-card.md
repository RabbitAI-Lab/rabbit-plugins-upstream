## Description:

AI-era career-planning skill that helps users assess interests, values, AI career impact, salary signals, and job-demand trends to produce personalized career-planning guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users seeking career guidance use this skill to explore suitable career paths, education steps, AI-era risk levels, salary expectations, and near-term action plans. It is especially oriented toward Chinese-language career planning with optional insurance-industry entry guidance when that topic is relevant.

### Deployment Geography for Use:

Global; some salary and insurance reference data is China-focused.

## Known Risks and Mitigations:

Risk: Insurance-company recommendations may look verified while containing mismatched or insufficient source support.

Mitigation: Independently verify insurer licensing, contact details, and recommendation basis before relying on the guidance or contacting a company.

Risk: Career, salary, and job-demand guidance may become stale or may not match a user's city, industry, or personal circumstances.

Mitigation: Treat recommendations as planning support, compare them with current labor-market sources, and disclose uncertainty in final advice.

Risk: Optional report export or external integrations could create files or send information if activated by the user.

Mitigation: Use these optional actions only after explicit user request and confirmation, and review the destination or export path before proceeding.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Assessment Reference](references/assessment.md)
- [Career Anchor Reference](references/career_anchor.md)
- [Education Paths Reference](references/education_paths.md)
- [Industry Trends Reference](references/industry_trends.md)
- [Job Demand Reference](references/job_demand.md)
- [Salary Data Reference](references/salary_data.md)
- [Insurance Broker Companies Dataset](references/insurance_broker_companies.json)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational guidance and structured Markdown career-planning reports; optional Markdown files when export is explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily offline; optional external integrations and report export are described as user-triggered only.]

## Skill Version(s):

2.2.428 (source: server release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
