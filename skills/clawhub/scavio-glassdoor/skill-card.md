## Description:

Resolve a company name to a Glassdoor employer id, then pull the employer profile with ratings and CEO approval, up to three full reviews, and salary percentiles by job title. 4 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, recruiting teams, and talent-intelligence users use this skill to query Scavio's Glassdoor endpoints for company profiles, employee-review snapshots, ratings, and salary percentiles by job title.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company searches and Glassdoor URLs are sent to Scavio.

Mitigation: Use the skill only with company lookup data appropriate to share with Scavio and keep SCAVIO_API_KEY scoped to the intended account.

Risk: Scavio API calls may consume credits even when responses are empty, failed, or slow.

Mitigation: Resolve the employer id first, reuse returned review and salary URLs, apply the documented 180-second timeout, and retry sparingly on transient failures.

Risk: Glassdoor review outputs are capped and salary values are estimates rather than complete datasets.

Mitigation: Present individual reviews as anecdotes, rely on aggregate rating fields for sentiment-shaped summaries, and label salary figures with currency, pay period, and estimate context.

## Reference(s):

- [Scavio Glassdoor Companies Documentation](https://scavio.dev/docs/glassdoor-companies)
- [Scavio](https://scavio.dev)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-glassdoor)
- [Publisher Profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown with inline code examples and structured JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and sends POST requests to Scavio's Glassdoor API endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
