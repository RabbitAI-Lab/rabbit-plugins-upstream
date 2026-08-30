## Description:

Download TikTok videos without watermark and extract MP3 audio via the TikTok Video Downloader API on RapidAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangsirme](https://clawhub.ai/user/wangsirme)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn public TikTok URLs into metadata, no-watermark MP4 links, watermarked MP4 links, or MP3 audio links through a RapidAPI-backed downloader. It is useful when a user has permission to save the content and needs direct download commands or guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok URLs are sent to a third-party RapidAPI service.

Mitigation: Use the skill only when that service relationship is acceptable for the content being processed.

Risk: The RAPIDAPI_KEY can expose account access, quota, or billing if logged or shared.

Mitigation: Keep the key private and avoid echoing, logging, embedding, or committing it.

Risk: Downloads may exceed subscription quota or paid-plan limits.

Mitigation: Monitor RapidAPI usage and billing, and handle rate-limit responses before retrying.

Risk: Saving TikTok media without permission may violate rights or platform terms.

Mitigation: Download only content the user has rights or permission to save.

## Reference(s):

- [TikTok Video Download No Watermark API on RapidAPI](https://rapidapi.com/fwelljson/api/tiktok-video-download-no-watermark2)
- [ClawHub skill page](https://clawhub.ai/wangsirme/skills/tiktok-downloader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and a private RAPIDAPI_KEY; generated download links may expire and should be fetched promptly.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
