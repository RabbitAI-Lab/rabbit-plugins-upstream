## Description:

Comprehensive career planning for the AI era: analyzes skills, identifies opportunities, plans development paths, and guides career transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career-planning agents use this skill to assess user-provided skills, goals, constraints, and optional resume text, then produce structured career recommendations, development paths, and transition guidance. It is suited for AI-era career exploration, skills planning, salary research, and staged action planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resume, skills, goals, salary expectations, and career plans can be personal data.

Mitigation: Keep processing local unless the user explicitly chooses an external provider or integration, minimize supplied personal data, and protect generated reports or logs before sharing.

Risk: Optional LLM, email, subscription, or realtime data integrations can transmit user-provided career details outside the local environment.

Mitigation: Activate optional integrations only after explicit user authorization, confirm destinations and data scope, and review outputs before sending or saving.

Risk: Career plans, salary references, and job-demand guidance may be incomplete, outdated, or unsuitable for an individual decision.

Mitigation: Treat outputs as informational guidance, verify important claims against current sources, and review recommendations before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/ai-era-career-planner)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [Career planning flow engine](artifact/references/flow_engine.md)
- [Education paths reference](artifact/references/education_paths.md)
- [Salary data reference](artifact/references/salary_data.md)
- [Overseas jobs reference](artifact/references/overseas_jobs.md)
- [Optional integrations reference](artifact/references/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text guidance, with optional generated Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include career recommendations, assessment summaries, salary references, staged action plans, and reviewable tracker or report content.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
