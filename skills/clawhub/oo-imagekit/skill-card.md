## Description:

ImageKit (imagekit.io). Use this skill for ANY ImageKit request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage ImageKit media assets through an OOMOL-connected account. It supports listing and searching assets, retrieving file and media metadata, requesting cache purges, checking purge status, and deleting files after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can run a remote installer script for the oo CLI.

Mitigation: Install the CLI manually from trusted documentation and verify the installer before use.

Risk: The skill can permanently delete ImageKit files or purge cached content.

Mitigation: Approve delete_file or purge_cache only after checking the exact target and payload.

Risk: ImageKit actions are mediated through an OOMOL-connected account.

Mitigation: Install only when the user is comfortable with OOMOL mediating ImageKit actions and server-side credential handling.

## Reference(s):

- [ClawHub ImageKit skill](https://clawhub.ai/oomol/skills/oo-imagekit)
- [ImageKit homepage](https://imagekit.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses; destructive actions require explicit target confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
