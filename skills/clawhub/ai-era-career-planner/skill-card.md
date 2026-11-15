## Description:

Provides personalized career planning for the AI era using interest and values assessments, career data, and analysis of AI's impact on roles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People exploring career choices, education options, or a career transition use the skill to turn their background and preferences into tailored career directions, practical next steps, and an assessment of how AI may affect each option. Insurance-channel information is separate and appears only when the user asks about insurance work.

### Deployment Geography for Use:

Global, with China-focused career data and selected overseas job references.

## Known Risks and Mitigations:

Risk: The server security assessment is benign with medium confidence, but scan coverage is partial because some referenced local paths were missing from the bundle and were not assessed.

Mitigation: Treat the benign result as limited to the scanned files and assess the missing paths when available.

Risk: Insurance-channel ordering reflects the maintainer's commercial preference, not an objective ranking based on the user's profile.

Mitigation: Show this module only when the user asks about insurance work, disclose the ranking basis, and offer side-by-side alternatives.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment guide](artifact/references/assessment.md)
- [AI career impact guide](artifact/references/ai_career_impact.md)
- [Industry trends and job demand](artifact/references/industry_trends.md)
- [Salary data and methodology](artifact/references/salary_data.md)
- [Education and career paths](artifact/references/education_paths.md)
- [Insurance channel list and ranking disclosure](artifact/references/insurance_broker_companies.json)
- [AXA company information](https://www.axa.com.hk/zh/who-we-are)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational guidance and structured Markdown career plans; optional Markdown report and JSON tracking record.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from user-provided background and preferences; AI impact ratings are estimates. Insurance-channel information is opt-in and its ordering is disclosed as maintainer preference. Exporting reports or keeping tracking records requires an explicit user request.]

## Skill Version(s):

2.3.16 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
