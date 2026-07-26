## Description: <br>
Send high-quality text-to-speech voice messages on WhatsApp in 40+ languages with automatic delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hopyky](https://clawhub.ai/user/hopyky) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
External users and developers use this skill to generate Piper text-to-speech audio and send it as WhatsApp voice messages to individual recipients or groups through a configured Clawdbot account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send real WhatsApp voice messages from the connected Clawdbot account. <br>
Mitigation: Install only for trusted WhatsApp accounts, test first with --no-send, and verify recipient phone numbers or group IDs before sending. <br>
Risk: A configured default recipient can cause messages to be sent without an explicit target. <br>
Mitigation: Set WHATSAPP_DEFAULT_TARGET only when intentional and review the Clawdbot skill configuration before routine use. <br>
Risk: Generated audio files may be deleted automatically after successful delivery or during cleanup. <br>
Mitigation: Use --no-send or preserve outputs separately when audio files need to be reviewed or retained. <br>


## Reference(s): <br>
- [TTS WhatsApp on ClawHub](https://clawhub.ai/hopyky/skills/tts-whatsapp) <br>
- [Piper Voice Samples](https://rhasspy.github.io/piper-samples/) <br>
- [Piper Voices on Hugging Face](https://huggingface.co/rhasspy/piper-voices) <br>
- [Clawdbot Documentation](https://docs.clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Audio files, WhatsApp messages, Guidance] <br>
**Output Format:** [Command-line output, OGG/Opus voice messages, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can generate audio without sending via --no-send; successful sends may delete generated files automatically.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, SKILL.md frontmatter, changelog released 2026-01-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
