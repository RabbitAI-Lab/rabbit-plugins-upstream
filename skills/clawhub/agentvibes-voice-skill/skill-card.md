## Description: <br>
Agentvibes Voice Skill provides multi-provider text-to-speech for AI agents with voice switching, preview, speed and effects controls, background music, replay, and language-learning playback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to add text-to-speech playback to agent workflows, content narration, voice customization, and language-learning scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local command execution for TTS providers and documented setup flows. <br>
Mitigation: Review the skill before installing and run it only in environments where local command execution for speech tooling is acceptable. <br>
Risk: First-use voice downloads or automatic component installation can introduce network and supply-chain exposure. <br>
Mitigation: Use trusted sources for voice assets and components, and approve downloads or installation steps before running them. <br>
Risk: Callback URLs and high-verbosity speech modes may disclose agent outputs or internal reasoning to unintended destinations or listeners. <br>
Mitigation: Avoid callback URLs unless the destination is trusted, and keep verbosity low or medium for sensitive workflows. <br>
Risk: Replay and local audio caching may retain generated speech after use. <br>
Mitigation: Clear cached audio when handling sensitive content and avoid replay features for confidential material. <br>


## Reference(s): <br>
- [Skill homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agentvibes-voice-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with slash commands, shell snippets, and structured JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger local TTS provider execution, first-use voice downloads, optional component installation, and local audio caching.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
