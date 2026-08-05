## Description:

Provides AI-era career planning for China-focused users by collecting career context, assessing interests and values, evaluating AI disruption risk, and producing personalized career direction recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to explore career choices, education paths, industry transitions, and AI-era job risks through a guided conversation. The skill returns a structured, actionable career-planning report with recommended directions, AI impact ratings, learning paths, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask about age, education, interests, goals, and career concerns.

Mitigation: Collect only information needed for the planning task and avoid storing or sharing personal details unless the user explicitly requests supported persistence or export.

Risk: Optional report export, memory, email, subscriptions, and real-time data lookup can move information outside the default chat response.

Mitigation: Keep those features disabled by default and use them only after explicit user authorization in a host environment that supports the requested action.

Risk: Insurance-company recommendations may be interpreted as endorsements.

Mitigation: Present insurance-company entries as informational career leads and advise users to compare options independently.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Skill definition](artifact/SKILL.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [MBTI career personality reference](artifact/references/mbti.md)
- [Career anchor reference](artifact/references/career_anchor.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Job demand trends](artifact/references/job_demand.md)
- [Industry trends](artifact/references/industry_trends.md)
- [2026 emerging careers](artifact/references/emerging_industries/2026_careers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown career-planning report, with optional generated Markdown report file when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-first; optional memory, email, subscriptions, real-time lookup, and report export require explicit user request and host support.]

## Skill Version(s):

2.2.277 (source: server release metadata; artifact frontmatter says 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
