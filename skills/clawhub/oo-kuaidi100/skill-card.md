## Description:

Kuaidi100 enables agents to run Kuaidi100 tracking, pickup order, quote, and delivery estimate actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to perform Kuaidi100 logistics workflows, including carrier detection, real-time tracking, pickup order handling, shipping price estimates, and delivery-time estimates. The skill supports schema-first command construction and calls out actions that require confirmation before changing state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute downloaded scripts locally.

Mitigation: Review the setup path before installing and prefer a verified package, pinned release, checksum or signature validation, or manual inspection of the installer.

Risk: Pickup-order actions can create, cancel, quote, or query orders and may change Kuaidi100 state.

Mitigation: Fetch the live action schema, confirm the exact payload and effect with the user, and run write actions only after explicit approval.

## Reference(s):

- [ClawHub Kuaidi100 Skill Page](https://clawhub.ai/oomol/skills/oo-kuaidi100)
- [Kuaidi100 Homepage](https://www.kuaidi100.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
