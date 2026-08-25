## Description:

AI Era Career Planner is a Chinese-language career planning agent that collects user background, assesses Holland interests, MBTI-style preferences, career anchors, AI-era job risk, salary ranges, and demand trends, then produces a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users seeking education, career planning, career transition, or AI-era job-risk guidance use this skill to receive structured questions and a personalized career direction report. It is also useful for advisors who want a reusable conversation flow and reference-backed career planning framework.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for personal career, education, preference, and location details during planning.

Mitigation: Share only information needed for the planning task, and do not allow persistence, exported reports, or saved records unless the user explicitly requests them.

Risk: Insurance-industry guidance can include company contact recommendations.

Mitigation: Treat company information as informational, compare options independently, and verify company credentials before contacting or applying.

Risk: Optional email, subscription, live-search, and saved-record integrations can send data outside the chat or retain user information.

Mitigation: Use these integrations only when the user explicitly asks for them and the host environment permits the requested action.

Risk: Career plans, salary ranges, and demand trends are planning guidance rather than guarantees.

Mitigation: Review recommendations against current local labor-market data and personal constraints before making education, job, or financial decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Assessment Framework](references/assessment.md)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Salary Data Reference](references/salary_data.md)
- [Job Demand Trends](references/job_demand.md)
- [Industry Trends](references/industry_trends.md)
- [Education Paths](references/education_paths.md)
- [Insurance Broker Company Data](references/insurance_broker_companies.json)
- [Optional Integrations](references/integrations.md)
- [Tracker System](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or structured Markdown career planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown report export only when the user explicitly asks and the host environment permits it.]

## Skill Version(s):

2.2.357 (source: server release evidence; artifact frontmatter lists 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
