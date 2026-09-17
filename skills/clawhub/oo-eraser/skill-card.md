## Description:

Eraser (eraser.io). Use this skill for ANY Eraser request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Eraser through an OOMOL-connected account, including reading files and diagrams, creating or updating files, rendering diagrams from DSL, and generating diagrams from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands.

Mitigation: Review before installing, trust the OOMOL installer endpoint only after due diligence, and prefer signed or checksum-verified packages when available.

Risk: The skill can perform Eraser write and destructive actions.

Mitigation: Confirm exact payloads and effects before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-eraser)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Eraser homepage](https://www.eraser.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing actions require user confirmation; destructive actions require explicit approval.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
