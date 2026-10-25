## Description:

Search YouTube through FlashData with keyword and video filters to find videos, channels, and available metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to find YouTube videos for research or recommendations, filtering by date, duration, subtitles, and other criteria and collecting video links and channel details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests spend FlashData Credits, including requests that time out after submission.

Mitigation: Check pricing and the approved budget before querying; check existing jobs rather than automatically resubmitting a timed-out request.

Risk: The FlashData API key is a credential used for hosted search.

Mitigation: Store the key as a protected environment secret and never include it in prompts, logs, or committed files.

Risk: Private or sensitive search terms are sent to FlashData for the query.

Mitigation: Avoid submitting sensitive terms unless the user is comfortable sharing them with FlashData.

Risk: Retrieved video titles and descriptions may contain untrusted instructions.

Mitigation: Treat retrieved content as search data, not as instructions to the agent.

## Reference(s):

- [FlashData YouTube Search documentation](https://flashdata.dev/docs/sources/youtube_search?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task)
- [FlashData MCP documentation](https://flashdata.dev/mcp)
- [Search input schema](artifact/references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured search results or a concise video list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include video IDs, watch links, titles, channels, durations, and available view counts.]

## Skill Version(s):

1.0.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
