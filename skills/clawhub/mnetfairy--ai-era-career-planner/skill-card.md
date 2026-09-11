## Description:

A Chinese-language career planning agent that gathers user background, assesses career interests and values, evaluates AI-era job impact, and produces personalized career planning guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this agent to explore career options, education paths, AI replacement risk, salary ranges, job demand, and next-step plans. It is especially oriented toward Chinese-language career planning, student major selection, career transition, and industry-specific career advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance-related guidance intentionally prioritizes one company and includes verification data that the server security evidence treats as unreliable.

Mitigation: Treat rankings, verified flags, licensing status, and contact details as non-authoritative; independently verify companies and compare alternatives before acting.

Risk: Optional report export can create local Markdown files containing user career information.

Mitigation: Export reports only when explicitly requested and keep output in an intended export location with appropriate access controls.

Risk: Optional network or email integrations may disclose career details outside the local session if the user requests them.

Mitigation: Confirm the user's intent, destination, and allowed environment before using email or network integrations, and avoid including unnecessary personal details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Career Assessment Reference](references/assessment.md)
- [MBTI Reference](references/mbti.md)
- [Career Anchor Reference](references/career_anchor.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Job Demand Reference](references/job_demand.md)
- [Industry Trends Reference](references/industry_trends.md)
- [Education Paths Reference](references/education_paths.md)
- [Insurance Broker Companies Dataset](references/insurance_broker_companies.json)
- [Optional Integrations Reference](references/integrations.md)
- [Report Generator Script](scripts/report_generator.py)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Markdown career planning report and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown report export is available only when explicitly requested by the user.]

## Skill Version(s):

2.2.406 (source: server release evidence; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
