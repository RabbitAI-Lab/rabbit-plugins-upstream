## Description: <br>
Find accommodation contact details and run AI-assisted booking calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arein](https://clawhub.ai/user/arein) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and travel operators can use this skill to find accommodation contact details from listing URLs and prepare or run AI-assisted booking calls through the concierge CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real outbound AI phone calls and may incur provider charges or contact unintended recipients. <br>
Mitigation: Use test numbers first, verify destination numbers before dialing, and set billing or quota limits with the configured providers. <br>
Risk: The call flow can expose a local service through ngrok. <br>
Mitigation: Use ngrok only when needed, avoid exposing the service directly, protect tunnel credentials, and use controlled hosting for production deployments. <br>
Risk: Calls can process phone numbers, audio, transcripts, API keys, and personal booking details through third-party services. <br>
Mitigation: Protect and rotate API keys, review generated logs, follow call recording and consent laws, and avoid sensitive healthcare, financial, or account-changing calls without strong human confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arein/skills/concierge) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Voice Call Setup Guide](artifact/CALL-SETUP.md) <br>
- [Twilio](https://www.twilio.com/try-twilio) <br>
- [Deepgram](https://console.deepgram.com/signup) <br>
- [ElevenLabs](https://elevenlabs.io/sign-up) <br>
- [Anthropic Console](https://console.anthropic.com) <br>
- [ngrok](https://ngrok.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; contact lookup can return JSON when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate real outbound phone calls through configured third-party services.] <br>

## Skill Version(s): <br>
1.5.0 (source: server-resolved release metadata; artifact frontmatter states 1.3.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
