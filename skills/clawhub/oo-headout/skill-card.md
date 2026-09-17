## Description:

Headout lets agents search and retrieve Headout cities, categories, products, variants, inventory, and bookings through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Headout travel experiences and retrieve product, inventory, pricing, and booking data from an OOMOL-connected Headout account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may execute remote installer scripts locally.

Mitigation: Use a signed or checksum-verified installation method for the oo CLI, and run remote installer commands only after explicit user approval.

Risk: Unlisted, write, or destructive connector actions could affect a Headout account.

Mitigation: Require confirmation of the exact action, payload, and expected effect before running any action that is not clearly read-only.

## Reference(s):

- [ClawHub Headout Skill](https://clawhub.ai/oomol/skills/oo-headout)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Headout](https://www.headout.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before running connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
