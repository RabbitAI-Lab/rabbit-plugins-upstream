## Description:

DocuGenerate (docugenerate.com) support for reading, creating, updating, and deleting DocuGenerate data through the OOMOL-connected `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate DocuGenerate through an OOMOL-connected account, including template discovery, document generation, document retrieval, renaming, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installation commands that can execute changing remote code.

Mitigation: Review the installer source independently before running it, or install the oo CLI through a trusted package or manually verified path.

Risk: The skill can run write and destructive DocuGenerate actions, including document rename and permanent deletion.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write action, and require explicit approval before deletion.

Risk: Commands operate through a connected OOMOL and DocuGenerate account.

Mitigation: Use the skill only when the user trusts the connected account access and has verified that the DocuGenerate connection is intended for the requested task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-docugenerate)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [DocuGenerate Homepage](https://www.docugenerate.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
