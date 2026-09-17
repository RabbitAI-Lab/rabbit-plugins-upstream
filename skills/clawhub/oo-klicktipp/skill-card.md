## Description:

KlickTipp helps agents handle KlickTipp requests, including subscriber sign-in, sign-off, and sign-out workflows, through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run KlickTipp subscriber actions through an OOMOL-connected account while relying on live connector schemas before sending payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change KlickTipp subscriber records even though its summary emphasizes searching and reading data.

Mitigation: Require explicit user confirmation for signin, signoff, and signout actions before running commands that alter subscriber records.

Risk: The setup instructions include remote installer commands.

Mitigation: Install the oo CLI through a verified official method before running installer commands.

## Reference(s):

- [KlickTipp Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-klicktipp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [KlickTipp homepage](https://www.klicktipp.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before constructing payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
