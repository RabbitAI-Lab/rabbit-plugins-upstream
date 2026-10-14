## Description:

Resolves company names to Glassdoor employer IDs and retrieves employer profiles, ratings, up to three reviews, and salary percentiles through Scavio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, compensation analysts, and developers use this skill to research employers, compare workplace ratings, read a limited set of reviews, and benchmark estimated pay by job title.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, employer IDs, Glassdoor URLs, and the Scavio API key are sent to Scavio during use.

Mitigation: Review what will be shared before use and keep the API key in an environment variable or secret store.

Risk: Credit-based API calls can incur charges, including unnecessary retries or broad salary pagination.

Mitigation: Check credit costs and remaining balance; limit pagination and avoid unnecessary retries.

## Reference(s):

- [Scavio Glassdoor companies documentation](https://scavio.dev/docs/glassdoor-companies?utm_source=agent-skills&utm_medium=skill&utm_campaign=glassdoor-salary-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=glassdoor-salary-data)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance and code examples; structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reviews are limited to three per response; salary estimates include currency and pay period.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release; skill frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
