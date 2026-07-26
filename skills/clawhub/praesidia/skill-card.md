## Description: <br>
Praesidia helps agents verify AI agent identities, inspect trust scores, discover marketplace agents, fetch A2A cards, and manage security or compliance guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msoica](https://clawhub.ai/user/msoica) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI assistant users use this skill to check whether agents are registered and trustworthy, find public agents by capability, and configure guardrails for security, content moderation, or compliance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a Praesidia API key to access private or organization-scoped agent and guardrail data. <br>
Mitigation: Use a scoped API key where possible and install the skill only when Praesidia access is intended. <br>
Risk: Validating secrets or regulated data through Praesidia may create privacy or compliance exposure if Praesidia is not authorized for that data. <br>
Mitigation: Avoid submitting secrets or regulated data unless Praesidia is approved for that data class. <br>
Risk: Applying guardrails can change agent behavior through scope, action, severity, and rollback choices. <br>
Mitigation: Review organization ID, agent ID, scope, action, severity, and rollback steps before applying or changing guardrails. <br>


## Reference(s): <br>
- [Praesidia homepage](https://praesidia.ai) <br>
- [Praesidia API documentation](https://app.praesidia.ai/docs/api) <br>
- [A2A protocol](https://a2a-protocol.org) <br>
- [ClawHub skill page](https://clawhub.ai/msoica/skills/praesidia) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration, API Calls] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and API request snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRAESIDIA_API_KEY for private or organization-scoped Praesidia API access.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
