## Description:

AI Era Career Planner is a Chinese-language career planning assistant that collects user background, assesses career interests and values, evaluates AI-era job impact, and produces personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, students, and career changers use this skill to receive structured career direction, AI impact analysis, salary and demand context, and short- and long-term action plans. It can optionally export a Markdown report when the user explicitly requests export.

### Deployment Geography for Use:

Global; reference data and insurance-company guidance are primarily China-focused.

## Known Risks and Mitigations:

Risk: Salary and insurance-company data may be incomplete, outdated, or advisory rather than authoritative.

Mitigation: Treat those outputs as reference material and independently verify company credentials, contact details, salary ranges, and source claims before acting on recommendations.

Risk: Career planning guidance can materially influence education, employment, or insurance-industry decisions.

Mitigation: Use the skill as decision support, compare multiple sources, and avoid treating recommendations as a guarantee of employment outcomes or professional advice.

Risk: Optional export, email, subscription, network lookup, or tracking features can create privacy or persistence effects.

Mitigation: Enable those actions only after an explicit user request and confirm the destination, data to be shared, and storage behavior before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [SKILL.md](artifact/SKILL.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment reference](artifact/references/assessment.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [Insurance broker company data](artifact/references/insurance_broker_companies.json)
- [Optional integrations reference](artifact/references/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance, Files]

**Output Format:** [Markdown-style conversational report with structured career recommendations; optional Markdown file export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local reference material by default; optional export, email, subscription, network lookup, and tracking behaviors require explicit user request.]

## Skill Version(s):

2.2.438 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
