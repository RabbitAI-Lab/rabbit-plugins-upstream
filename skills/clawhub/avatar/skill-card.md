## Description: <br>
Interactive AI avatar with Simli video rendering and ElevenLabs TTS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johannes-berggren](https://clawhub.ai/user/johannes-berggren) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to run a local avatar interface that converts agent responses into spoken summaries, lip-synced Simli video, and markdown detail panels. It can optionally forward responses through Slack, email, or Stream Deck workflows when those integrations are configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is flagged for review because it exposes a provider key to the browser and gives the local avatar server broad messaging and business-tool authority. <br>
Mitigation: Use restricted Simli, ElevenLabs, OpenClaw, Slack, and email credentials; bind or firewall the server to trusted local access; disable forwarding integrations unless needed; rotate the Simli key if this version has already exposed it to browsers. <br>
Risk: Prompts and avatar responses may be processed by third-party voice, video, messaging, or email services when those features are enabled. <br>
Mitigation: Avoid sensitive prompts unless vendor processing is acceptable, and enable only the integrations required for the deployment. <br>


## Reference(s): <br>
- [ClawHub Avatar Skill Page](https://clawhub.ai/johannes-berggren/skills/avatar) <br>
- [Simli](https://simli.com) <br>
- [ElevenLabs](https://elevenlabs.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Tagged text with spoken plain text and detailed markdown sections, plus setup commands and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js, npm, SIMLI_API_KEY, and ELEVENLABS_API_KEY; optional Slack, email, OpenClaw gateway, and Stream Deck integrations may expand local server authority.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
