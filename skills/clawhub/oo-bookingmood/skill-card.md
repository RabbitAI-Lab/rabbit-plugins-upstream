## Description:

Bookingmood (bookingmood.com). Use this skill for Bookingmood requests that search, read, or query booking-related data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Bookingmood action schemas, list bookings and products, and query product availability through an OOMOL-connected Bookingmood account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts directly.

Mitigation: Use a verified oo CLI installation path with pinned releases and checksums before running Bookingmood connector actions.

Risk: Bookingmood access is mediated through an OOMOL-connected account.

Mitigation: Install and use the skill only when OOMOL-mediated access is acceptable, and run actions from the intended account connection.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bookingmood)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Bookingmood Homepage](https://www.bookingmood.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI schema inspection before connector calls; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
