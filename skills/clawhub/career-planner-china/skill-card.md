## Description:

Guides people in China through education and career choices with personalized assessment, AI-era job impact analysis, and practical next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Students and working adults in China use the skill to explore education choices, career changes, and future job options. It gathers the user's background and preferences, then provides career assessment, AI impact considerations, and an actionable plan; insurance channel information is shown only when the user expresses interest.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security review was partial because some referenced paths were missing, so it does not cover the complete release with full confidence.

Mitigation: Check that the complete release package is present and review or scan it again before installation.

Risk: Career, job demand, and salary guidance relies on bundled local reference material and may not reflect current conditions.

Mitigation: Treat projections and salary figures as indicative, and confirm important decisions against current local sources.

Risk: When the user asks about insurance careers, channel ordering reflects the maintainer's business preference rather than personalized suitability.

Mitigation: Disclose the basis of the ordering and offer a side-by-side comparison of other channels on request.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career assessment framework](references/assessment.md)
- [AI career impact guidance](references/ai_career_impact.md)
- [Salary reference](references/salary_data.md)
- [Career tracking guidance](references/tracker_system.md)
- [Insurance channel disclosures](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Personalized Chinese-language career guidance and structured Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are based on information provided by the user and local reference material. A Markdown report can be exported on request to the skill's exports directory.]

## Skill Version(s):

2.3.26 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
