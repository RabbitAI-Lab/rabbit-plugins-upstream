## Description:

Search Pinterest pins, pull one pin with its save/share counts, read a user's profile and boards, page through a board, and look up how often external URLs have been saved. 6 endpoints, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve public Pinterest pins, profiles, boards, and URL save counts through Scavio for content research, trend analysis, and creator or influencer analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinterest searches, usernames, pin or board URLs, and external URLs are sent to Scavio for third-party processing.

Mitigation: Avoid sensitive investigations or private identifiers unless the user accepts that third-party processing.

Risk: The SCAVIO_API_KEY could be exposed if placed in source code, logs, or shared transcripts.

Mitigation: Load the key from the environment or a secret store and keep it out of source control.

Risk: URL save counts can be stale or differ by exact URL string.

Mitigation: Preserve exact URLs, report API results as returned, and avoid fabricating or extrapolating counts.

Risk: Pin descriptions and public profiles may contain people-authored personal information.

Mitigation: Summarize results and avoid building profiles of individuals.

## Reference(s):

- [Scavio Pinterest API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-pinterest)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API request and response details plus Python and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY; API responses include data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
