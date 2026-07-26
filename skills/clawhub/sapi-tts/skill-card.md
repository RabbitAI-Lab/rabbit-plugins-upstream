## Description: <br>
Windows SAPI5 text-to-speech helper that generates local WAV audio with installed Windows 10/11 voices, including Neural voices when available, without GPU use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[korddie](https://clawhub.ai/user/korddie) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Windows users can use this skill to create a local PowerShell text-to-speech helper for generating WAV audio from text with installed SAPI5 voices. It is intended for Windows 10/11 environments where local speech synthesis and optional immediate playback are desired. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is Windows-specific and depends on local SAPI5 voices. <br>
Mitigation: Install it only on Windows 10/11 systems where SAPI voices are intended to be used, and list available voices before relying on a selected voice. <br>
Risk: The skill asks users to save and run a PowerShell script that writes WAV files to local paths. <br>
Mitigation: Review the PowerShell script before saving it and choose output paths you trust. <br>
Risk: Using the Play option can play generated audio aloud immediately. <br>
Mitigation: Use Play only in environments where immediate audio playback is appropriate. <br>
Risk: The optional NaturalVoiceSAPIAdapter is a separate third-party dependency. <br>
Mitigation: Review that dependency separately before installing or using it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/korddie/skills/sapi-tts) <br>
- [NaturalVoiceSAPIAdapter](https://github.com/gexgd0419/NaturalVoiceSAPIAdapter) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with PowerShell code blocks, parameter tables, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The provided script generates local WAV audio files and can optionally play the generated audio immediately.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
