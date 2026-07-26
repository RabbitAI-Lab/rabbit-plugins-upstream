## Description: <br>
Interact with Skylight Calendar frame - manage calendar events, chores, lists, task box items, and rewards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[riyadchowdhury](https://clawhub.ai/user/riyadchowdhury) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users with Skylight Calendar smart displays use this skill to ask an agent for Skylight account setup guidance and curl-based actions for calendar events, chores, lists, task box items, categories, rewards, frame details, and devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to handle sensitive Skylight account credentials or authorization tokens. <br>
Mitigation: Use the email/password flow only when the user accepts agent access to Skylight household data, avoid exposing tokens in logs or chat history, and rotate or revoke exposed tokens where possible. <br>
Risk: The token-capture option relies on HTTPS proxy interception. <br>
Mitigation: Avoid the proxy capture method unless the user understands TLS interception, remove trusted proxy certificates afterward, and prefer the normal login flow when possible. <br>
Risk: The skill uses an unofficial, reverse-engineered Skylight API that may change without notice. <br>
Mitigation: Review generated API commands before execution and verify results against the user's Skylight account. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/riyadchowdhury/skills/skylight-skill) <br>
- [Skylight Website](https://ourskylight.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and SKYLIGHT_FRAME_ID; authentication uses either SKYLIGHT_EMAIL with SKYLIGHT_PASSWORD or SKYLIGHT_TOKEN.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
