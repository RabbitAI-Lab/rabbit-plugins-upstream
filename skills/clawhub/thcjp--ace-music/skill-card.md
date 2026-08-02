## Description: <br>
ACE Music helps agents generate AI music from prompts and lyrics through ACE Music's hosted ACE-Step 1.5 API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, creators, and automation teams use this skill to ask an agent for generated music, vocals, lyrics-driven songs, instrumentals, covers, or repainted audio. The source states it is not suitable for processing copyright-protected media content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Music prompts, lyrics, or proprietary creative material may be sent to ACE Music's API. <br>
Mitigation: Use the skill only for content appropriate to share with that external API, and avoid enabling full request-body logs for private lyrics or proprietary work. <br>
Risk: The ACE Music API key could be exposed if stored in shared instructions or logs. <br>
Mitigation: Store ACE_MUSIC_API_KEY in a private environment variable or secrets manager rather than TOOLS.md. <br>
Risk: The artifact states it is not suitable for copyright-protected media content. <br>
Mitigation: Use only prompts, lyrics, and audio inputs that the user has rights to provide and transform. <br>


## Reference(s): <br>
- [ACE Music API Key Page](https://acemusic.ai/playground/api-key) <br>
- [ACE Music API Base URL](https://api.acemusic.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands, API request examples, and generated MP3 file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May send user prompts, lyrics, and music-generation parameters to ACE Music's external API; generated audio is described as base64 MP3 decoded to files.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
