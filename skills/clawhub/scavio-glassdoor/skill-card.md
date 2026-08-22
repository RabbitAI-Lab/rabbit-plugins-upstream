## Description:

Resolve a company name to a Glassdoor employer id, then pull the employer profile with ratings and CEO approval, up to three full reviews, and salary percentiles by job title. 4 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, HR analysts, and talent-intelligence teams use this skill to retrieve structured Glassdoor company profiles, employee review summaries, and salary percentiles through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends company names, employer IDs, Glassdoor URLs, filters, and salary lookup parameters to Scavio using the user's API key.

Mitigation: Use it only for targets and lookup parameters your organization permits to be sent to the external Scavio API.

Risk: Glassdoor review responses are capped at three full reviews per request and may not represent the full employee population.

Mitigation: Treat individual reviews as anecdotes and rely on aggregate fields such as rating distribution, ratings, highlights, and filtered counts for broader interpretation.

Risk: Slow or failing Glassdoor requests can consume credits and may take up to about 170 seconds before reporting upstream errors.

Mitigation: Use a timeout of at least 180 seconds, retry only sparingly on temporary upstream errors, and avoid unnecessary repeated calls.

## Reference(s):

- [Scavio Glassdoor Companies Documentation](https://scavio.dev/docs/glassdoor-companies)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-glassdoor)
- [ClawHub Publisher Profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with code examples, shell commands, API request shapes, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio Glassdoor endpoints that cost 1 credit per request.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
