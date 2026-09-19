## Description:

Favro lets an agent read, create, and update Favro data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Favro workspace operators use this skill to have an agent inspect Favro connector schemas, retrieve organization, collection, board, widget, and card data, and perform confirmed card write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions can execute unreviewed code if followed blindly.

Mitigation: Review the installer path before installing, prefer verified releases or package-manager sources, and require explicit approval before running curl-to-bash or PowerShell iex commands.

Risk: Favro write actions can change workspace card data.

Mitigation: Inspect the live action schema and confirm the exact create_card or update_card payload and expected effect before running the command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-favro)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Favro homepage](https://www.favro.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation of the exact payload and intended effect before execution.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
