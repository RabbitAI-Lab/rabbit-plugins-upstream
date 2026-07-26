## Description: <br>
Ace Music Free helps agents generate MP3 music from text prompts, optional lyrics, and instrumental settings through the ACE Music API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators and developers use this skill to ask an agent for quick text-to-music prototypes, lyric-based vocal tracks, or instrumental MP3 files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an ACE Music API key for requests. <br>
Mitigation: Provide the key only through the ACE_MUSIC_API_KEY environment variable and avoid pasting or storing it in chat or version control. <br>
Risk: Generated MP3 output is written to the local filesystem. <br>
Mitigation: Use explicit output filenames in a working directory you control and check before overwriting existing files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ace-music-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>
- [ACE Music API key setup](https://acemusic.ai/playground/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands and generated MP3 file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ACE_MUSIC_API_KEY and writes generated MP3 files locally.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
