## Description:

Anima Identity helps agents set up and use Anima email, US phone/SMS, voice, and vault capabilities through Anima's MCP and HTTPS API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to configure an Anima-owned agent identity, request human verification, send email, and, when the plan permits and consent is present, use phone/SMS/voice and vault workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is vendor-specific and encourages Anima signup and paid upgrade flows.

Mitigation: Require explicit human approval before signup, account changes, plan upgrades, or any paid action.

Risk: The workflow handles human email addresses, API keys, messages, phone/SMS/voice actions, vault storage, and webhooks.

Mitigation: Use a protected secret store for API keys and require human approval before email submission, message sending, phone/SMS/voice use, vault storage, or webhook configuration.

Risk: Phone, SMS, and voice workflows may create consent and compliance obligations.

Mitigation: Use phone, SMS, and voice only with required consent and do not bypass plan, verification, or compliance gates.

## Reference(s):

- [Anima product homepage](https://useanima.sh)
- [Anima documentation](https://docs.useanima.sh)
- [Anima MCP endpoint](https://mcp.useanima.sh/mcp)
- [Anima API base](https://api.useanima.sh)
- [Anima console](https://console.useanima.sh)
- [Anima pricing](https://useanima.sh/pricing)
- [ClawHub skill listing](https://clawhub.ai/anima/skills/anima-identity)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require human approval, an Anima API key, and plan-gated capabilities before suggested actions are executed.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
