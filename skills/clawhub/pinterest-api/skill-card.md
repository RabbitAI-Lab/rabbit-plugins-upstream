## Description:

Search Pinterest pins, retrieve detailed pin data, read public profiles and boards, page through board pins, and look up external URL save counts through Scavio's structured Pinterest API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform Pinterest content research, trend analysis, creator research, and structured retrieval of public pin, profile, board, and URL save-count data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to Scavio as a third-party service and depends on a SCAVIO_API_KEY.

Mitigation: Use an environment variable or secret store for SCAVIO_API_KEY, avoid committing keys to source control, and install only when third-party service use is acceptable.

Risk: Public profile and board data can be misused to build detailed profiles of private individuals.

Mitigation: Summarize public data for the user's task and avoid creating detailed profiles of private individuals.

Risk: Pinterest counts and URL-stat matching can be stale, zero, or sensitive to exact URL variants.

Mitigation: Report API-returned values without fabrication and preserve URL variants when interpreting save-count results.

## Reference(s):

- [Scavio Pinterest API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON API request and response handling examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls return structured JSON envelopes with data, response time, credits used, and credits remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
