## Description: <br>
Calendly API integration with managed OAuth for viewing scheduling data, checking availability, booking meetings, and managing Calendly webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access Calendly scheduling resources through Maton-managed OAuth, inspect availability and scheduled events, book invitees, cancel events, and manage webhook subscriptions with user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Maton API key and can access scheduling data in a connected Calendly account. <br>
Mitigation: Protect MATON_API_KEY and install the skill only when Calendly access through Maton is intended. <br>
Risk: Requests may target the wrong Calendly account when multiple connections are available. <br>
Mitigation: Verify the intended Calendly connection and use the Maton-Connection header when more than one account is connected. <br>
Risk: Write actions can create bookings, cancel events, or change webhook subscriptions. <br>
Mitigation: Approve write actions only after checking the target event, invitee details, webhook URL, scope, and expected effect. <br>


## Reference(s): <br>
- [ClawHub Calendly Skill](https://clawhub.ai/byungkyu/skills/calendly-api) <br>
- [Calendly Developer Portal](https://developer.calendly.com/) <br>
- [Calendly API Reference](https://developer.calendly.com/api-docs) <br>
- [Calendly API Use Cases](https://developer.calendly.com/api-use-cases) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline bash, Python, JavaScript, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; write operations require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
