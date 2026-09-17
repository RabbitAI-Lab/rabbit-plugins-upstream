## Description:

Cloudinary enables agents to read, create, and update Cloudinary assets through an OOMOL-connected oo CLI workflow instead of calling the Cloudinary API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Cloudinary action schemas, list or fetch assets, and perform confirmed write operations such as uploads, renames, and asset updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running an internet-hosted installer directly in a shell.

Mitigation: Review the oo CLI installation path before installing, and prefer a verified package, pinned release, checksum, or signed installer.

Risk: Write actions can upload, rename, or update Cloudinary assets.

Mitigation: Inspect the live action schema and confirm the exact asset, payload, and expected effect with the user before running write actions.

## Reference(s):

- [Cloudinary homepage](https://cloudinary.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Cloudinary skill release](https://clawhub.ai/oomol/skills/oo-cloudinary)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return a JSON response with data and meta.executionId when invoked with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
