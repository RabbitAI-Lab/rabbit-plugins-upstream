## Description: <br>
Download online videos with quality and format controls using yt-dlp for reliable local saves. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and end users use this skill to download single videos or extract audio from user-provided video URLs with explicit quality, format, and output-location controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the requested media URL and standard downloader headers to the relevant video host through yt-dlp. <br>
Mitigation: Use only trusted URLs and videos the user has rights to download; inspect metadata before downloading. <br>
Risk: Downloaded files and optional preference or history notes may remain on the local machine. <br>
Mitigation: Choose the output folder deliberately and delete or decline ~/video-downloader/ memory and log files when local retention is not desired. <br>
Risk: The wrapper runs local shell commands and writes files based on user-selected download settings. <br>
Mitigation: Review the generated command, output directory, and format before execution, and verify the resulting file exists and is non-empty. <br>


## Reference(s): <br>
- [Video Downloader on ClawHub](https://clawhub.ai/ivangdavila/video-downloader) <br>
- [Video Downloader homepage](https://clawic.com/skills/video-downloader) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and local file guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke yt-dlp locally, write downloaded media to a user-approved folder, and optionally maintain local preference or download-history notes under ~/video-downloader/.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
