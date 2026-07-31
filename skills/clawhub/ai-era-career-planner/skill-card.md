## Description: <br>
AI Era Career Planner helps users plan education choices, career transitions, and future job paths by collecting career context, applying career-interest and values assessments, evaluating AI-related role risk, and producing a personalized career plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill for Chinese-language career planning, education-path selection, and AI-era career transition guidance. The skill produces assessment-informed recommendations, AI impact ratings, salary and demand context, learning paths, and next-step action plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may collect personal career details such as age or stage, education background, interests, city, goals, and current career concerns. <br>
Mitigation: Share only the career details needed for the plan, avoid unnecessary sensitive information, and do not enable memory or tracking unless the user explicitly wants a saved record. <br>
Risk: Optional integrations can send email, create subscriptions, save memory, use realtime web data, or export report files. <br>
Mitigation: Keep these actions disabled by default and require explicit user intent and confirmation before any external send, subscription, persistence, web-data access, or file export. <br>
Risk: Insurance-career scenarios may display insurance company contact information that could influence user decisions. <br>
Mitigation: Present company information as reference material only, preserve the artifact's disclosure language, and advise users to compare options and verify company credentials before contact. <br>
Risk: Career recommendations, salary ranges, demand trends, and AI impact ratings are planning aids rather than guarantees. <br>
Mitigation: Frame recommendations as probabilistic guidance, note uncertainty, and encourage users to validate choices against current local market data and personal constraints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner) <br>
- [AI career impact reference](artifact/references/ai_career_impact.md) <br>
- [Career assessment framework](artifact/references/assessment.md) <br>
- [Career anchor reference](artifact/references/career_anchor.md) <br>
- [Conversation flow engine](artifact/references/flow_engine.md) <br>
- [Education paths](artifact/references/education_paths.md) <br>
- [Job demand trends](artifact/references/job_demand.md) <br>
- [Industry trends](artifact/references/industry_trends.md) <br>
- [Salary data summary](artifact/references/salary_data.md) <br>
- [Salary database](artifact/references/salary_database.json) <br>
- [Optional integrations](artifact/references/integrations.md) <br>
- [Tracking system](artifact/references/tracker_system.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown career-planning report with structured sections and optional generated Markdown files when explicitly requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assessment labels, AI impact ratings, salary ranges, learning paths, company contact information for insurance-career scenarios, and immediate action items.] <br>

## Skill Version(s): <br>
2.2.254 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
