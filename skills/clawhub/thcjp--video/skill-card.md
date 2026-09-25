## Description: <br>
Processes, edits, and optimizes videos for different platforms, including compression, transcoding, batch processing, and subtitle generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and automation teams use this skill to ask an agent for video compression, transcoding, editing, optimization, batch handling, and subtitle generation across common platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read and write video files and run FFmpeg-style commands. <br>
Mitigation: Use it only in an environment where media file access and command execution are acceptable, and review proposed commands before execution. <br>
Risk: The skill may process local paths or trusted URLs that contain copyrighted or sensitive media. <br>
Mitigation: Prefer trusted local files or trusted URLs, and process copyrighted or sensitive media only when intentional and authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/video) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON, Markdown, or text responses with file paths, media metadata, execution logs, and optional command or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include video or subtitle file outputs and FFmpeg-oriented processing guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
