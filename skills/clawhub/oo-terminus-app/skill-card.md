## Description:

Terminus App helps agents read, create, and update Terminus App data through the OOMOL terminus_app connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when a user asks to list Terminus projects, inspect tracking conventions, read tracked links, or create tagged links through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unpinned remote installer commands that can execute downloaded code.

Mitigation: Review the oo CLI installer through an official source and prefer a signed or checksum-verified installation path before installing.

Risk: The create_link action can change Terminus App state in the connected OOMOL account.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-terminus-app)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Terminus App homepage](https://www.terminusapp.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require payload and effect confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
