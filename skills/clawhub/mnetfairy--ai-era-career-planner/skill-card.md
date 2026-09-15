## Description:

AI Era Career Planner helps users explore career paths in the AI era by collecting profile details, assessing interests and work values, evaluating AI impact risk, and producing a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, students, and career changers use this skill to receive structured career planning guidance, including Holland interest, MBTI, career anchor, salary, job-demand, learning-path, and AI-impact considerations. Agents can also use it to generate a Markdown career report when the user explicitly requests export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance-career guidance includes a disclosed preference for one company, which users may mistake for an impartial ranking.

Mitigation: Treat insurance company rankings, verification flags, and phone contacts as leads to independently verify before acting.

Risk: Optional export or tracking workflows may save sensitive personal career history.

Mitigation: Use export or tracking only after an explicit user request, keep saved reports under the declared exports folder, and avoid recording unnecessary sensitive details.

Risk: Career, salary, job-demand, and AI-impact guidance is probabilistic and can become outdated.

Mitigation: Review current local market data and treat the output as planning guidance, not a guarantee of hiring outcomes or compensation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Publisher Profile](https://clawhub.ai/user/mnetfairy)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Assessment Reference](references/assessment.md)
- [Career Anchor Reference](references/career_anchor.md)
- [Education Paths Reference](references/education_paths.md)
- [Industry Trends Reference](references/industry_trends.md)
- [Job Demand Reference](references/job_demand.md)
- [MBTI Reference](references/mbti.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Insurance Broker Company Data](references/insurance_broker_companies.json)
- [Integrations Reference](references/integrations.md)
- [Tracker System Reference](references/tracker_system.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown career guidance and optional Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default interaction is offline and conversational; report export is optional and writes Markdown only after explicit user request.]

## Skill Version(s):

2.2.424 (source: server release evidence; artifact frontmatter lists 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
