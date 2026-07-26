## Description: <br>
Book Calendly meetings instantly from natural-language requests without link sharing or tab switching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dompi123](https://clawhub.ai/user/dompi123) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and teams use this skill to let an agent create Calendly bookings from attendee name, email, timezone, and requested time details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create real Calendly bookings through the user's account, including accidental bookings from broad booking requests. <br>
Mitigation: Use explicit Calendly-specific commands and confirm attendee details and time before submission. <br>
Risk: A Calendly API token is required and could continue enabling booking actions after the user stops using the skill. <br>
Mitigation: Store the token only in the configured environment variable and remove or revoke it when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/dompi123/skills/calendly-quick-book) <br>
- [Publisher profile](https://clawhub.ai/user/dompi123) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Calendly API and webhooks integrations](https://calendly.com/integrations/api_webhooks) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and structured booking responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CALENDLY_API_TOKEN and user-provided attendee name, email, timezone, and requested time.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
