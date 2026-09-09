## Description:

Resolve a company name to a Glassdoor employer id, then pull the employer profile with ratings and CEO approval, up to three full reviews, and salary percentiles by job title.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up Glassdoor employer profile data, employee review summaries, and salary percentiles by job title through Scavio's API. It supports company research, recruiting, employer-brand analysis, and compensation benchmarking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lookup inputs are sent to Scavio and each API call can spend credits.

Mitigation: Confirm Scavio is an acceptable data provider before use, keep SCAVIO_API_KEY in an environment variable or secret store, and check expected credit use before running calls.

Risk: Glassdoor reviews are capped at three per response, so individual reviews can mislead if treated as representative.

Mitigation: Use aggregate fields such as rating distribution, category ratings, highlights, and review counts for sentiment-shaped analysis, and present individual reviews only as anecdotes.

Risk: Salary values are estimates by job title rather than individual reported salaries.

Mitigation: Label salary figures as estimates and include the pay period, currency, sample counts, and reported percentile fields when presenting them.

Risk: Glassdoor endpoints can be slow or temporarily unavailable, and failed calls may still consume credits.

Mitigation: Use at least a 180 second client timeout, retry sparingly on temporary failures, and avoid tight retry loops.

## Reference(s):

- [Scavio Glassdoor Companies documentation](https://scavio.dev/docs/glassdoor-companies?utm_source=agent-skills&utm_medium=skill&utm_campaign=glassdoor-salary-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=glassdoor-salary-data)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/glassdoor-salary-data)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with API examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoints use Scavio API credits and may require long client timeouts.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
