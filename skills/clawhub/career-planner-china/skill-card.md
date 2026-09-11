## Description:

AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this agent to discuss China-focused education and career choices, career transitions, AI impact on occupations, salaries, demand trends, learning paths, and next-step action plans. When relevant, it can also provide insurance-industry entry guidance using bundled company data.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security review flags a maintainer-selected insurance company recommendation and conflicting data, contact, and persistence instructions.

Mitigation: Treat insurance company suggestions and verified flags as advisory, ask for objective criteria and current source checks, and require user confirmation before showing contact details.

Risk: Optional integrations can send email, store memory, subscribe to follow-up updates, or perform real-time job-data lookup.

Mitigation: Leave these behaviors disabled unless the user explicitly requests them and the host environment permits them.

Risk: Career, salary, and AI-impact guidance can be incomplete or stale for an individual user's location, industry, and time horizon.

Mitigation: Present recommendations as planning inputs rather than guarantees, and encourage source review before making employment, education, or financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchor reference](references/career_anchor.md)
- [MBTI career reference](references/mbti.md)
- [Education paths](references/education_paths.md)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [China salary database](references/salary_database.json)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [2026 emerging careers](references/emerging_industries/2026_careers.md)
- [Industry-specific career modules](references/industries/)
- [Optional integrations](references/integrations.md)
- [Career tracking system](references/tracker_system.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration]

**Output Format:** [Markdown career-planning reports with structured recommendations, action lists, and optional exported Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is conversational Markdown; report export, email sending, memory storage, follow-up tracking, and real-time job-data lookup are optional behaviors that require explicit user request and host support.]

## Skill Version(s):

2.2.411 (source: ClawHub release evidence; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
