## Description:

Helps people plan career choices and transitions in China using personal assessments and information about AI, industries, jobs, salaries, and education paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People in China use the skill to explore suitable careers, assess interests and work values, consider how AI may affect roles, and turn the discussion into practical next steps. It can also provide insurance-channel information when the user explicitly asks about insurance careers.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Security analysis was partial because some referenced local files did not match the bundled files; the release also includes an executable report-generation script and optional career tracking.

Mitigation: Review the bundled references and script before use. Keep report export and tracking off unless the user requests them, and use the documented export directory and deletion controls for any saved tracking data.

Risk: Insurance-channel ordering reflects the maintainer's disclosed commercial preference and is separate from personalized career-fit recommendations.

Mitigation: Only provide the channel list when the user explicitly asks about insurance careers or channels, disclose the basis for the ordering, and offer side-by-side comparison with other channels.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Publisher profile](https://clawhub.ai/user/mnetfairy)
- [Skill instructions and scope](artifact/SKILL.md)
- [Career assessment methods](artifact/references/assessment.md)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Industry trends reference](artifact/references/industry_trends.md)
- [Job demand reference](artifact/references/job_demand.md)
- [Salary reference](artifact/references/salary_data.md)
- [Education paths reference](artifact/references/education_paths.md)
- [Insurance channel data and disclosures](artifact/references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Files]

**Output Format:** [Conversational guidance and structured Markdown career reports; optional exported Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized to the user's background and goals; may include career assessments, AI impact ratings, salary and demand context, learning paths, and action steps. Report export and career tracking are optional and require an explicit user request.]

## Skill Version(s):

2.3.13 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
