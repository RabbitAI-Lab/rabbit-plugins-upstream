## Description:

Resolves a TikTok video URL into available no-watermark download, watermarked download, playback, and cover image URLs for saving or offline analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and agents use this skill to resolve a specific TikTok video link into returned media URLs and cover images when those fields are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok URLs are sent to LinkFox and full API responses are stored locally.

Mitigation: Use only links appropriate to share with LinkFox, review generated files under the local linkfox directory, and remove stored responses when they are no longer needed.

Risk: Authentication, API-key generation, credit, and payment flows may expose account or billing information if handled carelessly.

Mitigation: Prefer self-service API-key setup, do not share phone numbers or API keys in transcripts, and verify payment actions before displaying or scanning any QR code.

Risk: Returned download and playback URLs may be unavailable for some videos or expire after resolution.

Mitigation: Check returned fields before presenting links, fall back to playback links when direct downloads are absent, and re-resolve expired URLs.

## Reference(s):

- [EchoTik TikTok Video Download API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-get-video-download-url)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and locally saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TikTok video URL and a LinkFox API key; full responses are persisted under a local linkfox session directory, with large responses summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
