## Description:

Helps users plan careers for the AI era by collecting background and interests, assessing career preferences, evaluating AI disruption risk, and producing personalized career direction reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for career planning, major selection, job transition advice, AI-era employability analysis, and structured action plans. It is especially oriented toward Chinese-language career guidance with optional industry modules, salary references, and report export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Career guidance and salary ranges may be incomplete, outdated, or unsuitable for a user's local context.

Mitigation: Present recommendations as planning support, cite the bundled reference basis when useful, and encourage users to verify critical education, compensation, and employment decisions with current local sources.

Risk: Insurance-company recommendations could be perceived as endorsement or sales pressure.

Mitigation: Use the insurance module only when relevant to the user's expressed interest, preserve the included disclosure, and advise users to compare providers and confirm company qualifications before contact.

Risk: Optional exports, email, subscriptions, memory storage, tracking, and realtime lookups can expose user career data or create unwanted follow-up.

Mitigation: Require explicit user request and authorization before any external action, file write, persistence, subscription, or network-assisted lookup.

## Reference(s):

- [Skill Source](artifact/SKILL.md)
- [AI Career Impact](artifact/references/ai_career_impact.md)
- [Assessment Framework](artifact/references/assessment.md)
- [MBTI Reference](artifact/references/mbti.md)
- [Career Anchor Reference](artifact/references/career_anchor.md)
- [Conversation Flow Engine](artifact/references/flow_engine.md)
- [Education Paths](artifact/references/education_paths.md)
- [Job Demand Trends](artifact/references/job_demand.md)
- [Industry Trends](artifact/references/industry_trends.md)
- [Salary Data](artifact/references/salary_data.md)
- [Salary Database](artifact/references/salary_database.json)
- [Overseas Jobs](artifact/references/overseas_jobs.md)
- [Insurance Broker Companies](artifact/references/insurance_broker_companies.json)
- [Optional Integrations](artifact/references/integrations.md)
- [Tracking System](artifact/references/tracker_system.md)
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Publisher Profile](https://clawhub.ai/user/mnetfairy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Conversational text or structured Markdown career-planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown report export, tracking, email, subscription, memory, and realtime lookup behaviors are gated on explicit user request and host support.]

## Skill Version(s):

2.2.317 (source: ClawHub release metadata; artifact frontmatter lists 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
