## Description:

Recharge (getrecharge.com). Use this skill for Recharge requests that read, create, or update Recharge data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Recharge through OOMOL's oo CLI connector, including reading customers, orders, products, subscriptions, and charges and running supported account actions after inspecting live schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute unverified code during first-time setup.

Mitigation: Review the installer path, prefer signed or verifiable oo CLI releases, and avoid pipe-to-shell installation when a safer package is available.

Risk: Recharge actions may alter account, customer, order, charge, or subscription data.

Mitigation: Inspect the live connector schema and confirm the exact payload and effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-recharge)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Recharge Homepage](https://getrecharge.com/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas; command results include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: metadata.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
