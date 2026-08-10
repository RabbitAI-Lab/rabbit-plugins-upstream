## Description:

mubu-integration lets agents and users manage Mubu outlines from the command line, including Markdown import/export, Obsidian workflows, search, tree export, and OPML or FreeMind export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and agent operators use this skill to read, convert, and manage Mubu outlines as Markdown. Common uses include syncing Mubu content with Obsidian, letting an agent read or update structured notes, and exporting outline trees for local review or backup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authenticates to a real Mubu account and can change account content.

Mitigation: Use a dedicated or low-risk account where possible, verify target document and folder IDs before write operations, and begin with read-only list/get/export operations when exploring.

Risk: The documented confirmation boundary is not universal; several write commands may not require --yes.

Mitigation: Do not treat --yes as the only safety control. Review the specific command behavior before use and keep recoverable backups of important Mubu content.

Risk: Local credential and token files can expose account access if mishandled.

Mitigation: Protect ~/.mubu_token and ~/.workbuddy/.env.mubu, avoid sharing terminal logs or exported configuration, and rotate credentials if a token file may have been exposed.

Risk: export-tree can create a bulk local copy of Mubu content.

Mitigation: Store exports in an access-controlled location, review generated files before sharing, and remove temporary exports when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/mubu-integration)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Example weekly outline](artifact/examples/weekly.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, OPML or FreeMind XML, and command-line text depending on the requested operation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Markdown exports and may perform authenticated API operations against the user's Mubu account.]

## Skill Version(s):

1.3.12 (source: server release evidence and CHANGELOG, released 2026-08-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
