## Description: <br>
Download YouTube videos, playlists, audio, thumbnails, metadata, and subtitles with yt-dlp. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawbus](https://clawhub.ai/user/clawbus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to download YouTube videos, playlists, audio, subtitles, thumbnails, and metadata with yt-dlp while selecting formats, output locations, and cookie-based access options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper can install or update yt-dlp in the user's Python environment. <br>
Mitigation: Review before installing, prefer a trusted preinstalled yt-dlp version, and use --skip-update when automatic updates are not desired. <br>
Risk: Cookie options can pass authenticated browser session cookies to yt-dlp. <br>
Mitigation: Enable --cookies or --cookies-from-browser only after explicit approval for the specific video or playlist. <br>
Risk: Downloaded media may be subject to copyright or platform access restrictions. <br>
Mitigation: Download only content the user has rights or permission to access and retain. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/clawbus/skills/clawbus-youtube-download) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and local file output from yt-dlp] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces downloaded media and metadata files in a local output directory when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
