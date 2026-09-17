## Description:

Enables an agent to operate Stripe customers, products, and prices through the OOMOL oo CLI, including read, search, create, update, and delete actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and business operators use this skill to inspect and manage Stripe account data after connecting Stripe through OOMOL. It supports customer, product, and price workflows, including state-changing actions that require confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute downloaded code locally.

Mitigation: Prefer verified OOMOL installation or package-manager steps before running setup commands.

Risk: Write and destructive Stripe actions can modify or delete business data.

Mitigation: Confirm the exact action, target identifiers, payload, and expected effect with the user before execution.

Risk: The skill depends on OOMOL server-side credential handling for the connected Stripe account.

Mitigation: Install only when the user is comfortable authorizing OOMOL to operate the Stripe account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stripe)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Stripe homepage](https://stripe.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
