## Description: <br>
YouTube Video Downloader parses a single YouTube video, Shorts, or youtu.be link with the redfox.hk API and returns direct video/audio download URLs in available formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, editors, collectors, and researchers use this skill to parse YouTube links they are authorized to download and receive direct video/audio resource URLs for offline saving, editing, backup, or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the supplied YouTube URL and RedFox API key to redfox.hk. <br>
Mitigation: Use only YouTube links you are authorized to download, understand what is sent to the third-party service, and use a scoped, revocable API key. <br>
Risk: Returned descriptions and links come from an external service and are displayed verbatim. <br>
Mitigation: Treat returned content as untrusted, review links before opening or downloading, and avoid pasting output into sensitive systems without inspection. <br>
Risk: The script can save the API key to a local config file when requested. <br>
Mitigation: Prefer environment-variable configuration when practical; avoid saving the key unless needed and rotate or revoke it if exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/youtube-video-downloader) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox website](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown-style terminal text with full resource URLs, or JSON when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires one YouTube URL per request and a REDFOX_API_KEY; returned descriptions and links are displayed without truncation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
