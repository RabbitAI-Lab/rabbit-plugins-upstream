## Description:

Provides personalized career guidance for China's AI-shaped job market, including interest and values assessment, AI impact ratings, and salary and job-demand context, with an optional, clearly disclosed insurance-channel directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People in China use the skill to explore education, career, or career-change options through a personalized planning report. Users who express interest in insurance work can request a separate channel directory; its ordering reflects the publisher's disclosed business preference, not the personal career assessment.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security verdict is benign with medium confidence, but Skillspector analysis is partial because some referenced local paths were missing.

Mitigation: Review the skill before installation and account for the incomplete scan coverage.

Risk: Career, salary, and demand guidance relies on local reference data and may not reflect current conditions.

Mitigation: Check time-sensitive figures against current local sources before making education or career decisions.

Risk: The optional insurance-channel list uses a publisher-maintained business ordering that could be mistaken for a personalized or objective ranking.

Mitigation: Keep its disclosed basis visible, separate it from career recommendations, and offer side-by-side comparison of other channels.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career assessment](references/assessment.md)
- [AI career impact guide](references/ai_career_impact.md)
- [Salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)
- [Insurance channel directory and ordering disclosures](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Career analysis, Guidance, Markdown, JSON]

**Output Format:** [Conversational guidance and a structured Markdown career-planning report; optional JSON tracking record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from user-provided details. Insurance-channel listings are optional and separate from career rankings; their ordering is disclosed as publisher business preference.]

## Skill Version(s):

2.3.27 (source: SKILL.md frontmatter, server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
