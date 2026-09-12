## Description:

Search Indeed job postings, pull one posting in full with its original ATS link, and read employer profiles and employee reviews. 4 endpoints, 2 credits each, structured JSON for recruiting and labour-market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and talent-intelligence teams use this skill to search Indeed postings, retrieve full job details, inspect employer profiles, and read employee reviews through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key for authenticated requests.

Mitigation: Store SCAVIO_API_KEY in the environment or a secret manager and avoid embedding live keys in source code.

Risk: Search pages, review pages, empty results, and 404 responses can consume paid credits.

Mitigation: Cap loops, state the expected credit spend before bulk calls, and derive job keys or company slugs from returned results before requesting detail endpoints.

Risk: Unsupported Indeed filter values may be ignored while still returning billable results.

Mitigation: Use only documented radius and max_age_days values, round user requests to the nearest supported value, and tell the user when rounding occurs.

Risk: Optional SDK installation introduces ordinary third-party package supply-chain exposure.

Mitigation: Prefer the documented direct HTTPS examples when possible, or install pinned SDK versions in an isolated environment.

## Reference(s):

- [Scavio Indeed API documentation](https://scavio.dev/docs/indeed-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=indeed-jobs-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=indeed-jobs-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/indeed-jobs-api)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with JSON response descriptions and inline Python, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns structured JSON from Scavio's Indeed endpoints.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
