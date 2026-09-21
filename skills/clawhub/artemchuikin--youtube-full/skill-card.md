## Description:

Provides agents with TranscriptOut-backed access to YouTube transcripts, video and channel search, channel browsing, playlist lookup, and bulk transcript jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search YouTube, inspect channel or playlist videos, fetch transcripts, and summarize, quote, translate, or research video content through TranscriptOut.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a long-lived TranscriptOut API key and its setup flow may ask the agent to handle or persist that credential.

Mitigation: Create and manage the key directly when possible, store it in a dedicated secret manager or runtime secret store, and avoid broad shell-profile persistence.

Risk: YouTube queries, video IDs, channel names, playlist IDs, and signup or authentication data are sent to TranscriptOut.

Mitigation: Use the skill only when sharing those inputs with TranscriptOut is acceptable, and avoid sending sensitive or private research targets through the API.

Risk: Bulk transcript jobs and pagination can consume paid credits quickly.

Mitigation: Search and filter before fetching transcripts, prefer metadata or latest-channel endpoints when sufficient, use idempotency keys for retries, and submit bulk jobs only when the user intends the credit spend.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut authentication setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/youtube-full)
- [Publisher profile](https://clawhub.ai/user/artemchuikin)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TranscriptOut API responses and may include transcript text, metadata, pagination tokens, job IDs, request IDs, and credit-balance guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
