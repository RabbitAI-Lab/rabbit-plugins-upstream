## Description:

Helps agents inspect Razorpay action schemas and run order, payment, and refund operations through an OOMOL-connected Razorpay account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to read Razorpay orders and payments, create orders, and issue refunds from an agent workflow after confirming financial write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Use a verified, signed, or separately reviewed oo CLI installation path and avoid elevated privileges.

Risk: The skill can create Razorpay orders and refunds.

Mitigation: Confirm the exact Razorpay account, amount, payment or order identifier, and payload before allowing write actions.

Risk: Connector-mediated Razorpay access requires trusting OOMOL's connector and credential handling.

Mitigation: Install only when the publisher and OOMOL connector model are acceptable for the intended account.

## Reference(s):

- [ClawHub Razorpay Skill](https://clawhub.ai/oomol/skills/oo-razorpay)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Installation Guide](https://cli.oomol.com/install-guide.md)
- [Razorpay](https://razorpay.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live action schemas before execution and to confirm financial write payloads before running them.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
