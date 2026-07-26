## Description: <br>
Generate Pinterest-optimized vertical videos using JSON2Video API with AI-generated or URL-based images, AI-generated or provided voiceovers, optional subtitles, and zoom effects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benhuebner01](https://clawhub.ai/user/benhuebner01) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External creators, marketers, and developers use this skill to configure and run JSON2Video renders for vertical social media videos with images, narration, subtitles, and scene effects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video prompts, narration text, overlays, image URLs, audio URLs, and related metadata are sent to the third-party JSON2Video API. <br>
Mitigation: Use only content approved for third-party processing and avoid confidential assets, personal data, private internal URLs, and sensitive business material in video configs. <br>
Risk: The CLI can print part of the render payload or render status to stdout. <br>
Mitigation: Keep secrets out of configs and review terminal output or logs before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/benhuebner01/skills/claw-video-generator) <br>
- [Advanced usage guide](ADVANCED.md) <br>
- [JSON2Video API key setup](https://json2video.com/get-api-key/) <br>
- [Microsoft Azure Speech voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts) <br>
- [ElevenLabs Voice Library](https://elevenlabs.io/app/voice-library) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, Python code, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces JSON2Video project payloads and may print render status or video URLs when commands are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
