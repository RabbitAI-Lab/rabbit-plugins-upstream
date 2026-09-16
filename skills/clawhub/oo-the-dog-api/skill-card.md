## Description:

The Dog API skill lets an agent use OOMOL's oo CLI to read, search, create, and delete The Dog API data through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve dog breeds and images, search The Dog API data, and manage favourites or votes through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Use a verified installer or package manager where possible, pin the release, verify checksums or signatures, and run installation from a non-elevated shell.

Risk: The skill supports write and destructive actions for favourites and votes.

Mitigation: Confirm the exact payload, target record, and intended effect with the user before running write or delete actions.

## Reference(s):

- [The Dog API homepage](https://thedogapi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [The Dog API ClawHub listing](https://clawhub.ai/oomol/skills/oo-the-dog-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include live oo CLI schema checks, connector execution commands, JSON request payloads, and summaries of returned API data.]

## Skill Version(s):

1.0.4 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
