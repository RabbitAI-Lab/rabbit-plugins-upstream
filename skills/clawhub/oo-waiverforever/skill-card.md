## Description:

WaiverForever helps agents read, create, and update WaiverForever data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate WaiverForever from an agent, including listing templates, creating signing links or waiver request groups, retrieving waivers and account information, and searching signed waivers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes piping remote install scripts directly into a shell.

Mitigation: Prefer downloading and verifying the oo CLI from official documentation before installation.

Risk: Write actions can create WaiverForever signing links or waiver request groups.

Mitigation: Confirm the exact payload and user-visible effect before running any write action.

## Reference(s):

- [WaiverForever homepage](https://www.waiverforever.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [WaiverForever skill on ClawHub](https://clawhub.ai/oomol/skills/oo-waiverforever)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the user to have the oo CLI installed, be signed in to OOMOL, and have WaiverForever connected before actions can run.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
