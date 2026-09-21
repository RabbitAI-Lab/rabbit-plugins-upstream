## Description:

PayPal (paypal.com). Use this skill for ANY PayPal request — reading, creating, updating, and deleting data. Whenever a task involves PayPal, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PayPal through an OOMOL-connected account, including order, payment, refund, tracking, balance, and transaction workflows. It is intended to route PayPal tasks through the oo CLI connector instead of direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports broad financial-account authority for PayPal workflows.

Mitigation: Require explicit user approval before payments, refunds, captures, tracking changes, voids, or other write and destructive actions.

Risk: The security scan notes setup commands that pipe remote installer scripts into a shell.

Mitigation: Review the installer source or install the oo CLI through a verified method before running setup commands.

Risk: Connector actions depend on the user having a connected OOMOL PayPal account and valid scopes.

Mitigation: Inspect the live connector schema before each action and use first-time setup only after an authentication, scope, credential, app, or billing failure.

## Reference(s):

- [PayPal homepage](https://www.paypal.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-paypal)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the PayPal connector through the oo CLI and may return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
