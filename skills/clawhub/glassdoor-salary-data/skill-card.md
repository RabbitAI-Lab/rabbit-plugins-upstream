## Description:

Resolve a company name to a Glassdoor employer id, then pull the employer profile with ratings and CEO approval, up to three full reviews, and salary percentiles by job title.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Scavio's Glassdoor API for employer profile, review, and salary-percentile data when researching companies, benchmarking compensation, or comparing employer brand signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lookup requests are sent to Scavio and require a SCAVIO_API_KEY that may consume credits.

Mitigation: Use only the required API key, keep it out of source control, and confirm the user is comfortable with Scavio processing the lookup request and spending credits.

Risk: Optional SDK installation introduces package-registry supply-chain exposure.

Mitigation: Prefer documented direct HTTPS requests for stricter environments, or install the SDK in an isolated environment with only the required API key exposed.

Risk: Glassdoor review responses are limited to a small number of reviews and may not represent the full employee population.

Mitigation: Use aggregate rating, distribution, highlight, and count fields for conclusions, and treat individual reviews as anecdotes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/glassdoor-salary-data)
- [Scavio Glassdoor Companies API Documentation](https://scavio.dev/docs/glassdoor-companies?utm_source=agent-skills&utm_medium=skill&utm_campaign=glassdoor-salary-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=glassdoor-salary-data)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with code snippets and structured JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Glassdoor calls can be slow; endpoints cost credits; review responses are capped at three reviews.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
