## Description:

Linkhut enables an agent to read, create, update, delete, and filter Linkhut bookmarks through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to manage Linkhut bookmarks and tags through OOMOL's Linkhut connector, including reading bookmark data and performing confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Review the installer path before use, prefer verified official installation documentation, and check signatures or checksums where available.

Risk: Bookmark write and delete actions can change Linkhut data.

Mitigation: Confirm the exact payload, target bookmark, and intended effect before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-linkhut)
- [Linkhut Homepage](https://ln.ht)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Linkhut Icon](https://static.oomol.com/logo/third-party/Linkhut.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Linkhut action schemas, JSON command payloads, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
