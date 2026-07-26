## Description: <br>
Local 24x7 OpenAI-compatible API server for STT/TTS, powered by MLX on your Mac. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guoqiao](https://clawhub.ai/user/guoqiao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to install and run a local macOS audio API server for speech-to-text and text-to-speech workflows. It is intended for Apple Silicon Macs using Homebrew and MLX-backed audio models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install flow starts a persistent local audio API server as a Homebrew service. <br>
Mitigation: Keep the service bound to localhost or protected by firewall rules, and stop the Homebrew service when it is no longer needed. <br>
Risk: The install flow depends on a third-party Homebrew tap. <br>
Mitigation: Review or trust the guoqiao Homebrew tap before installing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/guoqiao/skills/mlx-audio-server) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/guoqiao) <br>
- [Clawdis Homepage](https://github.com/guoqiao/skills/blob/main/mlx-audio-server/mlx-audio-server/SKILL.md) <br>
- [mlx-audio](https://github.com/Blaizzy/mlx-audio) <br>
- [mlx-audio-server Homebrew Formula](https://github.com/guoqiao/homebrew-tap/blob/main/Formula/mlx-audio-server.rb) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; helper scripts return transcript text or an audio file path.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local macOS workflow; requires Homebrew, Apple Silicon, and a running localhost audio API server.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
