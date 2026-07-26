## Description: <br>
Generates realistic ElevenLabs text-to-speech audio with emotional audio tags, multilingual voice synthesis, and WhatsApp voice-message workflow guidance for OpenClaw agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaharsha](https://clawhub.ai/user/shaharsha) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and agents use this skill to turn text into expressive ElevenLabs voice audio, tune audio-tag prompts, convert audio for WhatsApp, and send voice messages after confirming content and recipient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text synthesized by the skill is sent to ElevenLabs, and generated audio may be sent through WhatsApp. <br>
Mitigation: Install only when that third-party processing is acceptable, and confirm both message content and recipient before sending. <br>
Risk: Audio conversion and cleanup use ffmpeg and temporary audio files. <br>
Mitigation: Use a trusted ffmpeg installation, select the latest generated file for the current task, and keep cleanup commands scoped to the temporary workspace copy. <br>


## Reference(s): <br>
- [Audio Tags Reference](references/audio-tags.md) <br>
- [ClawHub skill listing](https://clawhub.com/skills/elevenlabs-tts) <br>
- [ClawHub release page](https://clawhub.ai/shaharsha/skills/elevenlabs-tts) <br>
- [ElevenLabs](https://elevenlabs.io) <br>
- [ElevenLabs voice library](https://elevenlabs.io/voice-library) <br>
- [ElevenLabs v3-optimized voices](https://elevenlabs.io/app/voice-library/collections/aF6JALq9R6tXwCczjhKH) <br>
- [ElevenLabs voices API](https://api.elevenlabs.io/v1/voices) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline tool calls, JSON configuration, and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ELEVENLABS_API_KEY and ffmpeg; generated audio may be copied to the workspace for WhatsApp sending.] <br>

## Skill Version(s): <br>
2.4.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
