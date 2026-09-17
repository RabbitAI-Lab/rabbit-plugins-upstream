## Description:

Google Slides lets agents read, create, update, copy, and thumbnail Google Slides presentations through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read, create, update, copy, and thumbnail Google Slides presentations through an OOMOL-connected account. It is intended for agents that need to inspect live action schemas, run Google Slides connector actions, and confirm payloads before write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote installer directly in a shell.

Mitigation: Review the installer path before installing, and prefer a package-manager or version-pinned OOMOL CLI installation with checksum or signature verification.

Risk: Write and batchUpdate actions can change Google Slides state.

Mitigation: Approve write actions only after checking the exact target presentation, payload, and expected effect.

## Reference(s):

- [Google Slides homepage](https://workspace.google.com/products/slides/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Google Slides connector command results as JSON when actions are executed.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
