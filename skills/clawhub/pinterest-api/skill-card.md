## Description:

Search Pinterest pins, pull one pin with its save/share counts, read a user's profile and boards, page through a board, and look up how often external URLs have been saved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content researchers use this skill to query Pinterest search results, pins, public profiles, boards, and URL save counts through structured API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinterest queries, usernames, board or pin identifiers, and URL-stat lookups are sent to Scavio with the user's API key.

Mitigation: Install only when this data sharing is acceptable for the intended use case, and keep the API key in an environment variable or secret store.

Risk: Credit-backed API calls can consume account balance, including empty results or retries.

Mitigation: Monitor credit usage and handle 402, 429, 502, and 503 responses before retrying or continuing at scale.

Risk: Returned public profile data could be misused to make sensitive judgments about individuals.

Mitigation: Summarize public profile data cautiously and avoid using it for sensitive profiling or consequential decisions.

## Reference(s):

- [Scavio Pinterest API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/pinterest-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with HTTP request examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. API responses include data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
