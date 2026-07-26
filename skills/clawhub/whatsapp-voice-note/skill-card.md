## Description: <br>
Send WhatsApp voice notes from an OpenClaw agent by converting text to opus/ogg audio with ElevenLabs or macOS say and sending it through the WhatsApp channel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[georgecot99](https://clawhub.ai/user/georgecot99) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to let an OpenClaw agent reply by WhatsApp voice note, read text aloud to a chat, or generate an opus/ogg voice-note file for another channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can send voice notes to unintended WhatsApp recipients. <br>
Mitigation: Configure explicit allowed recipients and require confirmation before sending voice notes. <br>
Risk: Text sent to ElevenLabs may contain secrets or sensitive personal or business information. <br>
Mitigation: Do not use ElevenLabs for sensitive text; use the local say engine or --out-only and --dry-run flows for lower-risk testing. <br>
Risk: Generated audio may be sent before the user has reviewed the message content. <br>
Mitigation: Use --dry-run or --out-only for review workflows before enabling live WhatsApp sends. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/georgecot99/skills/whatsapp-voice-note) <br>
- [Build Your Own Chief starter kit](https://chief.natalicot.com/kit/?utm=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown usage guidance with bash commands; runtime output is an opus/ogg audio file or a WhatsApp voice-note send action.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ffmpeg and OpenClaw WhatsApp configuration; ElevenLabs is optional and uses ELEVENLABS_API_KEY when configured.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
