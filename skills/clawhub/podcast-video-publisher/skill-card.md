## Description: <br>
Render podcast episodes as 1080p art-slideshow MP4s and publish them to a YouTube Podcasts playlist: covers/thumbnails generated from your art, resumable batch upload, playlist ordering, retiring old versions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickflach](https://clawhub.ai/user/nickflach) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, producers, and channel operators use this skill to render podcast audio and artwork into episode videos, then upload, thumbnail, order, retire, and verify those episodes in a YouTube Podcasts playlist. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad persistent YouTube write access and can make public channel and playlist changes. <br>
Mitigation: Review and edit the playlist ID and episode ordering before execution, run phases one at a time on a test or private playlist first, and revoke the Google OAuth grant immediately if the token file is exposed. <br>
Risk: OAuth credentials and upload state are written to local project files. <br>
Mitigation: Keep .youtube.json and upload-state.json out of version control and confirm they are ignored before using the publishing scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nickflach/skills/podcast-video-publisher) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands and bundled Python and Node.js scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled scripts can produce local MP4 renders, cover image files, upload state, and YouTube API changes when run with user-provided credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
