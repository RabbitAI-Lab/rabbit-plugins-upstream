## Description:

This skill operates Stripe through OOMOL's oo CLI connector for reading, creating, updating, and deleting Stripe account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with an OOMOL-connected Stripe account use this skill to inspect Stripe schemas and run customer, product, price, and account actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can create, update, delete, or overwrite Stripe account data.

Mitigation: Confirm the exact payload, effect, and target with the user before running any action marked write or destructive.

Risk: The documented one-line installer commands execute remote scripts.

Mitigation: Prefer an official, verifiable oo CLI installation path and avoid running remote installer commands blindly.

Risk: The skill depends on OOMOL mediating access to the user's Stripe account.

Mitigation: Install and use it only when the user trusts OOMOL for Stripe access, and verify the connected account and scopes before state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stripe)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Stripe](https://stripe.com)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from executed connector actions are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.5 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
