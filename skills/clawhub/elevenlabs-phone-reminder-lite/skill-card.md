## Description: <br>
Build AI phone call reminders with ElevenLabs Conversational AI + Twilio. Free starter guide. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and builders use this skill to set up outbound AI phone reminder calls with ElevenLabs Conversational AI and Twilio. It provides a starter guide for credentials, phone number setup, agent creation, Twilio connection, and test calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outbound reminder calls may require recipient consent and clear AI caller identification. <br>
Mitigation: Use the skill only for recipients who have agreed to receive calls, and identify AI callers where required. <br>
Risk: Reminder call content can expose sensitive personal data. <br>
Mitigation: Avoid sensitive personal data in prompts, reminders, and call content. <br>
Risk: ElevenLabs and Twilio credentials can be exposed if copied into code or shared logs. <br>
Mitigation: Store API keys and tokens in environment variables or a secret manager, and rotate them periodically. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daaab/skills/elevenlabs-phone-reminder-lite) <br>
- [ElevenLabs signup](https://try.elevenlabs.io/clawhub) <br>
- [Twilio](https://twilio.com) <br>
- [ElevenLabs create Conversational AI agent endpoint](https://api.elevenlabs.io/v1/convai/agents/create) <br>
- [ElevenLabs connect Twilio phone number endpoint](https://api.elevenlabs.io/v1/convai/phone-numbers/create) <br>
- [ElevenLabs outbound Twilio call endpoint](https://api.elevenlabs.io/v1/convai/twilio/outbound-call) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup steps, credential placeholders, cost notes, and lite-version limitations.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
