## Description:

Pull LinkedIn person and company profiles, their posts, job listings and post comments as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured LinkedIn profile, company, post, comment, and job data through Scavio's API for prospecting, recruiting, and market research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve public personal and professional data that may be sensitive in recruiting, prospecting, or market research contexts.

Mitigation: Collect only data needed for the user's task, avoid invasive profiling or surveillance, and follow applicable privacy laws and platform terms.

Risk: The skill requires a Scavio API key for authenticated access.

Mitigation: Keep SCAVIO_API_KEY private, load it from the environment or a secret store, and do not include it in prompts, logs, or source files.

Risk: Paginated collection can spend credits quickly and gather more data than needed.

Mitigation: Set explicit page limits, estimate credit use before broad collection, and stop when the endpoint's documented pagination stop signal is reached.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/linkedin-scraper-api)
- [Scavio LinkedIn API documentation](https://scavio.dev/docs/linkedin-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON and paginated endpoints should be capped.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
