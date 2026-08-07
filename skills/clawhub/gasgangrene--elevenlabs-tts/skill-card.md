## Description: <br>
Generates expressive ElevenLabs text-to-speech guidance for OpenClaw, including emotional audio tags, multilingual voice synthesis, and WhatsApp voice-message workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure ElevenLabs text-to-speech, write expressive audio-tagged prompts, and prepare generated voice audio for WhatsApp delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated voice content or WhatsApp messages could be sent with the wrong text, recipient, or attachment. <br>
Mitigation: Review the generated text content, target phone number, and audio file path before sending messages. <br>
Risk: The ElevenLabs API key is required and could be misconfigured or exposed during setup. <br>
Mitigation: Store ELEVENLABS_API_KEY in the configured environment or OpenClaw configuration and review the configured key before use. <br>
Risk: Temporary audio files may contain generated speech that should not persist longer than needed. <br>
Mitigation: Use the documented workspace copy path deliberately and remove temporary audio files after sending. <br>


## Reference(s): <br>
- [Audio Tags Reference](references/audio-tags.md) <br>
- [ClawHub source listing](https://clawhub.com/skills/elevenlabs-tts) <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/elevenlabs-tts) <br>
- [ElevenLabs](https://elevenlabs.io) <br>
- [ElevenLabs Voice Library](https://elevenlabs.io/voice-library) <br>
- [ElevenLabs v3-optimized voices](https://elevenlabs.io/app/voice-library/collections/aF6JALq9R6tXwCczjhKH) <br>
- [ElevenLabs Voices API](https://api.elevenlabs.io/v1/voices) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands, Text] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, text prompt examples, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ELEVENLABS_API_KEY; ffmpeg is needed for workflows that convert audio for WhatsApp compatibility.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
