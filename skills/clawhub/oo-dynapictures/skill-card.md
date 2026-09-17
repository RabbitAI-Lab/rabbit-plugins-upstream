## Description:

DynaPictures (dynapictures.com). Use this skill for ANY DynaPictures request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected DynaPictures account through OOMOL, including generating template-based images and retrieving or listing templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flagged risky shell installer commands.

Mitigation: Review and independently verify the oo CLI installer source before running curl|bash or irm|iex installation commands.

Risk: The security review noted that image generation is treated as a safe read action.

Mitigation: Confirm the exact generate_images payload and intended account effect with the user before running image generation.

Risk: The skill operates a connected DynaPictures account.

Mitigation: Use it only when the user intends to operate that account and has the required OOMOL and DynaPictures connection in place.

## Reference(s):

- [DynaPictures homepage](https://dynapictures.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dynapictures)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs and connector responses when actions are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
