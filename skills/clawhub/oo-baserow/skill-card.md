## Description:

Baserow lets agents read, create, update, and delete Baserow data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Baserow tables from an agent session, including listing tables and fields, reading rows, creating or updating rows, and deleting rows after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may ask users to pipe a remote installer directly into a shell, creating supply-chain risk.

Mitigation: Review the oo CLI installation path before installing and prefer verified or package-manager installation instructions when available.

Risk: Write and delete actions can change or remove Baserow data.

Mitigation: Confirm the exact payload, target row, and expected effect with the user before write operations, and require explicit approval before destructive deletes.

## Reference(s):

- [ClawHub Baserow Skill](https://clawhub.ai/oomol/skills/oo-baserow)
- [Baserow Homepage](https://baserow.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Installation Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
