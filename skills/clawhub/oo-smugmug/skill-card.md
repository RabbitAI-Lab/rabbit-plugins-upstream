## Description:

SmugMug enables agents to search and read SmugMug data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve SmugMug albums, folders, images, metadata, profile information, and search results through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing network code on a user's machine.

Mitigation: Review the setup path before installing; prefer a verified, versioned oo CLI package or manually inspect and verify the installer before running it.

Risk: Connecting OOMOL to SmugMug lets the connector read SmugMug account data through the authorized connection.

Mitigation: Connect only the intended account and scopes, and run read actions only after confirming the target user, album, folder, or image.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-smugmug)
- [SmugMug Homepage](https://www.smugmug.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SmugMug connector actions return account or public content through the oo CLI; setup guidance may be needed when authentication or connection errors occur.]

## Skill Version(s):

1.0.3 (source: evidence release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
