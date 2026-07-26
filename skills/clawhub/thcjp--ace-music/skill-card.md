## Description: <br>
Ace Music helps agents use the ACE Music API to generate vocal or instrumental MP3 music from prompts, lyrics, and optional source audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use Ace Music to generate complete songs, instrumentals, covers, repainted audio segments, and batch variants through the ACE Music API with controls for duration, BPM, key, language, lyrics, and seed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, lyrics, and optional source audio are sent to ACE Music's API. <br>
Mitigation: Do not submit private, proprietary, or copyrighted material unless the user has the right to process it with ACE Music. <br>
Risk: ACE_MUSIC_API_KEY can grant access to the user's ACE Music account. <br>
Mitigation: Keep the API key out of logs, chat transcripts, generated files, and version control. <br>
Risk: Generated music may not be suitable for every commercial distribution or copyright workflow. <br>
Mitigation: Confirm usage rights, distribution rights, and any licensing requirements before publishing generated or transformed audio. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/ace-music) <br>
- [Skill Homepage](https://skillhub.cn) <br>
- [ACE Music API Key Page](https://acemusic.ai/playground/api-key) <br>
- [ACE Music API Generate Endpoint](https://api.acemusic.ai/v1/generate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated MP3 file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ACE_MUSIC_API_KEY; generated audio is returned by the API as base64 MP3 and decoded to local MP3 files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
