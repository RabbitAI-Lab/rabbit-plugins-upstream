## Description:

A conversational career-planning skill that helps people assess their interests and values, consider AI's effects on work, and build a personalized career plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People considering career, education, or job-transition choices use the skill to reflect on their interests and values, understand possible AI-related changes to work, and receive practical next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports writes or persistent storage beyond the stated scope.

Mitigation: Review and constrain export and storage paths, and allow report export only when the user requests it.

Risk: ClawScan flags a fixed preference in the insurer recommendations.

Mitigation: Review the prioritization basis, disclose it clearly, and make alternative providers available for comparison.

Risk: The security scan is incomplete: 25 of 26 components were fully covered, and the salary database was only partially inspected.

Mitigation: Complete review of the remaining component and salary database before relying on the assessment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchor reference](references/career_anchor.md)
- [Job demand trends](references/job_demand.md)
- [Salary reference data](references/salary_data.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured Markdown career plans; optional Markdown file export on explicit request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from user-provided information and local reference files; career and AI-impact assessments are guidance rather than predictions.]

## Skill Version(s):

2.3.7 (source: release evidence, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
