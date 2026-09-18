## Description:

Helps agents operate Recharge through an OOMOL-connected account using the oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and list Recharge charges, customers, orders, products, and subscriptions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts that execute directly in a shell.

Mitigation: Review the oo CLI installation path, prefer a versioned installer from OOMOL, and verify publisher, signature, or checksum before running it manually.

Risk: Recharge reads may expose customer, order, subscription, and related commerce data through the OOMOL connector.

Mitigation: Confirm the user is comfortable routing Recharge data through OOMOL and use an account connection with appropriate scopes before running actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-recharge)
- [Recharge homepage](https://getrecharge.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides oo CLI schema inspection and connector execution for Recharge actions.]

## Skill Version(s):

1.0.2 (source: server evidence release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
