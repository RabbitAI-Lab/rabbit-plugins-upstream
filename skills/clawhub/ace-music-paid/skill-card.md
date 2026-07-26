## Description: <br>
Ace Music Paid guides agents through ACE Music Pro API workflows for batch music generation, cover and repaint tasks, audio-input generation, and outputs up to 300 seconds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and professional music production teams use this skill to configure ACE Music Pro API access and generate commercial music assets through command-line workflows. It is oriented toward advertising, film, game, label demo, and brand audio production tasks that need batch generation or longer-form output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses command execution for ACE Music API workflows and file-handling examples. <br>
Mitigation: Review generated commands and output paths before execution, especially before moving or archiving files. <br>
Risk: The workflow requires an ACE Music API key. <br>
Mitigation: Store ACE_MUSIC_API_KEY in environment variables or a secrets manager and avoid writing credentials into scripts or shared files. <br>


## Reference(s): <br>
- [ClawHub release page for Ace Music Paid](https://clawhub.ai/thcjp/skills/ace-music-paid) <br>
- [ACE Music API endpoint](https://api.acemusic.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ACE_MUSIC_API_KEY and API-driven command execution; generated audio is represented through output file paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
