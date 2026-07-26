## Description: <br>
LYGO SMART DISK AGENT provides a localhost browser portal for a local Ollama-backed assistant with a local operator token, P0-P5 controls, and no HTTP chat-memory export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and local AI operators use this skill to install and run an offline-first smart disk assistant that serves a local portal, talks to host Ollama, and exposes status, help, chat, and controlled limb actions through token-protected loopback APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a localhost AI portal that opens a browser and communicates with local Ollama. <br>
Mitigation: Keep auth.required enabled, keep the default localhost bind, avoid LAN binding unless intentionally configured, and run the included self-check before use. <br>
Risk: The local operator token is a bearer secret for protected local API actions. <br>
Mitigation: Treat data/.sda_local_token and printed boot tokens as local secrets and avoid sharing console output or browser URLs that include the token. <br>
Risk: Some older design documentation describes an earlier no-auth model. <br>
Mitigation: Use the v1.1.0 security evidence and current SECURITY.md behavior as authoritative: token auth is enabled by default and HTTP memory export is blocked. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-smart-disk-agent) <br>
- [Publisher profile](https://clawhub.ai/user/deepseekoracle) <br>
- [Project repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Skill source tree](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/lygo_smart_disk) <br>
- [Security notes](references/SECURITY.md) <br>
- [SkillSpector audit](references/SKILLSPECTOR_AUDIT.md) <br>
- [Quick start](references/QUICK.md) <br>
- [Public README](public/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text responses from a local browser portal and command-line workflow] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local Ollama for chat; uses a localhost portal on port 9631 with a local operator token by default.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence release.version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
