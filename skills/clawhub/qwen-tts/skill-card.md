## Description: <br>
Generates WAV text-to-speech audio with Qwen3-TTS custom voices, speaker selection, language selection, and instruction-based voice style control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paki81](https://clawhub.ai/user/paki81) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agent builders use this skill to generate spoken audio files from text for OpenClaw workflows, voice messages, narration, and local or remote TTS automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's offline framing does not fully match its remote HTTP modes and unauthenticated network server behavior. <br>
Mitigation: Keep QWEN_TTS_REMOTE unset for private local use, avoid sending sensitive text to remote servers, and verify the active runtime mode before processing private content. <br>
Risk: Exposing the TTS server can make submitted text and generated audio available over the network. <br>
Mitigation: Bind the server to localhost or a tightly controlled private network, and add authentication, TLS, or firewall restrictions before exposing it. <br>


## Reference(s): <br>
- [Qwen3-TTS-12Hz-1.7B-CustomVoice model card](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) <br>
- [Qwen3-tts ClawHub page](https://clawhub.ai/paki81/skills/qwen-tts) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands, Configuration] <br>
**Output Format:** [WAV audio files with stdout file paths; optional HTTP WAV responses when remote mode is configured] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs uncompressed WAV audio, supports local generation and remote server mode, and uses speaker, language, model, and instruction parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
