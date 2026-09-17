## Description:

Paystack helps agents operate Paystack through an OOMOL-connected account for customer and transaction read, create, update, initialize, and verify workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Paystack action schemas and run customer or transaction workflows through the oo CLI with server-side credential injection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Paystack customer and transaction data through an OOMOL-connected account.

Mitigation: Treat read results as sensitive and use the skill only when routing Paystack operations through OOMOL is acceptable.

Risk: Customer creation, customer update, and transaction initialization can change Paystack state.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running write actions.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified, pinned installation path and avoid running pipe-to-shell installers blindly.

## Reference(s):

- [ClawHub Paystack Skill](https://clawhub.ai/oomol/skills/oo-paystack)
- [Paystack Homepage](https://paystack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing payloads; customer creation, customer update, and transaction initialization require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
