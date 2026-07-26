## Description: <br>
Handle Clawver customer reviews by monitoring ratings, crafting responses, tracking sentiment trends, and supporting reputation management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nwang783](https://clawhub.ai/user/nwang783) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Store operators and support teams use this skill to list Clawver reviews, analyze ratings and sentiment, draft or post professional responses, and configure review webhooks for new feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access customer review data, including reviewer contact details. <br>
Mitigation: Use the least-privileged CLAW_API_KEY available and avoid exposing customer emails unless they are needed for support. <br>
Risk: The skill can publish store responses that affect customer trust and public reputation. <br>
Mitigation: Review generated replies before posting and keep responses concise, professional, and accurate. <br>
Risk: Webhook configuration can send review notifications to an unintended endpoint. <br>
Mitigation: Configure webhooks only to URLs you control and use a strong secret with signature verification. <br>


## Reference(s): <br>
- [Clawver homepage](https://clawver.store) <br>
- [ClawHub skill listing](https://clawhub.ai/nwang783/skills/clawver-reviews) <br>
- [Reviews API Examples](artifact/references/api-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash, Python, JavaScript, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAW_API_KEY for authenticated Clawver API use; review responses are capped at 1000 characters.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
