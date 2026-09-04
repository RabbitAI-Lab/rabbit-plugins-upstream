## Description:

Downloads TikTok videos without watermark and extracts MP3 audio by resolving supported TikTok URLs through the free TikTok Download API at tk.seekubo.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangsirme](https://clawhub.ai/user/wangsirme)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when given a public TikTok URL to retrieve video metadata and direct MP4 or MP3 download links, including no-watermark options when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok URLs are sent to tk.seekubo.com, a third-party downloader service.

Mitigation: Use only public, non-sensitive links and install the skill only when that data sharing is acceptable.

Risk: Downloaded media may be subject to platform terms or rights restrictions.

Mitigation: Use downloaded video or audio only when the user has the right to do so.

Risk: The service is rate limited and returned media links can expire.

Mitigation: Process one video at a time, retry after the documented wait period on rate limits, and download selected files promptly.

## Reference(s):

- [TikTok Download API homepage](https://tk.seekubo.com)
- [ClawHub skill page](https://clawhub.ai/wangsirme/skills/tiktok-downloader)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API calls, Guidance]

**Output Format:** [Markdown with curl commands and JSON response interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses curl to call a third-party downloader API; returned CDN and thumbnail links may expire.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
