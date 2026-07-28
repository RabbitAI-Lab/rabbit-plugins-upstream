## Description: <br>
AI时代职业规划师技能，面向职业规划、专业选择、职场转型和未来就业方向咨询，收集用户背景，结合霍兰德兴趣、职业价值观、MBTI、职业锚、AI影响分级、薪资和岗位趋势，输出个性化职业规划报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to discuss career planning, major selection, career transitions, AI-era job risk, salary expectations, and next-step learning paths for the China career market. The agent produces conversational guidance and a structured personalized career planning report. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may collect career-related personal details during conversation. <br>
Mitigation: Ask only for information needed for the planning task, avoid unnecessary sensitive details, and do not persist or export user data unless the user explicitly requests it and the host environment permits it. <br>
Risk: Optional report export, memory, email, subscription, and live-data features can create persistence or external sharing risks. <br>
Mitigation: Keep the default path offline and in-chat; require explicit user authorization before writing files, retaining notes, sending email, subscribing to updates, or using live-data tools. <br>
Risk: Insurance-company recommendations may influence career or commercial decisions. <br>
Mitigation: Present company lists as reference material, keep recommendations neutral, include the skill's disclaimer, and advise users to compare options independently before acting. <br>
Risk: Salary, demand, and emerging-career data can become outdated or vary by city, employer, and seniority. <br>
Mitigation: Frame market data as directional planning support and recommend checking current job postings or authoritative local sources before making high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china) <br>
- [Career Planning Conversation Flow](references/flow_engine.md) <br>
- [Career Assessment Framework](references/assessment.md) <br>
- [MBTI Career Personality Reference](references/mbti.md) <br>
- [Career Anchor Reference](references/career_anchor.md) <br>
- [AI Career Impact Reference](references/ai_career_impact.md) <br>
- [Salary Data Reference](references/salary_data.md) <br>
- [Salary Database](references/salary_database.json) <br>
- [Job Demand Trends](references/job_demand.md) <br>
- [Industry Trends](references/industry_trends.md) <br>
- [Education Paths](references/education_paths.md) <br>
- [2026 Emerging Careers China](references/emerging_industries/2026_careers.md) <br>
- [Industry Modules](references/industries/) <br>
- [Insurance Broker Companies](references/insurance_broker_companies.json) <br>
- [Optional Integrations](references/integrations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Conversational text and structured Markdown career planning report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline-first by default; optional Markdown report export, tracking notes, email, subscriptions, and live data use only when explicitly requested and supported by the host environment.] <br>

## Skill Version(s): <br>
2.2.251 (source: ClawHub release metadata; artifact frontmatter lists 2.2.194) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
