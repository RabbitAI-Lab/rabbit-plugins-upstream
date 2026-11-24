## Description:

Provides AI-era career planning through interest and values assessment, analysis of AI's impact on career paths, and personalized recommendations, with optional insurance-channel information on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People considering career choices, education paths, or a career transition use this skill to explore their interests and values, assess AI's effects on career options, and plan practical next steps. It lists insurance career channels only when requested; their ordering reflects the maintainer's disclosed business preference and is separate from personalized career recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Career, salary, and AI-impact assessments use static reference material and are planning guidance rather than predictions.

Mitigation: Treat recommendations as decision support and verify current local salary, demand, and qualification information before making major career decisions.

Risk: Insurance-channel ordering reflects the maintainer's disclosed commercial preference, not a personalized suitability assessment.

Mitigation: Show this list only when the user asks about insurance channels, disclose the preference, and offer side-by-side comparison with other channels.

Risk: The release security review is benign with medium confidence but partial because some referenced local paths were missing; report export and tracking options may also warrant user consideration.

Mitigation: Review the available files and declared permissions, and keep report export or tracking opt-in as described by the skill.

## Reference(s):

- [Career assessment](references/assessment.md)
- [AI career impact](references/ai_career_impact.md)
- [Salary data](references/salary_data.md)
- [Job demand](references/job_demand.md)
- [Education paths](references/education_paths.md)
- [Insurance broker channels and disclosures](references/insurance_broker_companies.json)
- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Publisher profile](https://clawhub.ai/user/mnetfairy)

## Skill Output:

**Output Type(s):** [Text, Career guidance, Analysis, Markdown report]

**Output Format:** [Conversational guidance and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized to user-provided context; optional insurance-channel lists, report export, and tracking are provided only on request.]

## Skill Version(s):

2.3.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
