## Description:

DynaPictures lets agents list API-ready templates, inspect customizable template layers, and generate hosted image URLs through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate DynaPictures from an OOMOL-connected account, including listing API-ready templates, retrieving template layer details, and generating image URLs from templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the installer source and prefer a verified package or signed release before running setup commands.

Risk: The generate_images action is a write operation that creates hosted image outputs from template data.

Mitigation: Confirm the template UID, payload, and expected effect with the user before running the write action.

## Reference(s):

- [ClawHub DynaPictures skill page](https://clawhub.ai/oomol/skills/oo-dynapictures)
- [DynaPictures homepage](https://dynapictures.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; action results are JSON that may include hosted image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require confirming the exact payload and effect with the user before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
