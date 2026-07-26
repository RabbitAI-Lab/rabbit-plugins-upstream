## Description: <br>
Generates a three-minute first-person book video from a book title and author, combining book research, script and storyboard generation, flat cartoon illustrations, TTS narration, animated subtitles, music, transitions, and MP4 composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenjun198711](https://clawhub.ai/user/chenjun198711) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators and developers use this skill to turn a book name and author into a short narrated video with generated visuals, subtitles, background music, and a final MP4 suitable for book-focused content workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may use external search, image generation, TTS services, dependency or model downloads, and local video output. <br>
Mitigation: Install only in environments where those services and downloads are acceptable, review referenced scripts and assets before running them, and inspect generated media before publishing. <br>
Risk: TTS configuration may involve service credentials. <br>
Mitigation: Prefer environment variables or protected local configuration for API keys, and do not store credentials in a shared skill directory. <br>


## Reference(s): <br>
- [Server-resolved GitHub repository](https://github.com/chenjun198711/if-book-could-speak-video-generator) <br>
- [ClawHub skill listing](https://clawhub.ai/chenjun198711/skills/if-book-could-speak-video-generator) <br>
- [Agent Skills open standard](https://agentskills.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents through generating scripts, storyboards, image and audio assets, subtitle timing, and final MP4 video output.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
