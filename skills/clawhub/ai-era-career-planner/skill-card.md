## Description:

Guides users through a personalized career plan using interest and values assessments and an evaluation of AI's impact on career options; optional insurance channel information is provided only when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People considering education or career changes use the skill to reflect on their interests, values, strengths and goals, then receive career options, learning steps and context about AI's potential effects. On explicit request, it can also provide insurance channel information; the channel ordering is a maintainer business preference, separate from personalized career recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports benign findings at medium confidence, but scan coverage is partial because some referenced local paths did not match bundled files.

Mitigation: Review available reference files and verify current salary, job demand and other time-sensitive claims before relying on them.

Risk: The optional insurance channel list uses a maintainer-set business priority that does not represent personalized suitability.

Mitigation: Disclose the business preference and offer side-by-side alternatives; keep the channel list separate from career assessment and recommendations.

Risk: Optional tracking can retain user-provided career goals and assessment details in a local file.

Mitigation: Create tracking records only on explicit request, store only the documented minimal fields, and explain the 90-day default retention and deletion option.

## Reference(s):

- [Assessment methods](references/assessment.md)
- [AI and career impact reference](references/ai_career_impact.md)
- [Career conversation flow](references/flow_engine.md)
- [Industry trends](references/industry_trends.md)
- [Salary reference data](references/salary_data.md)
- [Education paths](references/education_paths.md)
- [Insurance channel data and disclosures](references/insurance_broker_companies.json)
- [Optional career tracking and retention](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational guidance and structured career plan reports; optional Markdown exports and JSON tracking records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from user-provided information and bundled local references; export and tracking are optional and require an explicit user request.]

## Skill Version(s):

2.3.14 (source: ClawHub release evidence, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
