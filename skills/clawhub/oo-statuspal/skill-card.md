## Description:

StatusPal lets an agent inspect schemas and read StatusPal incidents, services, page status, and page summaries through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve StatusPal operational data, including incidents, services, current page status, and page summaries, from an already connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code.

Mitigation: Do not let an agent run the remote installer automatically; use official installation documentation, pinned packages, and checksum or signature verification before installation.

## Reference(s):

- [StatusPal homepage](https://www.statuspal.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub StatusPal skill page](https://clawhub.ai/oomol/skills/oo-statuspal)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, OOMOL sign-in, and a connected StatusPal account.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
