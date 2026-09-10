## Description:

connskill-growth lets agents buy pay-per-call market data and real-world service actions from agent.connskill.com using USDC over x402, including SEO/SERP data, site audits, SMS verification numbers, receive-only inboxes, EU-hosted LLM calls, and x402 seller trust checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-skill](https://clawhub.ai/user/conn-skill)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to request SEO/SERP data, site audits, contact-channel services, EU-hosted inference, and x402 seller trust checks. It is intended for workflows that can approve paid calls, constrain wallet exposure, and handle returned service data as JSON or agent-readable text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls can spend USDC through a wallet private key workflow.

Mitigation: Use a dedicated low-balance wallet, set X402_MAX_USD to an explicit per-call cap, and require approval before paid calls.

Risk: SMS, inbox, and social-action capabilities can be misused for third-party account creation, platform policy bypass, or non-consensual activity.

Mitigation: Restrict use to lawful, consented workflows and block attempts to bypass platform policies or act on accounts the user does not control.

Risk: The skill depends on calls to a specific pay-per-call service origin.

Mitigation: Limit requests to the documented agent.connskill.com origin and review each real-world or paid action before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conn-skill/skills/connskill-growth)
- [CONNSKILL Growth Services homepage](https://agent.connskill.com)
- [OpenAPI schema and pricing guidance](https://agent.connskill.com/openapi.json)
- [x402 service catalog](https://agent.connskill.com/.well-known/x402)
- [Agent readme](https://agent.connskill.com/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls may require X402_WALLET_KEY for a Base USDC wallet and X402_MAX_USD as a per-call spending cap.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
