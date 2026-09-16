## Description:

Zylvie (zylvie.com). Use this skill for ANY Zylvie request - reading, creating, updating, and deleting data. Whenever a task involves Zylvie, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Zylvie products, coupons, license keys, subscriptions, and authenticated account details through the OOMOL-connected oo CLI. It supports read actions and state-changing Zylvie actions while requiring confirmation for write and destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer step before use and prefer a verified, versioned oo CLI source with checksum or signature validation.

Risk: Zylvie write and destructive actions can create, update, delete, archive, redeem, or refund account data.

Mitigation: Approve these actions only after checking the exact target, payload, and expected effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zylvie)
- [Zylvie homepage](https://zylvie.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action results are returned by the oo CLI as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
