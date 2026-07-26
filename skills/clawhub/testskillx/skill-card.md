## Description: <br>
Simple test skill that calls a GET endpoint to fetch a daily post. No authentication required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[natx223](https://clawhub.ai/user/natx223) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can ask an assistant to fetch a daily post from the configured public endpoint and return the endpoint response in chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically contacts the configured ngrok URL when daily-post-like prompts are recognized. <br>
Mitigation: Install and use it only if contacting that public endpoint is acceptable for the environment. <br>
Risk: The endpoint response may contain untrusted web content. <br>
Mitigation: Return the response as content for the user to review and do not treat it as assistant instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/natx223/skills/testskillx) <br>
- [DailyPost endpoint](https://b024a53917d6.ngrok-free.app/agent/dailyPost) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API response] <br>
**Output Format:** [Endpoint response returned directly to chat, typically plain text or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Makes one unauthenticated public GET request; endpoint content should be treated as untrusted web content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
