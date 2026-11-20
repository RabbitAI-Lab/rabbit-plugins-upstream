## Description:

Guides users through AI-era career planning with interest and values assessments, career impact analysis, and personalized recommendations, with an optional insurance-channel directory available on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People exploring education choices, career changes, or future job options use guided conversation and local reference material to assess interests, values, AI-related job changes, and practical next steps. The optional insurance-channel directory is separate from personalized career recommendations and has a maintainer-set ordering that is disclosed to users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security analysis was marked partial because some referenced paths were missing, so its benign verdict has incomplete coverage.

Mitigation: Review the full release, especially the optional tracking and report-export behavior, before relying on the scan result.

Risk: The optional insurance-channel directory uses a maintainer-set commercial ordering that is not an assessment of user fit.

Mitigation: Disclose the ordering when presenting the directory, keep it separate from career recommendations, and offer side-by-side comparisons with other channels.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment framework](references/assessment.md)
- [AI career impact guidance](references/ai_career_impact.md)
- [Salary reference data](references/salary_data.md)
- [Industry trends](references/industry_trends.md)
- [Insurance channel directory and disclosures](references/insurance_broker_companies.json)
- [AXA company information](https://www.axa.com.hk/zh/who-we-are)

## Skill Output:

**Output Type(s):** [Career guidance, Analysis, Text, Markdown]

**Output Format:** [Conversational guidance and structured Markdown reports, including recommendations, AI impact ratings, and action steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are based on user-provided information and local reference materials. Optional insurance-channel information is provided only on request and separately from personalized career recommendations.]

## Skill Version(s):

2.3.22 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
