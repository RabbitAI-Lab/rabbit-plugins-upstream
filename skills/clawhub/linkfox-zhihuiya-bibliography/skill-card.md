## Description:

Queries Zhihuiya patent bibliography records by patent ID or publication number and returns factual patent metadata such as titles, applicants, inventors, classifications, citations, abstracts, and dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent researchers, IP professionals, and developers use this skill to retrieve bibliography metadata for known patent IDs or publication numbers. It is intended for factual lookup and presentation of patent records, not patent search, valuation, legal-status analysis, or infringement advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox/Zhihuiya API credentials and includes in-chat phone/SMS onboarding for missing keys.

Mitigation: Prefer self-service account setup outside the skill, confirm endpoint environment variables are not overridden, and avoid sharing credentials in chat.

Risk: Complete patent responses are written to local session and cache files.

Mitigation: Use the skill only in workspaces where local storage of patent research is acceptable, and clear ./linkfox/ session or cache data when retention is not desired.

Risk: Lookups consume credits and the onboarding flow can create payment orders.

Mitigation: Warn users before paid lookups, avoid automatic retries or exploratory re-queries, and verify plan and payment details before ordering credits.

Risk: The server security summary notes automatic feedback reporting in addition to patent lookup behavior.

Mitigation: Avoid sending confidential patent research in feedback and review whether feedback reporting is acceptable for the deployment environment.

## Reference(s):

- [智慧芽-著录项目 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-bibliography)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries and tables for users, with JSON API responses saved to local files when the script runs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts patentId or patentNumber values, up to 100 comma-separated identifiers per request; the script uses a 24-hour local cache and stores complete responses under ./linkfox/.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
