## Description:

Resolve any place or business name to Tripadvisor ids, then pull ranked restaurants, hotels and attractions in a geo, one location in full, and paged review bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve structured Tripadvisor location, ranking, venue, and review data for restaurants, hotels, attractions, destination research, competitive comparisons, and reputation monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested place and review lookups to Scavio.

Mitigation: Use the skill only for queries that may be shared with the external Scavio API.

Risk: The skill consumes paid API credits per request, including unnecessary empty, duplicate, or excess paging calls.

Mitigation: Resolve ids first, reuse the first review page returned by the location endpoint, de-duplicate paged reviews, and avoid paging beyond the needed results.

Risk: The Scavio API key could be exposed if placed in source or logs.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and keep it out of source control and generated output.

## Reference(s):

- [Scavio Tripadvisor Locations Documentation](https://scavio.dev/docs/tripadvisor-locations)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/tripadvisor-reviews-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API details and Python, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses guide an agent through authenticated Scavio API requests and structured JSON interpretation.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
