## Description:

Resolve a company name to a Glassdoor employer id, then pull the employer profile with ratings and CEO approval, up to three full reviews, and salary percentiles by job title.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Glassdoor employer identifiers and retrieve employer profiles, employee review summaries, and salary percentile data through Scavio. It supports company research, compensation benchmarking, employer-brand analysis, recruiting workflows, and talent intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employer lookup requests are sent through Scavio using the user's SCAVIO_API_KEY.

Mitigation: Install and use the skill only when that data flow is acceptable, and keep the API key in an environment variable or secret store.

Risk: Each endpoint call consumes one API credit, including empty, failed, or timed-out calls.

Mitigation: Resolve the employer once, reuse returned review and salary URLs, and avoid retry loops that spend credits without adding value.

Risk: Review responses are capped at three full reviews and should not be treated as a representative sample.

Mitigation: Use aggregate ratings, distributions, highlights, and counts for summaries, and treat individual reviews as anecdotes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/glassdoor-salary-data)
- [Scavio Glassdoor Companies documentation](https://scavio.dev/docs/glassdoor-companies)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples and structured JSON response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Glassdoor API calls consume credits and may require client timeouts of at least 180 seconds.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
