## Description: <br>
Video Editor renders JSON project templates into videos with layered visuals, effects, subtitles, and narration/background/SFX audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fackee](https://clawhub.ai/user/fackee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content automation teams use this skill to define video projects as JSON and render local media assets into finished MP4 videos with compositing, transitions, subtitles, and mixed audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted project files or media assets could cause unsafe or unexpected local rendering behavior. <br>
Mitigation: Use the skill only with project files and assets from trusted sources. <br>
Risk: Rendering to an existing output path can overwrite an important video file. <br>
Mitigation: Choose a fresh output filename or back up important files before rendering. <br>
Risk: Secrets stored near the skill could be exposed through local project handling. <br>
Mitigation: Avoid placing sensitive secrets in a .env file next to the skill. <br>


## Reference(s): <br>
- [JSON Project Template Complete Field Reference](references/template-schema.md) <br>
- [FFmpeg Filter Parameters Quick Reference](references/ffmpeg-filters.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/fackee/skills/video-editor) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update JSON project templates and invoke local Python/FFmpeg rendering commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
