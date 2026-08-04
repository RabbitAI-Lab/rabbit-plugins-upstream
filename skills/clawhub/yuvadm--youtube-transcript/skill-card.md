## Description: <br>
Fetch and save YouTube video transcripts as clean plain text. Use when the user provides a YouTube URL or wants to extract a transcript from a podcast, interview, or talk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuvadm](https://clawhub.ai/user/yuvadm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and content analysts use this skill to extract plain-text transcripts from YouTube podcasts, interviews, and talks for review or summarization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs yt-dlp against YouTube URLs, which performs network access based on the user-provided video URL. <br>
Mitigation: Use the skill only when the user expects YouTube transcript fetching and is comfortable with yt-dlp running against the supplied URL. <br>
Risk: When an output file is requested, an existing file at that path may be overwritten. <br>
Mitigation: Choose output paths carefully and avoid pointing the skill at files that should be preserved. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Files, Shell commands] <br>
**Output Format:** [Plain text transcript output, optionally saved to a user-selected file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.10+ and yt-dlp; default subtitle language is English unless the user selects another language.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
