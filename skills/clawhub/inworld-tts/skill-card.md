## Description: <br>
Text-to-speech via Inworld.ai API. Use when generating voice audio from text, creating spoken responses, or converting text to MP3/audio files. Supports multiple voices, speaking rates, and streaming for long text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gugic](https://clawhub.ai/user/gugic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to generate spoken audio from text through the Inworld.ai TTS API, including configurable voice, speaking rate, temperature, model, and streaming behavior for long text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text converted to speech is sent to Inworld.ai using the configured API key. <br>
Mitigation: Do not pass secrets, private customer data, or regulated content unless policy allows sending that data to Inworld.ai. <br>
Risk: The INWORLD_API_KEY credential is required for API access. <br>
Mitigation: Store the API key carefully in the environment or an approved secret store, and do not commit or share it. <br>
Risk: The optional global symlink makes the TTS script callable from anywhere on the system. <br>
Mitigation: Skip the symlink unless global command-line access is needed, and review the target path before creating it. <br>


## Reference(s): <br>
- [Inworld Platform](https://platform.inworld.ai) <br>
- [Inworld API Examples](https://github.com/inworld-ai/inworld-api-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and generated MP3 audio files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses INWORLD_API_KEY for Inworld.ai API calls and writes the decoded audio response to a requested MP3 path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
