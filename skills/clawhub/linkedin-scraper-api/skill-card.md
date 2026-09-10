## Description:

Pull LinkedIn person and company profiles, their posts, job listings and post comments as structured JSON for prospecting, recruiting, and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to query Scavio's LinkedIn API for structured person, company, post, comment, and job data. Typical workflows include B2B prospecting, recruiting research, and market research where API credit cost and pagination limits need to be planned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an API key and normal API-key handling mistakes could expose access to the Scavio API.

Mitigation: Install in a dedicated virtual environment, avoid elevated pip usage, and expose only SCAVIO_API_KEY to the process.

Risk: Paginated or high-cost endpoints can spend credits quickly if an agent loops or fetches broad result sets.

Mitigation: Review Scavio billing terms before use, cap pagination, and estimate credit cost before running large prospecting or recruiting workflows.

Risk: LinkedIn-derived public profile data can be misused if an agent infers private details or overstates completeness.

Mitigation: Review Scavio data-handling terms, return only API data, and avoid inferring private details or presenting rotating search results as exhaustive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/linkedin-scraper-api)
- [Scavio LinkedIn API Documentation](https://scavio.dev/docs/linkedin-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-scraper-api)

## Skill Output:

**Output Type(s):** [JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and Python or bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON and endpoint usage can consume paid credits.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
