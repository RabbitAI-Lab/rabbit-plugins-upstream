## Description: <br>
Ace Music Free helps agents generate ACE Music text-to-music MP3 outputs from prompts, optional lyrics, instrumental mode, and duration settings through ACE Music's hosted API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and agent users can use this skill to request new music generation from text prompts, custom lyrics, or instrumental prompts and receive an MP3 file path. It is scoped to ACE Music text-to-music tasks and does not support cover, repaint, batch generation, seed reproduction, or precise BPM/key controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary marks the release suspicious because the documentation requests broad command and file authority and advertises unrelated media-processing capabilities. <br>
Mitigation: Use the skill only for ACE Music text-to-music tasks, avoid broad media-processing or command-execution tasks, and choose explicit output paths. <br>
Risk: API keys or sensitive prompt and lyric content could be exposed if supplied directly in chat or stored in generated files. <br>
Mitigation: Set ACE_MUSIC_API_KEY only as an environment variable, do not paste credentials into prompts, and avoid confidential lyrics or prompts. <br>
Risk: The skill text includes broader video, conversion, generic file-processing, and command-execution wording outside the text-to-music scope. <br>
Mitigation: Treat those broad claims as out of scope and review proposed commands before execution. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/ace-music-free) <br>
- [ACE Music API key page](https://acemusic.ai/playground/api-key) <br>
- [ACE Music API base endpoint](https://api.acemusic.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and generated MP3 file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ACE_MUSIC_API_KEY and explicit output paths for generated MP3 files.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
