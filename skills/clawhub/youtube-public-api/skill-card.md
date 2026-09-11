## Description:

Read-only YouTube data API for video, channel, playlist, comments, related-video, search, and transcript research through ReplyNodes prepaid credits with one long-lived Bearer fetcher key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public YouTube search results, video and channel metadata, playlist contents, public comments, related videos, and available transcripts through ReplyNodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube query, video, channel, playlist, comment, and transcript requests are sent to ReplyNodes.

Mitigation: Use the skill only when sending those public-data requests to ReplyNodes is acceptable for the task.

Risk: The ReplyNodes fetcher key can authorize prepaid-credit usage if exposed.

Mitigation: Store the key only in the agent secret store and never place it in prompts, source files, logs, URLs, or returned data.

Risk: Transcript requests cost substantially more prepaid credits than standard reads.

Mitigation: Monitor transcript calls and set explicit paid-overage caps where available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/youtube-public-api)
- [Operations reference](artifact/references/operations.json)
- [ReplyNodes API gateway](https://api.replynodes.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP GET examples and public YouTube API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the ReplyNodes response envelope and request ID when reporting results.]

## Skill Version(s):

2.0.1 (source: frontmatter, manifest, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
