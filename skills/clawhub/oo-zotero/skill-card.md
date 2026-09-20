## Description:

Use this skill to operate Zotero through an OOMOL-connected account for reading, creating, updating, and deleting Zotero library data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to manage Zotero user and group libraries through the OOMOL oo CLI. It supports listing, searching, retrieving, creating, updating, and deleting Zotero items and collections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote shell installation commands for the OOMOL oo CLI.

Mitigation: Review the installer source and installation path before use, and prefer a versioned installer with integrity verification.

Risk: Write and destructive actions can modify or delete Zotero library data.

Mitigation: Confirm the exact action, target library item or collection, version, and payload with the user before executing write or destructive commands.

## Reference(s):

- [Zotero homepage](https://www.zotero.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zotero)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
