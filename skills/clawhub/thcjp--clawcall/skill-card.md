## Description: <br>
Clawcall lets an AI agent place real U.S. phone calls, navigate menus or wait times, and return call status, transcript, outcome, and a recording link when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to have an AI agent prepare and place U.S. phone calls for tasks such as information gathering, reservations, customer-service waits, live transfer, and inbound-call preferences. It is most appropriate when the user has explicitly asked for a phone-call workflow and has supplied the private facts or decision boundaries needed for the call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate real phone calls and has broad trigger language. <br>
Mitigation: Use it only for explicit phone-call requests, and narrow the published trigger language to phone-call intents. <br>
Risk: Calls may lead to bookings, cancellations, purchases, payments, or account changes. <br>
Mitigation: Confirm user approval and decision boundaries before any call that could create a commitment or account change. <br>
Risk: The skill stores and reuses API keys and phone numbers. <br>
Mitigation: Avoid saving credentials or phone numbers unless the user understands where they are stored and how to remove them. <br>
Risk: The artifact describes account linking with an API key in a URL. <br>
Mitigation: Prefer safer account-linking flows that do not expose raw API keys in URLs. <br>


## Reference(s): <br>
- [Clawcall ClawHub listing](https://clawhub.ai/thcjp/skills/clawcall) <br>
- [Voice Call Service API base URL](https://api.voicecall.example) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown with API request examples, JSON snippets, call instructions, and call-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include call IDs, lifecycle status, transcripts, outcomes, recording links, and saved API-key or phone-number state.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
