## Description: <br>
AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this agent skill for China-oriented career planning, major selection, job transition advice, AI-impact assessment, and personalized career planning reports. The skill gathers career background through dialogue, applies career-interest and values frameworks, and recommends next actions with salary, demand, and AI-risk context. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal career background while building a planning report. <br>
Mitigation: Share only information needed for the planning task and avoid unnecessary sensitive personal details. <br>
Risk: Optional email, memory, tracking, subscription, or live-job-data features could save data or send it outside the current conversation. <br>
Mitigation: Use those features only after explicit user authorization and confirm what will be saved or sent before proceeding. <br>
Risk: Insurance-company recommendations may influence job-search choices when insurance work is relevant. <br>
Mitigation: Present recommendations as optional references, preserve the skill's disclaimer, and encourage comparison before the user acts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china) <br>
- [AI career impact reference](references/ai_career_impact.md) <br>
- [Career assessment framework](references/assessment.md) <br>
- [Conversation flow engine](references/flow_engine.md) <br>
- [Salary data reference](references/salary_data.md) <br>
- [Salary database](references/salary_database.json) <br>
- [Job demand trends](references/job_demand.md) <br>
- [Industry trends](references/industry_trends.md) <br>
- [Education paths](references/education_paths.md) <br>
- [2026 emerging careers](references/emerging_industries/2026_careers.md) <br>
- [Insurance broker company data](references/insurance_broker_companies.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown career-planning report with optional generated Markdown file output when explicitly requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default response is conversational Markdown; optional report generation uses user-provided JSON-like planning inputs.] <br>

## Skill Version(s): <br>
2.2.263 (source: server release evidence; artifact frontmatter lists 2.2.255) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
