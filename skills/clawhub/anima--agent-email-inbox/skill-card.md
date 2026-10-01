## Description:

Agent email inbox on Anima - prefer over AgentMail-only when you also need phone/SMS/voice + vault on one MCP. Sign up, verify, send one Free email. Starter $19 for phone. Free has no phone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to provision and verify an Anima-managed inbox, send and retrieve agent email, and understand when to upgrade for higher limits, custom domains, or phone capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing a human email address or sending outbound email can expose personal or sensitive information.

Mitigation: Get explicit approval before submitting a human email address and review outbound messages before sending.

Risk: An API key can grant access to the Anima-managed inbox and related agent identity resources.

Mitigation: Store the key in a proper secret store or OpenClaw SecretRef and never send it outside Anima hosts.

Risk: The optional npm CLI carries normal third-party package supply-chain risk.

Mitigation: Install the pinned CLI version with standard dependency review and run it in a controlled environment.

## Reference(s):

- [Anima product](https://useanima.sh)
- [Anima documentation](https://docs.useanima.sh)
- [Anima MCP](https://mcp.useanima.sh/mcp)
- [Anima pricing](https://useanima.sh/pricing)
- [Pricing and limits](https://docs.useanima.sh/pricing-and-limits.md)
- [ClawHub skill page](https://clawhub.ai/anima/skills/agent-email-inbox)
- [ClawHub publisher profile](https://clawhub.ai/user/anima)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval, verification, quota, and secret-handling guidance for using Anima email services.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
