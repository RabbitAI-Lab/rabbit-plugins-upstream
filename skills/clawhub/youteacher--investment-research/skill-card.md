## Description:

Retrieves company filings and reported facts and prepares sourced investment-research summaries with risk context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research teams use this skill to review public company filings and reported facts, identify evidence-backed risks, and prepare sourced research reports. It does not provide trading instructions or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and company queries sent to a remote service may be sensitive.

Mitigation: Use the service only if trusted, protect the API key, and handle queries, task IDs, reports, and local response files as potentially sensitive.

Risk: Historical filings or partial search results may be mistaken for current or complete financial evidence.

Mitigation: Preserve source and filing dates, distinguish missing data from absent facts, and disclose partial results and limitations.

Risk: Research outputs may be misused as trading instructions or financial advice.

Mitigation: Keep the information-only disclaimer and do not use the skill for automated trading or personalized investment recommendations.

## Reference(s):

- [ClawHub investment-research release](https://clawhub.ai/youteacher/skills/investment-research)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/investment-research/API-KEY.md)
- [Operations contract](https://ai-skills.open-idea.net/skill-docs/investment-research/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/investment-research/HTTP-REQUESTS.md)
- [Source and investment safety rules](https://ai-skills.open-idea.net/skill-docs/investment-research/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Sourced research summaries and reports with risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes filing dates and source references, identifies partial or missing results, and states that outputs are not investment advice.]

## Skill Version(s):

1.7.0 (source: ClawHub release metadata and skill packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
