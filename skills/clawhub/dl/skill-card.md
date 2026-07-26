## Description: <br>
Downloads video or music from media URLs such as YouTube, Bilibili, and X into local media folders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guoqiao](https://clawhub.ai/user/guoqiao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent download media from a provided URL into local Music, Movies, Videos, or user-selected folders. It can also support local media-server workflows and Telegram audio delivery when those environments are configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads media from network URLs and saves persistent files locally, which can consume disk space, especially for videos or playlists. <br>
Mitigation: Use it only for intended media URLs, choose an appropriate output directory, and monitor local storage before downloading large media or playlists. <br>
Risk: Configured cookie files can contain account-session secrets. <br>
Mitigation: Store cookie files securely, limit access to trusted users and agents, and remove or rotate them when they are no longer needed. <br>
Risk: Media-server sharing can make downloaded files visible on the local network. <br>
Mitigation: Enable media-server sharing only when local-network access is intended and restrict shared folders to the media directories you want exposed. <br>
Risk: Telegram delivery can send downloaded audio files outside the local machine when used in a Telegram session. <br>
Mitigation: Confirm the session context and recipient before sending downloaded audio files through Telegram. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/guoqiao/skills/dl) <br>
- [ClawHub Metadata Homepage](https://clawhub.ai/guoqiao/dl) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and local file or folder paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and uses yt-dlp to produce downloaded media files or playlist folders; the script prints the saved path after completion.] <br>

## Skill Version(s): <br>
0.2.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
