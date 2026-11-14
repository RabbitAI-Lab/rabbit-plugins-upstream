## Description:

Retrieve YouTube captions and subtitle segments with FlashData. Use for uploader-provided subtitles, language-specific caption tracks and SRT or WebVTT exports. Selects manual captions by default. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can retrieve an existing YouTube caption track in a chosen language, then use its text and timestamps or export the timed segments as SRT or WebVTT.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill connects to FlashData, requires an API key, and queries use paid Credits.

Mitigation: Keep the key in protected settings and review pricing and the intended query budget before making requests.

Risk: ClawScan reports incomplete coverage because two local path references could not be resolved.

Mitigation: Review the unresolved references before relying on the scan result or installing the skill.

Risk: A timed-out paid submission can have an unknown outcome and a retry may submit another paid request.

Mitigation: Check the existing job or FlashData console before retrying; do not automatically resubmit.

## Reference(s):

- [FlashData YouTube Captions documentation](https://flashdata.dev/docs/sources/youtube_captions?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_captions-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_captions-task)
- [ClawHub skill page](https://clawhub.ai/rocosen/skills/youtube-captions-flashdata)

## Skill Output:

**Output Type(s):** [Text, JSON, SRT, WebVTT]

**Output Format:** [Caption text or timed segments; subtitle exports use SRT or WebVTT]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the selected track's wording and timing; captions are retrieved from an existing track.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
