## Description:

Query Google Play app data through a read-only API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to retrieve public Android app metadata, reviews, permissions, availability, data safety information, categories, suggestions, and related app records through ReplyNodes' read-only Google Play API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ReplyNodes API keys could be exposed in prompts, logs, URLs, reports, screenshots, or copied shell commands.

Mitigation: Store the key in a secret store or environment variable, pass it only in the Authorization header, and redact it from all shared output.

Risk: Batch requests, review pagination, or availability lookups could consume prepaid credits or create unexpectedly large request volumes.

Mitigation: Check the capabilities endpoint before use, confirm advertised credit costs, and enforce caller-side limits for batches, pagination, and country lists.

Risk: A missing or invalid API key, malformed input, provider timeout, or upstream failure could be misread as a valid empty result.

Mitigation: Handle HTTP status codes explicitly, preserve meta.request_id for debugging, and treat null fields as unknown rather than false or zero.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/googleplay-public-data-api)
- [ReplyNodes publisher profile](https://clawhub.ai/user/replynodes-ai)
- [ReplyNodes account signup](https://app.replynodes.com/auth)
- [ReplyNodes developer console](https://app.replynodes.com/developers)
- [ReplyNodes API gateway](https://api.replynodes.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API route tables and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes normalized JSON responses, request IDs, bounded pagination, and secret-safe API key handling.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
