## Description: <br>
This skill helps an agent synthesize short text into local Piper TTS MP3 voice messages using the default en_US-kusal-medium voice after local setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to create short spoken messages or brief English text readouts as local MP3 files. It is best suited to occasional voice-message delivery and short-form listening workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to run local setup, install, or voice-model download commands for Piper. <br>
Mitigation: Review generated commands before execution and run setup in an environment where local package installation and downloaded model files are acceptable. <br>
Risk: The artifact contains generic API_KEY setup text even though the security guidance says no generic API_KEY is needed for this skill. <br>
Mitigation: Do not set or share a generic API_KEY unless the agent platform independently requires it, and keep secrets out of version control. <br>
Risk: Generated speech may be poor or incorrect for long, non-English, or unsupported text because the free skill documents a single default English voice and no long-text segmentation. <br>
Mitigation: Use short English input, verify the MP3 before sending it to others, and use a more capable TTS workflow when multilingual voices, long text, or style control are required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/beware-piper-tts-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with bash snippets, MP3 file paths, and audio_as_voice message wrappers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one short text-to-speech request at a time; expected audio output is an MP3 path or a voice-message wrapper referencing that file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
