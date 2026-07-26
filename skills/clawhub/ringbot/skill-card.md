## Description: <br>
RingBot helps agents make outbound AI phone calls for tasks such as calling businesses, ordering food by phone, making reservations, and scheduling appointments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gbessoni](https://clawhub.ai/user/gbessoni) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, employees, and developers use RingBot to initiate outbound AI voice calls for reservations, appointment scheduling, customer-service calls, reminders, lead qualification, and similar phone-based tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate real outbound AI phone calls, including scheduled or repeated calls, without evidence of built-in consent or confirmation safeguards. <br>
Mitigation: Require explicit user approval for each call or schedule, verify the recipient and purpose before dialing, and avoid sensitive or regulated outreach unless consent and legal authority are clear. <br>
Risk: Outbound calls can create Twilio or hosted-service charges. <br>
Mitigation: Set spend limits and rate limits, monitor call usage, and restrict who can trigger calls in shared or automated environments. <br>
Risk: DIY setup requires Twilio, LiveKit, and Groq credentials. <br>
Mitigation: Store provider keys only in approved secret stores, limit their permissions where possible, and rotate credentials if they are exposed. <br>
Risk: Future calls or automated reminders may continue if there is no clear cancellation path. <br>
Mitigation: Confirm call status, cancellation, and stop controls before enabling scheduled or recurring call workflows. <br>
Risk: The security evidence recommends separate review of the RingBot backend service before installation. <br>
Mitigation: Review the backend deployment, network behavior, logging, and access controls before using the skill in production or with personal data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gbessoni/skills/ringbot) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/gbessoni) <br>
- [Twilio](https://twilio.com) <br>
- [LiveKit Cloud](https://cloud.livekit.io) <br>
- [Groq Console](https://console.groq.com) <br>
- [RingBot hosted access](https://talkforceai.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown instructions with bash/curl examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a destination phone number, call purpose, and optional call context; calls may use Twilio, LiveKit, Groq, or hosted RingBot infrastructure.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
