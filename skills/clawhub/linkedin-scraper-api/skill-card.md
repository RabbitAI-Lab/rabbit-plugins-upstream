## Description:

Pull LinkedIn person and company profiles, their posts, job listings and post comments as structured JSON. 9 endpoints from 1 to 30 credits, four of them paginated, for prospecting, recruiting, and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, recruiters, sales teams, and market researchers use this skill to retrieve structured LinkedIn profile, company, post, comment, and job data through Scavio for user-directed research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn identifiers and URLs are sent to Scavio under the user's API key.

Mitigation: Use the skill only for legitimate, user-directed research and avoid sending sensitive or unnecessary identifiers.

Risk: Paginated endpoints can spend credits quickly, especially job search and post feeds.

Mitigation: Set a clear page limit before calling paginated endpoints and explain the expected credit cost before running larger pulls.

Risk: Profile, post, comment, and job data can be misused for sensitive profiling or private inferences.

Mitigation: Return only API-provided data, do not infer private details, and review use against LinkedIn terms and applicable privacy laws.

Risk: Retired endpoints return permanent 410 responses and cannot provide the withdrawn datasets.

Mitigation: Treat 410 responses as permanent, report the data as unavailable, and use only documented substitutes where the skill identifies one.

## Reference(s):

- [Scavio LinkedIn API documentation](https://scavio.dev/docs/linkedin-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/linkedin-scraper-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON endpoint details and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
