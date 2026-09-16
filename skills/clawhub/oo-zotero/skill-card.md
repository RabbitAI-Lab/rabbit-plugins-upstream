## Description:

Zotero automation for reading, creating, updating, and deleting Zotero library data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Zotero connector schemas and operate Zotero user or group libraries through an OOMOL-connected account. It supports listing and retrieving groups, collections, and bibliographic items, plus confirmed create, update, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Use an already installed trusted oo CLI where possible, or independently verify the installer source, version, and integrity before running remote installation commands.

Risk: Write and destructive Zotero actions can create, replace, or delete library data.

Mitigation: Confirm the exact action, target library object, payload, version, and expected effect with the user before running any write or destructive action.

Risk: Connector action schemas can change, which may make stale payloads incorrect.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zotero)
- [Zotero Homepage](https://www.zotero.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
