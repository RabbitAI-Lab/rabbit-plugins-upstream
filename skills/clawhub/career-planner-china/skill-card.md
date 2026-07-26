## Description: <br>
AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。关键词：职业规划、选专业、工作建议、做什么工作好、职业转型、AI时代职业、AI替代、哪些工作会被AI取代。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, job seekers, and career changers use this agent to explore China-focused career options, assess interests and work values, evaluate AI impact on occupations, and receive personalized action plans. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask users for personal career history, preferences, and location context. <br>
Mitigation: Collect only information the user chooses to provide, avoid unnecessary sensitive details, and do not persist profiles unless the user explicitly requests it. <br>
Risk: Optional report export, memory tracking, email or subscription workflows, and real-time data integrations can expose user information or trigger external actions. <br>
Mitigation: Use those capabilities only after explicit user authorization and only when the current host environment permits them. <br>
Risk: Built-in insurance-company recommendations and phone numbers may be outdated or unsuitable for a user's circumstances. <br>
Mitigation: Present insurance-company information as reference material and advise users to independently verify companies, phone numbers, and suitability before acting. <br>
Risk: Career, salary, job-demand, and AI-impact guidance may be incomplete or become outdated. <br>
Mitigation: Frame recommendations as planning guidance rather than guarantees, disclose uncertainty, and use current external data only when requested and authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china) <br>
- [Career planning workflow](references/flow_engine.md) <br>
- [Career assessment framework](references/assessment.md) <br>
- [MBTI reference](references/mbti.md) <br>
- [Career anchor reference](references/career_anchor.md) <br>
- [AI career impact reference](references/ai_career_impact.md) <br>
- [Salary data reference](references/salary_data.md) <br>
- [Salary database](references/salary_database.json) <br>
- [Job demand reference](references/job_demand.md) <br>
- [Industry trends reference](references/industry_trends.md) <br>
- [Education paths reference](references/education_paths.md) <br>
- [Insurance broker company list](references/insurance_broker_companies.json) <br>
- [Optional integrations reference](references/integrations.md) <br>
- [Zhaopin salary and job data source](https://www.zhaopin.com/) <br>
- [Liepin salary and job data source](https://www.liepin.com/) <br>
- [Boss Zhipin salary and job data source](https://www.zhipin.com/) <br>
- [Indeed Beijing backend developer salary source](https://cn.indeed.com/career/%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88/salaries/%E5%8C%97%E4%BA%AC%E5%B8%82) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Chinese conversational guidance and structured Markdown career-planning reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Holland code, MBTI type, career anchor, salary ranges, AI impact ratings, recommended career paths, and action lists.] <br>

## Skill Version(s): <br>
2.2.245 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
