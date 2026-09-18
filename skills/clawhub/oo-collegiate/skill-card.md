## Description:

This skill lets agents search and read Merriam-Webster Collegiate dictionary data through the OOMOL collegiate connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to look up Merriam-Webster Collegiate dictionary entries or spelling suggestions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The lookup action is read-only, but setup instructions may ask users to run installer commands that execute code fetched live from OOMOL.

Mitigation: Review the installation step before use and prefer a verified package, checksum or signature validation, or manual inspection before running remote installer commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-collegiate)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Merriam-Webster Collegiate homepage](https://www.merriam-webster.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action calls and returns dictionary lookup data from the collegiate connector.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
