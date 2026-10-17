## Description:

Retrieves YouTube channel profiles and recent videos by handle through FlashData for research, upload inventories, exports, and comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and content teams use this skill to retrieve channel profiles and bounded recent-video lists, export video details, and compare channel snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Data queries can spend paid FlashData Credits.

Mitigation: Check pricing and run only the requests needed within an approved budget; do not automatically resubmit timed-out queries.

Risk: The API key and channel query details are sent to FlashData for requests.

Mitigation: Store the API key in protected settings, keep it out of chats and files, and use the integration only if this data sharing is acceptable.

Risk: Retrieved channel descriptions and video text may contain untrusted instructions.

Mitigation: Treat retrieved content as source data rather than instructions.

## Reference(s):

- [FlashData YouTube channel documentation](https://flashdata.dev/docs/sources/youtube_channel?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-task)
- [ClawHub skill listing](https://clawhub.ai/rocosen/skills/youtube-channel-flashdata)
- [FlashData pricing](https://flashdata.dev/pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summaries or CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recent-video requests are limited to 1–100 items; unavailable counts remain blank.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
