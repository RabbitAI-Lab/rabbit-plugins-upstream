## Description:

Enables agents to search and read ONLYOFFICE DocSpace users, rooms, folders, and file metadata through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to answer ONLYOFFICE DocSpace requests by listing or retrieving connected account data such as users, rooms, folders, and file metadata. It guides the agent to inspect the live connector schema before constructing each request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read ONLYOFFICE DocSpace rooms, folders, file metadata, and user information through the connected OOMOL account.

Mitigation: Install and use it only for intended DocSpace access, with the connected account and scopes reviewed before use.

Risk: Future connector actions marked write or destructive could change, remove, or overwrite DocSpace data.

Mitigation: Review the live schema, exact payload, and expected effect with the user before approving write actions; require explicit approval for destructive actions.

Risk: Connector schemas can change, causing stale payload assumptions or incorrect requests.

Mitigation: Fetch the action's live schema with the oo CLI before constructing each payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-onlyoffice-docspace)
- [ONLYOFFICE DocSpace Homepage](https://www.onlyoffice.com/docspace.aspx)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; read actions are direct, while write or destructive actions require explicit confirmation if such actions are present.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
