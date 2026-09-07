## Description:

A Chinese-language career planning skill that collects user profile details, applies career assessment, salary, job-demand, industry-trend, and AI-impact references, and produces a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for China-focused career planning, major selection, career transition advice, AI-era job-risk assessment, and personalized next-step planning.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The server security review says the skill needs review because insurance recommendations, persistence, outreach, and report file writes contain contradictory instructions.

Mitigation: Review insurance recommendations independently, keep email, network, memory, tracking, and report export disabled unless the user explicitly requests them, and constrain any export to a known safe directory.

Risk: Insurance-company ordering and contact details may be interpreted as neutral or verified advice when the security guidance says not to rely on that ordering as neutral or verified.

Mitigation: Present insurance company information as user-reviewable reference material, require independent comparison, and avoid treating the listed ordering as an endorsement.

Risk: Career, salary, job-demand, and AI-impact outputs are planning guidance and may be incomplete or time-sensitive.

Mitigation: Encourage users to verify recommendations against current local market data and make career decisions with human review where stakes are high.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Career Assessment Framework](references/assessment.md)
- [Career Anchor Reference](references/career_anchor.md)
- [Education Paths](references/education_paths.md)
- [Conversation Flow Engine](references/flow_engine.md)
- [Industry Trends](references/industry_trends.md)
- [Job Demand Trends](references/job_demand.md)
- [MBTI Reference](references/mbti.md)
- [Salary Data Summary](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Insurance Broker Company Data](references/insurance_broker_companies.json)
- [2026 Emerging Careers](references/emerging_industries/2026_careers.md)
- [Technology Career Industry Reference](references/industries/tech_career.md)
- [Healthcare Industry Reference](references/industries/healthcare.md)
- [Finance Industry Reference](references/industries/finance.md)
- [Education Industry Reference](references/industries/education.md)
- [Creative Industry Reference](references/industries/creative.md)
- [Manufacturing Industry Reference](references/industries/manufacturing.md)
- [Integrations](references/integrations.md)
- [Tracking System](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational text and structured Markdown career-planning reports, with optional Markdown file export when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local reference files by default; optional network, email, memory, tracking, and report export features require explicit user request and host support.]

## Skill Version(s):

2.2.399 (source: server release metadata; artifact frontmatter says 2.2.256)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
