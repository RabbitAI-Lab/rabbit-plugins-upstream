## Description:

Paystack lets an agent inspect schemas and run supported Paystack customer and transaction actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage Paystack customers and transactions through an OOMOL-connected account, including listing, fetching, creating, updating, initializing, and verifying records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can install unverified code.

Mitigation: Review the installer path and prefer a trusted, versioned, verifiable oo CLI installation source before using the skill.

Risk: Paystack write actions can affect customer, transaction, or payment-related business data.

Mitigation: Inspect the live action schema and confirm the exact payload and business impact before running write actions.

## Reference(s):

- [Paystack homepage](https://paystack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Paystack Skill](https://clawhub.ai/oomol/skills/oo-paystack)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector schema inspection steps, JSON payload guidance, and safety confirmation guidance for state-changing Paystack actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
