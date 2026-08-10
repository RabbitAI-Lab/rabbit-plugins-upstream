## Description:

Resolves a TikTok video URL into available no-watermark and watermarked download URLs, playback URLs, and cover image URLs for saving or offline analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to resolve a specific TikTok video URL into media links, playback links, and thumbnails. It is intended for cases where the user already has a TikTok video link and needs structured download or preview data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok URLs and a LinkFox API key to LinkFox services.

Mitigation: Install only when this data sharing is acceptable, and prefer self-service API-key setup through the LinkFox account portal.

Risk: The skill may store full API responses and cache files locally under linkfox session directories.

Mitigation: Review generated output paths after use and delete saved response or cache files when they are no longer needed.

Risk: The onboarding flow can involve account signup, SMS verification codes, package selection, and payment actions.

Mitigation: Do not share SMS codes unless intentionally creating or accessing a LinkFox account, and review every payment action before confirming it.

## Reference(s):

- [EchoTik TikTok video download API reference](artifact/references/api.md)
- [LinkFox authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-get-video-download-url)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses, saved JSON files, and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TikTok video URL and a LinkFox API key; full responses may be persisted under a local linkfox session directory, and responses may be summarized when large.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
