## Description:

Operate Payhip through an OOMOL-connected account using the oo CLI for coupon and license workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators with Payhip accounts use this skill to inspect live connector schemas and manage coupons and license keys through OOMOL's oo CLI. It supports read, write, and destructive Payhip workflows with confirmation requirements for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review the setup path before installing, trust OOMOL and the oo CLI distribution channel, and prefer a pinned or verifiable installer when available.

Risk: Payhip write and destructive actions can change or remove coupons and license-key state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or delete actions.

## Reference(s):

- [Payhip homepage](https://payhip.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-payhip)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands run with --json.]

## Skill Version(s):

1.0.3 (source: evidence release and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
