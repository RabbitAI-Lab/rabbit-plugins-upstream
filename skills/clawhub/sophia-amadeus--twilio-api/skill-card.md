## Description: <br>
Twilio API integration with managed OAuth for SMS, voice calls, phone numbers, and other Twilio resources through Maton. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sophia-amadeus](https://clawhub.ai/user/sophia-amadeus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to connect to Twilio through Maton, inspect Twilio account resources, and prepare or execute SMS, voice, phone-number, application, queue, address, and usage-record API operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide access to or changes in broader Twilio account resources through Maton beyond the headline SMS, calls, phone numbers, and conversations scope. <br>
Mitigation: Use it only with a Twilio account and Maton connection where those broader operations are acceptable, and require explicit confirmation before any write action. <br>
Risk: The skill requires MATON_API_KEY for network API access. <br>
Mitigation: Provide MATON_API_KEY through a managed environment or secret store and avoid exposing it in prompts, logs, or shared artifacts. <br>


## Reference(s): <br>
- [ClawHub Twilio Api Skill Page](https://clawhub.ai/sophia-amadeus/skills/twilio-api) <br>
- [Twilio API Overview](https://www.twilio.com/docs/usage/api) <br>
- [Twilio Messages API](https://www.twilio.com/docs/messaging/api/message-resource) <br>
- [Twilio Calls API](https://www.twilio.com/docs/voice/api/call-resource) <br>
- [Twilio Phone Numbers API](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) <br>
- [Twilio Applications API](https://www.twilio.com/docs/usage/api/applications) <br>
- [Twilio Usage Records API](https://www.twilio.com/docs/usage/api/usage-record) <br>
- [Maton Account Settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands, Python and JavaScript snippets, and HTTP endpoint examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY, network access, and an authorized Twilio connection.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
