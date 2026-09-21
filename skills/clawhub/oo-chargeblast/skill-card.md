## Description:

Chargeblast helps agents read, create, and update Chargeblast data through OOMOL's Chargeblast connector instead of calling the Chargeblast API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and support teams use this skill to inspect Chargeblast alerts, orders, merchants, and deflection logs. They can also create credit requests or update alerts after confirming the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup suggests piping a remote installer script directly into a shell.

Mitigation: Review or replace the CLI installation step before installing; prefer official documentation, a pinned release, or manual script review.

Risk: Write actions can change Chargeblast business records.

Mitigation: Confirm the exact payload and expected effect with the user before approving credit request creation or alert updates.

## Reference(s):

- [Chargeblast skill on ClawHub](https://clawhub.ai/oomol/skills/oo-chargeblast)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Chargeblast homepage](https://www.chargeblast.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can run directly; write actions require confirmation of the exact payload and expected effect.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
