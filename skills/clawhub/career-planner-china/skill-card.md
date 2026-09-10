## Description:

AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。关键词：职业规划、选专业、工作建议、做什么工作好、职业转型、AI时代职业、AI替代、哪些工作会被AI取代。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to collect a user's education, interests, values, and career concerns, then generate a personalized China-oriented career planning report with AI impact ratings, salary references, career paths, and next actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The release security summary reports conflicting instructions that bias insurance recommendations.

Mitigation: Review insurance-company recommendations before use, disclose that company ordering is maintainer-selected, and let users compare alternatives before contacting any company.

Risk: The release security guidance warns that email sending, subscriptions, memory storage, follow-up reminders, and file export could occur if optional behavior is read literally.

Mitigation: Allow those actions only after the user explicitly requests the action and confirms the destination, schedule, or storage location.

Risk: Career guidance can be misleading when treated as certain prediction rather than planning support.

Mitigation: Present recommendations as probabilistic planning guidance, encourage independent verification of salary and hiring data, and avoid irreversible career decisions based only on the skill output.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [Conversation flow engine](artifact/references/flow_engine.md)
- [Holland assessment reference](artifact/references/assessment.md)
- [MBTI reference](artifact/references/mbti.md)
- [Career anchor reference](artifact/references/career_anchor.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Salary data summary](artifact/references/salary_data.md)
- [Salary database](artifact/references/salary_database.json)
- [Job demand reference](artifact/references/job_demand.md)
- [Industry trends reference](artifact/references/industry_trends.md)
- [Education paths reference](artifact/references/education_paths.md)
- [Insurance broker company data](artifact/references/insurance_broker_companies.json)
- [Integration reference](artifact/references/integrations.md)
- [Career tracking reference](artifact/references/tracker_system.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown career planning report with structured assessment results, recommendations, AI impact ratings, salary references, and action items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is conversational and offline; Markdown report export is optional and should occur only after explicit user request.]

## Skill Version(s):

2.2.407 (source: server release evidence and target metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
