## Description:

CoderPad helps agents operate CoderPad through an OOMOL-connected account for reading, creating, and updating interview data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and technical interview teams use this skill to retrieve CoderPad organization, pad, question, usage, and event data, and to create interview pads through the connected CoderPad service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute shell or PowerShell scripts.

Mitigation: Review the setup path before installing and prefer a trusted, verified, version-pinned installation method.

Risk: The skill can create CoderPad interview pads through a write action.

Mitigation: Confirm the exact payload and intended effect with the user before running CoderPad write actions.

## Reference(s):

- [ClawHub CoderPad Skill](https://clawhub.ai/oomol/skills/oo-coderpad)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [CoderPad Homepage](https://coderpad.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CoderPad connector requests and summarize JSON responses returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
