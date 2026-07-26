## Description: <br>
Verify AI agents, check trust scores (0-100), fetch A2A agent cards, discover marketplace agents, apply guardrails for security and compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msoica](https://clawhub.ai/user/msoica) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to verify agent identity and trust scores, discover public A2A-compatible agents, and configure or validate Praesidia guardrails for agent security, content moderation, and compliance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User content, including sensitive or regulated data, may be sent to the Praesidia API during validation or agent-card lookups. <br>
Mitigation: Use the skill only with trusted Praesidia endpoints, prefer scoped API keys, and avoid submitting secrets or regulated/private content unless external processing is intended. <br>
Risk: Guardrail changes can persist and affect production agent behavior. <br>
Mitigation: Require explicit user approval before applying or changing guardrails, and review the resulting settings in Praesidia after changes are made. <br>


## Reference(s): <br>
- [Praesidia homepage](https://praesidia.ai) <br>
- [Praesidia API documentation](https://app.praesidia.ai/docs/api) <br>
- [Agent-to-Agent protocol](https://a2a-protocol.org) <br>
- [ClawHub skill page](https://clawhub.ai/msoica/skills/praesidia-ai-a2a) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON and JavaScript API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Praesidia API responses to present trust scores, verification status, guardrail details, and recommended user-facing actions.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
