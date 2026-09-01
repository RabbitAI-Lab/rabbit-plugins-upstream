## Description:

Download TikTok videos without watermark and extract MP3 audio via the free TikTok Download API (tk.seekubo.com). Give it any TikTok URL (www.tiktok.com, vm.tiktok.com, vt.tiktok.com, m.tiktok.com) and it resolves video metadata plus direct, browser-fetchable CDN download links. No API key or subscription required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangsirme](https://clawhub.ai/user/wangsirme)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have a public TikTok URL and want an agent to resolve metadata, choose an appropriate no-watermark MP4 or MP3 download option, and provide curl-based retrieval guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok URLs are sent to the third-party tk.seekubo.com service and resulting media may be downloaded from third-party CDN links.

Mitigation: Use the skill only for content the user owns, has permission to download, or is otherwise legally allowed to use; avoid submitting sensitive or private URLs.

Risk: Download, thumbnail, and CDN links can expire and may stop working after the current session.

Mitigation: Download selected files promptly and re-parse the TikTok URL when fresh links are needed.

Risk: The API is rate limited and private, deleted, restricted, or unsupported media cannot be downloaded.

Mitigation: Process one video at a time, handle the response body success field and documented error codes, and retry transient upstream errors only after a short wait.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangsirme/skills/tiktok-downloader)
- [TikTok Download API homepage](https://tk.seekubo.com)
- [TikTok Download API parse endpoint](https://tk.seekubo.com/api/v2/parse)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include third-party CDN download URLs, TikTok metadata, and short-lived thumbnail or media links.]

## Skill Version(s):

2.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
