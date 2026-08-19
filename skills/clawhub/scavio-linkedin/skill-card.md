## Description:

Pull LinkedIn person and company profiles, their posts, job listings and post comments as structured JSON for prospecting, recruiting, and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external teams use this skill to retrieve structured LinkedIn profile, company, post, comment, and job data through Scavio APIs for prospecting, recruiting, and market research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn public activity may be misused to infer private or sensitive traits.

Mitigation: Use returned public data only for lawful, appropriate workflows and avoid drawing private or sensitive conclusions from it.

Risk: API keys can be exposed if copied into source files or prompts.

Mitigation: Store SCAVIO_API_KEY in an environment secret or secret manager and keep it out of source control.

Risk: Paginated API calls can increase cost and collect more data than needed.

Mitigation: Set explicit page caps before running paginated endpoints and state the expected credit use before starting.

## Reference(s):

- [Scavio LinkedIn API documentation](https://scavio.dev/docs/linkedin-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-linkedin)
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with API request examples, shell setup commands, and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; paginated runs should be capped to manage API credits and data volume.]

## Skill Version(s):

2.1.3 (source: server release metadata; artifact frontmatter lists 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
