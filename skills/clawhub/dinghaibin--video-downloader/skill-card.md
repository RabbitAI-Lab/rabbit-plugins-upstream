## Description: <br>
Download videos from YouTube and other video platforms. Use when user needs to download videos for offline viewing, extract audio from videos, or save video metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dinghaibin](https://clawhub.ai/user/dinghaibin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users can use this skill to download videos for offline access, extract audio, choose quality or format options, and inspect basic video metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change the local Python environment by installing yt-dlp automatically. <br>
Mitigation: Install dependencies yourself in a virtual environment or isolated workspace before running the downloader. <br>
Risk: Downloading video content involves local command execution and network activity. <br>
Mitigation: Review the command and target URL before execution, and run it only when the network activity and resulting files are expected. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files] <br>
**Output Format:** [Command-line output and downloaded media files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local video or audio files and print metadata or format listings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
