## Description:

Search Pinterest pins, pull one pin with its save/share counts, read a user's profile and boards, page through a board, and look up how often external URLs have been saved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured Pinterest search, pin, profile, board, and URL-save-count data through Scavio's API for visual content research, trend spotting, and creator analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinterest search terms, usernames, pin or board identifiers, and URL-stat lookup targets are sent to Scavio under the user's API key.

Mitigation: Avoid submitting sensitive private URLs or identifiers unless that is acceptable for the use case.

Risk: The skill requires a Scavio API key and consumes credits for each endpoint request.

Mitigation: Keep SCAVIO_API_KEY out of source control, monitor credit usage, and handle 401, 402, and 429 responses before retrying.

Risk: Returned Pinterest counts or URL statistics can be unavailable, exact-string dependent, zero, or stale.

Mitigation: Report only API-returned values, preserve pagination cursors, and avoid fabricating or extrapolating pins, counts, profiles, or board data.

## Reference(s):

- [Scavio API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)
- [Scavio Pinterest ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/pinterest-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands, API examples, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and returns cursor-paginated JSON for applicable endpoints.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
