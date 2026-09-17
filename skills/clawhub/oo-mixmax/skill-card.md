## Description:

This skill helps agents read, create, and update Mixmax data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Mixmax through an OOMOL-connected account for reading sequences and recipients, searching recipient records, and adding recipients to sequences after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell install commands for the oo CLI.

Mitigation: Review the installation path and prefer official, version-pinned, verifiable installation instructions before running installer commands.

Risk: The add_sequence_recipients action can change Mixmax state.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [Mixmax homepage](https://www.mixmax.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mixmax)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector responses as JSON objects with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
