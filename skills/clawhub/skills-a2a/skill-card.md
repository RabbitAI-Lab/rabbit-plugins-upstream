## Description: <br>
Praesidia helps OpenClaw assistants verify AI agent identities, check trust scores, discover marketplace agents, fetch A2A cards, and manage security, moderation, and compliance guardrails through the Praesidia API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msoica](https://clawhub.ai/user/msoica) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and OpenClaw users use this skill to evaluate whether agents are trustworthy, discover agents by capability, inspect trust and compliance signals, and apply or validate guardrails for security, moderation, and compliance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send agent metadata, validation content, and other user-provided information to a third-party Praesidia API. <br>
Mitigation: Use a least-privilege API key, keep PRAESIDIA_API_URL pointed only at a trusted endpoint, and avoid validating confidential, regulated, or secret-bearing content unless Praesidia's data handling is acceptable. <br>
Risk: The skill can make persistent guardrail changes for an agent or organization. <br>
Mitigation: Require the assistant to show the proposed guardrail configuration and obtain explicit confirmation before applying changes. <br>
Risk: Security scan evidence classified the release as suspicious because confirmation requirements for guardrail changes were unclear. <br>
Mitigation: Review the skill before production use and establish an operational review step for guardrail creation, update, and validation workflows. <br>


## Reference(s): <br>
- [Praesidia homepage](https://praesidia.ai) <br>
- [Praesidia API documentation](https://app.praesidia.ai/docs/api) <br>
- [A2A protocol](https://a2a-protocol.org) <br>
- [ClawHub skill page](https://clawhub.ai/msoica/skills/skills-a2a) <br>
- [Publisher profile](https://clawhub.ai/user/msoica) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown guidance with REST API request examples and structured trust, guardrail, and discovery summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRAESIDIA_API_KEY for authenticated Praesidia API requests; PRAESIDIA_API_URL may override the default endpoint.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
