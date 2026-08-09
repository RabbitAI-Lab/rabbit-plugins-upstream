## Description: <br>
Ace Music helps an agent generate AI music through ACE Music's hosted ACE-Step 1.5 API, including prompts, lyrics, instrumental tracks, duration, tempo, key, language, batch size, and seed options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn music prompts, lyrics, and generation parameters into AI-generated audio files through ACE Music. It is suited for workflows that need quick music drafts, instrumental tracks, multilingual vocals, covers, or audio repainting through an external hosted API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, lyrics, and generation parameters are sent to the external ACE Music API. <br>
Mitigation: Use the skill only for content that is appropriate to share with ACE Music and avoid broad request-content logging. <br>
Risk: An ACE Music API key is required for generation. <br>
Mitigation: Keep the key in a private environment variable and do not place it in shared project files. <br>
Risk: The skill may propose shell commands and create local audio files. <br>
Mitigation: Review generated commands before running them and inspect output paths before sharing generated files. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/ace-music) <br>
- [ACE Music API key page](https://acemusic.ai/playground/api-key) <br>
- [ACE Music API base URL](https://api.acemusic.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, code examples, and generated audio file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the ACE Music API and create local MP3 audio files.] <br>

## Skill Version(s): <br>
1.0.3 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
