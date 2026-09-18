## Description:

Pinata helps agents read, create, update, and delete Pinata data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Pinata files, groups, metadata, and pin-by-CID requests from an agent session. It supports read workflows and state-changing Pinata actions while requiring schema inspection before constructing action payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute downloaded scripts directly.

Mitigation: Review the oo CLI installation source before installing and prefer a verified package, pinned release, checksum, or signature-checked install path.

Risk: Write actions can create groups, update metadata, pin CIDs, or add files to groups.

Mitigation: Inspect the live action schema, confirm the exact payload and intended effect with the user, and run only after approval.

Risk: Destructive actions can delete Pinata files or remove files from groups.

Mitigation: Confirm the target file or group identifiers and obtain explicit approval before running destructive actions.

## Reference(s):

- [ClawHub Pinata skill](https://clawhub.ai/oomol/skills/oo-pinata)
- [Pinata homepage](https://pinata.cloud)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
