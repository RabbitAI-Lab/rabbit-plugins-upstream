## Description: <br>
Search YouTube for videos on any topic and get intelligent summaries from video subtitles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dillera](https://clawhub.ai/user/dillera) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to search YouTube, let a user select a video, extract English subtitles, and produce a concise summary with key topics, timestamps, and notable quotes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts YouTube and may rely on yt-dlp or web scraping to search videos and retrieve subtitles. <br>
Mitigation: Use it only where contacting YouTube is acceptable, and review the selected video URL before running subtitle extraction. <br>
Risk: Subtitle extraction creates local subtitle files in the directory where yt-dlp runs. <br>
Mitigation: Run the workflow from a normal non-privileged working folder and remove generated subtitle files when they are no longer needed. <br>
Risk: The workflow depends on third-party packages such as yt-dlp, requests, and bs4. <br>
Mitigation: Review and install third-party dependencies through trusted package sources before using the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dillera/skills/tube-summary) <br>
- [Publisher profile](https://clawhub.ai/user/dillera) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with command examples and structured summary text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected YouTube video metadata, subtitle-derived key topics, a concise summary, timestamps, and short quotes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
