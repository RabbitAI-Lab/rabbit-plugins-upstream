## Description:

Payhip (payhip.com). Use this skill for ANY Payhip request: reading, creating, updating, and deleting Payhip data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Payhip account workflows through an OOMOL-connected account, including coupon management and license verification or status changes. It guides agents to inspect live connector schemas before running Payhip actions and to request confirmation for write or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to execute remotely fetched oo CLI installer scripts directly in a shell.

Mitigation: Review the oo CLI installer before running it, and prefer an official package or verified installer when available.

Risk: Payhip write and destructive actions can change coupons or license status.

Mitigation: Fetch the live action schema and confirm the exact payload, target, and effect with the user before running write or destructive commands.

## Reference(s):

- [ClawHub Payhip skill page](https://clawhub.ai/oomol/skills/oo-payhip)
- [Payhip homepage](https://payhip.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Payhip connector schemas before execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
