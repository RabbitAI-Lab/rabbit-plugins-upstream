## Description:

The Cat API skill helps agents search and read cat breed and image data from The Cat API through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect The Cat API connector schemas, retrieve individual breeds or images, list and search cat breeds, and search cat images with filters and pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Prefer installing the oo CLI through a verifiable package manager or a pinned, checksum-verified installer, and avoid running remote installer commands from an elevated shell.

Risk: The skill relies on an OOMOL account connection for The Cat API access.

Mitigation: Use the connected-account flow rather than handling raw API tokens, and only run setup or reconnection steps after an auth or connection error.

## Reference(s):

- [The Cat API homepage](https://thecatapi.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-the-cat-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing request payloads; responses from connector runs are JSON.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
