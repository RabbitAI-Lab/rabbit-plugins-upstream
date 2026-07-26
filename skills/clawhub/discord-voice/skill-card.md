## Description: <br>
Real-time voice conversations in Discord voice channels with Claude AI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avatarneil](https://clawhub.ai/user/avatarneil) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and server operators use this skill to let a Discord bot join voice channels, transcribe participant speech, route it through an OpenClaw or Clawdbot agent, and speak the agent response back into the channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shared Discord voice audio may be sent to cloud speech-to-text or text-to-speech providers. <br>
Mitigation: Notify and get consent from participants, prefer local STT/TTS for sensitive conversations, and configure only the providers needed for the deployment. <br>
Risk: With an empty allowedUsers list, anyone in a joined channel can interact with the bot and trigger agent activity. <br>
Mitigation: Set allowedUsers to explicit Discord user IDs before installing on shared servers. <br>
Risk: Voice-triggered requests can reach the underlying agent's normal tools. <br>
Mitigation: Require approval for sensitive or state-changing tools in the underlying OpenClaw agent. <br>
Risk: Auto-joining public channels can expose unintended participants to recording, transcription, or playback. <br>
Mitigation: Avoid autoJoin in public channels and join only channels where the operator has confirmed consent and access controls. <br>


## Reference(s): <br>
- [Discord Voice ClawHub page](https://clawhub.ai/avatarneil/skills/discord-voice) <br>
- [README](artifact/README.md) <br>
- [Security model](artifact/SECURITY.md) <br>
- [OpenClaw plugin metadata](artifact/openclaw.plugin.json) <br>
- [Clawdbot plugin metadata](artifact/clawdbot.plugin.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, audio, shell commands, configuration, guidance] <br>
**Output Format:** [Discord voice audio, agent text responses, JSON status/control results, and Markdown usage instructions with command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports Discord slash commands, CLI commands, gateway methods, and an agent tool for joining, leaving, speaking, status checks, provider selection, model selection, thinking level, and fallback reset.] <br>

## Skill Version(s): <br>
0.1.6 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
