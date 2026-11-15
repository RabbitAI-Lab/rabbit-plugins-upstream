## Description:

Read YouTube video metadata with FlashData: title, description, channel, statistics, chapters and available media formats. Use to inspect a known video, build video cards, create chapter links or choose download options. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content researchers use this skill to inspect a known YouTube video and create metadata summaries, video cards, chapter navigation links, or compare available media formats. Queries require a FlashData API key and spend paid Credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Metadata queries connect to FlashData's hosted service and spend FlashData Credits.

Mitigation: Check pricing and the user's approved budget, and request only the metadata fields needed for the task.

Risk: The skill requires a FlashData API key, and security scan coverage was partial with medium confidence.

Mitigation: Keep FLASHDATA_API_KEY in protected client settings, never in prompts or skill files, and review unresolved local references before enabling the skill.

## Reference(s):

- [FlashData YouTube metadata documentation](https://flashdata.dev/docs/sources/youtube_metadata?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task)
- [FlashData MCP documentation](https://flashdata.dev/mcp?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task)
- [ClawHub release page](https://clawhub.ai/rocosen/skills/youtube-metadata-flashdata)
- [Request schema](references/schema.json)
- [Example request](references/query.json)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured video metadata as JSON, with text or Markdown summaries, video cards, and timestamped chapter links as requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional statistics, chapters, and format details may be unavailable; the metadata query does not download media.]

## Skill Version(s):

1.0.2 (source: frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
