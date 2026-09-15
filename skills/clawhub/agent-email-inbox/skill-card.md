## Description:

Agent Email Inbox guides an agent through creating, verifying, and using an Anima-owned email inbox, with related guidance for combined email, phone/SMS/voice, and vault workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to provision and verify an Anima inbox, send and inspect agent email, and decide when paid Anima capabilities are needed for higher volume, custom domains, or phone/SMS/voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates an Anima account or inbox and sends signup details to Anima.

Mitigation: Get explicit human approval before submitting an email address and review what information will be sent to Anima.

Risk: Anima API keys or inbox identifiers could be exposed if handled in chat or stored casually.

Mitigation: Store API keys in environment variables, a secrets manager, or SecretRef, and do not send keys outside Anima hosts.

Risk: Default vault creation may be more capability than the user intended.

Mitigation: Review whether vault provisioning is desired before signup and explain the resulting identity and credential storage behavior.

Risk: The optional npm CLI path adds package supply-chain exposure.

Mitigation: Prefer the API or MCP path when available, or run the pinned CLI version in a minimal workspace.

Risk: Agent email can be misused for unwanted or unverified outreach.

Mitigation: Send only after verification, get explicit consent where required, and respect suppression, opt-out, bounce, loop-protection, and quota controls.

## Reference(s):

- [Anima Product](https://useanima.sh)
- [Anima Documentation](https://docs.useanima.sh)
- [Anima MCP Endpoint](https://mcp.useanima.sh/mcp)
- [Anima API Base](https://api.useanima.sh)
- [Anima Pricing](https://useanima.sh/pricing)
- [ClawHub Skill Page](https://clawhub.ai/anima/skills/agent-email-inbox)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with bash and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl, npm/npx, CLI commands, endpoint references, and secret-handling guidance.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
