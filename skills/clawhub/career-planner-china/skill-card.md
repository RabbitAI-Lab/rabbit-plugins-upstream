## Description:

A Chinese-language career planning skill that collects career-stage and preference details, assesses Holland, MBTI, career-anchor, salary, job-demand, and AI-impact signals, and produces personalized career guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Students, workers, and career changers use this skill to explore China-oriented career options, AI replacement risk, salary ranges, learning paths, and practical next steps. It is intended for personalized career-planning conversations and structured report generation.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks for personal career-stage, education, preference, and location details to generate advice.

Mitigation: Collect only details needed for the requested planning task and avoid persistent memory or profile creation unless the user explicitly asks for it.

Risk: Salary ranges, job-demand trends, insurance-company suggestions, and AI-impact ratings are reference material and may be approximate or stale.

Mitigation: Present these data points as planning inputs, encourage users to verify important decisions against current local sources, and avoid framing recommendations as guarantees.

Risk: Optional integrations can send email, subscribe to updates, perform live job searches, or store follow-up records.

Mitigation: Use those integrations only when the host environment supports them and the user has clearly requested the specific action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career Assessment Framework](references/assessment.md)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Job Demand Trends](references/job_demand.md)
- [Industry Trends](references/industry_trends.md)
- [Education Paths](references/education_paths.md)
- [MBTI Reference](references/mbti.md)
- [Career Anchor Reference](references/career_anchor.md)
- [2026 Emerging Careers China Reference](references/emerging_industries/2026_careers.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational Chinese guidance and structured Markdown career-planning reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-first by default; optional Markdown export, email sending, subscriptions, live job search, and memory tracking require explicit user request and host support.]

## Skill Version(s):

2.2.382 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
