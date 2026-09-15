## Description:

SmugMug lets an agent search and read SmugMug users, folders, albums, images, image metadata, and image sizes through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve SmugMug account, folder, album, image, metadata, and search results through the oo CLI after connecting a SmugMug account in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts that are run directly in a shell.

Mitigation: Review the setup path before installation and prefer a verified or manually reviewed oo CLI installation method.

Risk: The skill depends on OOMOL account access and server-side credential injection for SmugMug actions.

Mitigation: Use the skill only when the OOMOL publisher and connected-account model are acceptable for the deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-smugmug)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SmugMug Homepage](https://www.smugmug.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, OOMOL sign-in, and a connected SmugMug account; listed actions are read-only.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
