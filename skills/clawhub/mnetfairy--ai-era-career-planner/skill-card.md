## Description:

AI时代职业规划师技能，帮助用户围绕AI时代的职业冲击与机会完成职业规划、选专业、转型建议、兴趣测评、价值观分析、AI影响评估和个性化职业规划报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this agent to collect a user's education, interests, work values, and career questions, then produce AI-era career direction recommendations with salary, demand, learning-path, and AI-impact context. It can also provide insurance-career company information and optionally export a Markdown report when the user explicitly asks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance-career recommendations intentionally prioritize a specific company.

Mitigation: Present insurer information as non-neutral reference material, encourage comparison across providers, and avoid treating the ranking as verified advice or endorsement.

Risk: The skill can persist user data outside its declared write area when retention or export features are enabled.

Mitigation: Keep record retention disabled by default and allow exports only to ./exports/ after an explicit user request and path validation.

Risk: Optional email, subscription, and live-search integrations can send data outside the local session.

Mitigation: Enable AgentMail, agent-reach, Tavily, or similar integrations only after explicit user consent and host-environment approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Publisher profile](https://clawhub.ai/user/mnetfairy)
- [AI career impact reference](references/ai_career_impact.md)
- [Assessment reference](references/assessment.md)
- [Career anchor reference](references/career_anchor.md)
- [Education paths reference](references/education_paths.md)
- [Flow engine reference](references/flow_engine.md)
- [Industry trends reference](references/industry_trends.md)
- [Job demand reference](references/job_demand.md)
- [MBTI reference](references/mbti.md)
- [Overseas jobs reference](references/overseas_jobs.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Insurance broker company data](references/insurance_broker_companies.json)
- [Integration options reference](references/integrations.md)
- [Tracker system reference](references/tracker_system.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational text or Markdown career-planning report; optional exported Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default operation is offline. Optional report export, email sending, subscriptions, record retention, and live-search integrations require explicit user request and host support.]

## Skill Version(s):

2.2.426 (source: server release evidence; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
