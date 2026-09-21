## Description:

Waffo Pancake (waffo.ai) lets an agent read, create, update, and delete Waffo Pancake data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Waffo Pancake stores, products, checkout sessions, payments, refunds, orders, and subscriptions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Waffo write or destructive actions can affect payment, refund, subscription, product, or store data.

Mitigation: Confirm the exact payload, target account, and expected business effect before allowing write or destructive actions.

Risk: The setup guidance includes remote-script CLI installation steps.

Mitigation: Review the oo CLI installation path first and prefer a verified or documented installer with version and integrity checks.

## Reference(s):

- [Waffo Pancake homepage](https://www.waffo.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waffo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of oo connector schema and oo connector run commands for Waffo actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
