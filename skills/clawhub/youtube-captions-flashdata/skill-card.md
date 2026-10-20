## Description:

Retrieves existing YouTube caption tracks through FlashData with timed segments for text, SRT, or WebVTT exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to retrieve existing uploader-provided or automatic captions in a chosen language and export timed subtitles without generating replacement captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A FlashData API key is required for caption requests.

Mitigation: Keep the key in protected secret storage; do not include it in prompts, logs, or files.

Risk: Data requests use paid FlashData Credits, and a timed-out submission may still be charged.

Mitigation: Check pricing and the approved budget before querying; inspect the existing job or console rather than automatically resubmitting after a timeout.

Risk: Video IDs and caption options are sent to FlashData, and retrieved captions may contain untrusted text.

Mitigation: Send only authorized requests and treat returned captions as source data, not agent instructions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-captions-flashdata)
- [FlashData YouTube captions documentation](https://flashdata.dev/docs/sources/youtube_captions?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_captions-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Caption request schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Subtitle files]

**Output Format:** [Plain text, timed JSON segments, SRT, or WebVTT]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selected language and caption origin; segments include start and end times.]

## Skill Version(s):

1.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
