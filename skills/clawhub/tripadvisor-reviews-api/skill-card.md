## Description:

Resolve any place or business name to Tripadvisor ids, then pull ranked restaurants, hotels and attractions in a geo, one location in full, and paged review bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Tripadvisor place names to IDs, retrieve ranked hotels, restaurants, and attractions, and collect venue details or paged reviews for travel research, competitive analysis, and reputation monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tripadvisor queries are sent to Scavio and may consume account credits.

Mitigation: Confirm the user wants to spend credits before making calls, avoid redundant requests, and review Scavio's data-use terms before deployment.

Risk: The skill requires a Scavio API key.

Mitigation: Store SCAVIO_API_KEY in a secure environment or secret store and keep it out of source code and shared logs.

Risk: Incorrect IDs, categories, or pagination can produce missing, repeated, or billed error responses.

Mitigation: Resolve names with the locations endpoint, keep category aligned with the venue type, de-duplicate reviews by review_id, and avoid requesting pages beyond the last known page.

## Reference(s):

- [Scavio Tripadvisor Locations Documentation](https://scavio.dev/docs/tripadvisor-locations)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with JSON examples, API parameters, and inline Python, JavaScript, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on structured JSON API responses returned by Scavio's Tripadvisor endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
