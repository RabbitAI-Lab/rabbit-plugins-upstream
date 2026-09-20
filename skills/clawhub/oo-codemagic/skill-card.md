## Description:

Codemagic connector workflow for reading Codemagic account, team, app, and build data, and for starting or canceling builds through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to inspect Codemagic users, teams, apps, and builds, and to create or cancel Codemagic builds through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes an oo CLI installer command that should be reviewed before execution.

Mitigation: Confirm trust in OOMOL's installer source or use an official package path before installing the CLI.

Risk: The create_build and cancel_build actions can start or cancel Codemagic builds.

Mitigation: Review the live action schema, exact payload, target app or build, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Codemagic Skill](https://clawhub.ai/oomol/skills/oo-codemagic)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Codemagic](https://codemagic.io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands, setup notes, and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live Codemagic action schemas from the oo CLI before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
