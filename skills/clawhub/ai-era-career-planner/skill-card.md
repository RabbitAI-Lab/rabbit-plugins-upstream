## Description:

Guides users through career planning for the AI era with interest and values assessments, career impact analysis, and a personalized action plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People choosing a major, changing careers, or planning their next career step use the skill to discuss their interests and values, consider how AI may affect career options, and receive a practical plan. If they explicitly ask about insurance work, the skill can provide channel information; its disclosed maintainer preference is separate from personalized career recommendations.

### Deployment Geography for Use:

Global; Chinese-language guidance with China-focused data and selected overseas job references.

## Known Risks and Mitigations:

Risk: The security scan found no issues but reported partial analysis because some local references were missing, limiting evidence for optional tracking or report export.

Mitigation: Review the packaged references and report-generation behavior before enabling optional tracking or report export.

Risk: The insurance channel list uses a maintainer-set commercial priority that could be mistaken for personalized or objective ranking.

Mitigation: Keep the disclosed preference separate from career recommendations and offer side-by-side channel comparisons when requested.

## Reference(s):

- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Salary reference](references/salary_data.md)
- [Insurance channel information](references/insurance_broker_companies.json)
- [AXA company information](https://www.axa.com.hk/zh/who-we-are)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational guidance and a structured career-planning report in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized to user-provided background and preferences; optional Markdown export and tracking are user-requested features.]

## Skill Version(s):

2.3.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
