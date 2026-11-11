## Description:

Extracts transcripts and video details from public short videos on Xiaohongshu, Douyin, Kuaishou, Weibo, and WeChat Channels, with copy-ready text and optional SRT subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and social media teams use this skill to turn public video links, share text, or platform IDs into video details and transcripts, then prepare copy-ready or concise text and optionally export SRT subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video links or share text are sent to SocialDataX for processing, and service charges may apply.

Mitigation: Submit only content you are comfortable sharing with SocialDataX and check applicable service charges.

Risk: An API key is required for direct CLI use and could be exposed if stored insecurely.

Mitigation: Use supported secret storage and keep the key out of version control.

Risk: The external executable and hosted service are outside the bundled document's full verification.

Mitigation: Use a reviewed, fixed CLI version and assess the external service before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-short-video-copy-extract)
- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured transcription results summarized as Markdown; optional UTF-8 SRT subtitle file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video details, transcript, copy-ready text, and a concise summary; SRT export is optional.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
