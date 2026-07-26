## Description: <br>
Praesidia helps agents verify AI agents, check trust scores, fetch A2A agent cards, discover marketplace agents, and apply guardrails for security and compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msoica](https://clawhub.ai/user/msoica) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use Praesidia to evaluate agent identity and trust, discover public or account-accessible agents, and configure guardrails for agent security, content moderation, and compliance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User content may be sent to Praesidia for guardrail validation. <br>
Mitigation: Use a least-privilege PRAESIDIA_API_KEY and get explicit user approval before sending sensitive text for validation. <br>
Risk: The skill can make account-backed guardrail configuration changes. <br>
Mitigation: Confirm the target organization, agent, guardrail template, action, scope, and severity before applying changes. <br>
Risk: A custom PRAESIDIA_API_URL can redirect requests away from the expected Praesidia endpoint. <br>
Mitigation: Verify PRAESIDIA_API_URL before use and prefer the documented production endpoint unless intentionally testing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/msoica/skills/praesidia-a2a) <br>
- [Praesidia Homepage](https://praesidia.ai) <br>
- [Praesidia API Documentation](https://app.praesidia.ai/docs/api) <br>
- [A2A Protocol](https://a2a-protocol.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and JavaScript-style API call examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API request examples and summarized trust, discovery, or guardrail results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
