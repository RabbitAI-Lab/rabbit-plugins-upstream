## Description: <br>
Downloads videos from YouTube, Bilibili, Twitter/X, TikTok, and other yt-dlp-supported sites, with options for audio extraction, subtitles, playlists, and quality selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apollo1234](https://clawhub.ai/user/apollo1234) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent construct yt-dlp shell commands for downloading media from provided URLs, including MP3 extraction, subtitles, playlists, and format selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill encourages browser-cookie use, which can expose a logged-in browser session to yt-dlp activity. <br>
Mitigation: Require explicit user consent before using browser cookies, prefer downloads without cookies first, and use a dedicated browser profile or limited-scope exported cookie file when cookies are needed. <br>
Risk: The skill can run networked shell commands and create downloaded files locally. <br>
Mitigation: Review the generated command, destination path, and requested media source before execution, and scan or inspect downloaded files before opening or redistributing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apollo1234/skills/yt-dlp-downloader-skill) <br>
- [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and brief status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create local downloaded media files when executed.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
