## Description:

Use flomo through an OOMOL-connected account to read, create, search, and update memos and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate flomo from an agent session, including memo search, memo creation, memo updates, tag operations, daily reviews, and related context retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Review the official install instructions and verify the installer source before running setup commands.

Risk: Write actions can change flomo memo or tag state.

Mitigation: Confirm the exact payload and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub flomo skill page](https://clawhub.ai/oomol/skills/oo-flomo)
- [flomo homepage](https://flomoapp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
