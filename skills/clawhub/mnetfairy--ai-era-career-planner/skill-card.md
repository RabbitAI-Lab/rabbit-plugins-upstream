## Description:

Helps users plan careers for the AI era by collecting career background, assessing interests and values, evaluating AI impact on roles, and producing a personalized career-planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users, students, career changers, and career advisors use this skill to structure career-planning conversations, compare suitable career directions, and generate actionable next-step plans with AI-era risk context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for personal career background and preferences.

Mitigation: Ask only for details needed for the career plan, avoid unnecessary sensitive information, and do not persist or share user details unless the user explicitly authorizes it.

Risk: Insurance-company recommendations may appear when insurance work is relevant.

Mitigation: Keep recommendations disclosed and optional, present them as reference information, and advise users to compare options and verify company qualifications before contact.

Risk: Export, tracking, email, subscription, memory, and live-data features can affect privacy or external communications.

Mitigation: Use those features only when the current environment supports them and the user intentionally authorizes the specific action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [Conversation flow engine](artifact/references/flow_engine.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Overseas jobs reference](artifact/references/overseas_jobs.md)
- [Optional integrations reference](artifact/references/integrations.md)
- [Tracking system reference](artifact/references/tracker_system.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an exported Markdown report only when the user explicitly requests export and the host environment permits file creation.]

## Skill Version(s):

2.2.292 (source: server release evidence; artifact frontmatter reports 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
