## Description:

Crowdin (crowdin.com) skill for reading, creating, and updating Crowdin data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and localization operators use this skill to list Crowdin projects, branches, directories, and files, and to create branches/directories or upload source files through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run a downloaded installer directly.

Mitigation: Review the installer source first and prefer a pinned, verified installation path.

Risk: Write actions can create Crowdin resources or upload source files.

Mitigation: Fetch the live action schema, confirm the exact payload and effect with the user, and only then run the write or upload command.

## Reference(s):

- [Crowdin homepage](https://crowdin.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-crowdin)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI commands after checking live action schemas; write and upload actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
