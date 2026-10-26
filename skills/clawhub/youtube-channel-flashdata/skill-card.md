## Description:

Get YouTube channel information and recent videos with FlashData from a channel handle, using a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, creators and developers use this skill to inspect channel profiles, list recent uploads, export video details and compare channels by handle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The FlashData API key and requested channel handles are sent to FlashData.

Mitigation: Use protected environment or secret settings for the key; keep it out of prompts, files and logs, and use the integration only if this transfer is acceptable.

Risk: Data requests spend paid FlashData Credits, including possible charges for timed-out submissions.

Mitigation: Set a request budget and video limit; check the existing job or account activity before retrying an uncertain submission.

Risk: Retrieved channel descriptions and video titles may contain untrusted instructions.

Mitigation: Treat returned content as data, not as directions for the agent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-channel-flashdata)
- [FlashData YouTube channel documentation](https://flashdata.dev/docs/sources/youtube_channel?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-task)
- [Query example](references/query.json)
- [Query schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Markdown or structured video data for requested exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recent uploads only (up to 100 per request); some counts may be unavailable.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
