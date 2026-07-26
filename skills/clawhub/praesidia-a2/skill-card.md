## Description: <br>
Verify AI agents, check trust scores (0-100), fetch A2A agent cards, discover marketplace agents, apply guardrails for security and compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msoica](https://clawhub.ai/user/msoica) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to verify agent identity and trust, discover public agents, retrieve A2A agent cards, and manage guardrails for security, moderation, and compliance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can apply or change live agent guardrails through authenticated Praesidia API calls. <br>
Mitigation: Require explicit user confirmation before applying or changing guardrails on production agents, and test guardrail behavior before enabling changes broadly. <br>
Risk: Content submitted for guardrail validation may be sent to Praesidia. <br>
Mitigation: Do not validate confidential, regulated, or secret-containing text unless sharing that content with Praesidia is acceptable. <br>
Risk: Authenticated operations depend on a Praesidia API key. <br>
Mitigation: Use a scoped API key and keep it in the configured environment or OpenClaw configuration rather than exposing it in prompts or outputs. <br>


## Reference(s): <br>
- [Praesidia homepage](https://praesidia.ai) <br>
- [Praesidia API documentation](https://app.praesidia.ai/docs/api) <br>
- [A2A protocol](https://a2a-protocol.org) <br>
- [ClawHub skill page](https://clawhub.ai/msoica/skills/praesidia-a2) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON and JavaScript request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Praesidia API key for authenticated agent and guardrail operations.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
