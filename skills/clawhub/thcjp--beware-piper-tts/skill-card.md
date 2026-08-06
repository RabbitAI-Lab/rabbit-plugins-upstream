## Description: <br>
Beware Piper Tts helps agents guide local Piper text-to-speech workflows for generating WAV or MP3 audio from text, including voice selection, long-text splitting, batch generation, and basic speech-style controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and automation teams use this skill when they want an agent to prepare local Piper TTS commands and guidance for single-clip, long-form, multi-voice, or batch audio generation. It is best suited to local speech generation where users can review commands, destinations, and dependencies before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence marks the release suspicious because its automation scope is broad and its network, API, and delivery guidance is inconsistent. <br>
Mitigation: Install only for intended local Piper speech generation, review generated shell commands before execution, and avoid callback, Telegram, Discord, or API delivery paths unless the exact destination and command behavior are controlled. <br>
Risk: The skill can guide installation or execution of local TTS tools and write generated audio files. <br>
Mitigation: Run commands in a reviewed local environment, write outputs only to expected directories, and avoid processing sensitive text unless the local storage and sharing path are acceptable. <br>
Risk: The evidence warns that API-key and integration instructions are under-specified. <br>
Mitigation: Do not provide secrets or route sensitive text or audio through external integrations until the commands, credentials, and recipients have been independently reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/beware-piper-tts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated audio file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local WAV or MP3 file paths and voice-message wrapper text when the recommended commands are run.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
