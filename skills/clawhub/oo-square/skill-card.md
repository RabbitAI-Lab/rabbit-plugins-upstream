## Description:

Provides an oo CLI-based Square connector for reading, creating, and updating customer and seller-location data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Square through an OOMOL-connected account, including customer creation, retrieval, listing, searching, updates, and seller-location listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path documents remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Install only after independently trusting and verifying the oo CLI source; prefer a signed or package-manager installation path when available.

Risk: Write actions can create or update Square customer records.

Mitigation: Confirm the exact payload and expected Square-side effect with the user before running write actions.

## Reference(s):

- [ClawHub Square skill page](https://clawhub.ai/oomol/skills/oo-square)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Square homepage](https://squareup.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before connector calls; write actions require confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
