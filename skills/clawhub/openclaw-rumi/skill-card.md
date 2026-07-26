## Description: <br>
Match with real humans who share your interests — topic-driven matching, not photo swiping. Chat through OpenClaw or on the web. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ricky610329](https://clawhub.ai/user/ricky610329) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users use Rumi to find and chat with real people who share their interests, expertise needs, or conversation topics. The skill helps the agent set up the external service, create one matching session with a rich user-approved description, poll for status, and relay chat messages when a match is found. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Matching descriptions and chat relay can expose personal context to an external service or another person. <br>
Mitigation: Before starting a match, ask the user to review the exact description that will be sent and remove private details. <br>
Risk: The Rumi API token can grant access to the user's account if exposed. <br>
Mitigation: Treat the token like a password, keep it in plugin configuration, and rotate it if exposure is suspected. <br>
Risk: The skill connects users with real people, so age and safety constraints matter. <br>
Mitigation: Respect age verification, keep minors matched only with other minors, and let users choose what personal information to reveal. <br>


## Reference(s): <br>
- [Rumi on ClawHub](https://clawhub.ai/ricky610329/skills/openclaw-rumi) <br>
- [Publisher profile: ricky610329](https://clawhub.ai/user/ricky610329) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, API Calls, Configuration] <br>
**Output Format:** [Conversational text with setup links, status updates, icebreakers, chat messages, and tool-call guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask the user to review the matching description before starting a session and may require an API token stored in plugin configuration.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
