## Description:

AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。关键词：职业规划、选专业、工作建议、做什么工作好、职业转型、AI时代职业、AI替代、哪些工作会被AI取代。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for China-focused AI-era career planning, including staged information gathering, career-interest and values assessment, AI impact analysis, salary and demand context, and personalized career-planning reports.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks users for personal career-planning details, including age, education, interests, values, and goals.

Mitigation: Collect only details needed for the current planning conversation and avoid exporting, storing, or sharing them unless the user explicitly requests it.

Risk: Optional report export, email, subscription, live-data, and memory integrations could create unwanted external actions or persistence.

Mitigation: Keep these integrations disabled by default and require clear user authorization plus host-environment support before use.

Risk: Insurance-company recommendations may be mistaken for exclusive endorsement or verified placement advice.

Mitigation: Present insurance guidance as informational, ask for the user location when relevant, and tell users to independently verify company details and compare options.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career-planning workflow](artifact/SKILL.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [Career anchors reference](artifact/references/career_anchor.md)
- [MBTI career personality reference](artifact/references/mbti.md)
- [Education paths](artifact/references/education_paths.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [2026 emerging careers](artifact/references/emerging_industries/2026_careers.md)
- [Insurance broker company data](artifact/references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown career-planning reports and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional Markdown report files only when the user explicitly requests export and the host environment allows it.]

## Skill Version(s):

2.2.309 (source: server release metadata; artifact frontmatter lists 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
