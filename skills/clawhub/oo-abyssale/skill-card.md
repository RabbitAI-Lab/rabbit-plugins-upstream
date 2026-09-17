## Description:

Abyssale helps agents operate Abyssale through the OOMOL oo CLI to read, create, and update Abyssale data without calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Abyssale connector schemas, generate banners, retrieve design and file metadata, list projects and fonts, and create Abyssale projects or dynamic image URLs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review the installer path before use; prefer verified, version-pinned documentation or a trusted package manager, and do not let an agent run the remote installer automatically.

Risk: Some Abyssale actions can create projects or dynamic image URLs and change account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Abyssale homepage](https://www.abyssale.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-abyssale)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent actions may return Abyssale connector JSON data and generated file metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
