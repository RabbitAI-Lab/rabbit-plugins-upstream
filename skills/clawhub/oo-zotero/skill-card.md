## Description:

Zotero enables agents to read, create, update, and delete Zotero library data through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zotero libraries through an OOMOL-connected account. It supports listing groups, retrieving collections and items, and performing confirmed create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote install scripts that execute directly in the user's shell.

Mitigation: Install the oo CLI only from a verified package or reviewed download path, and avoid piping remote scripts into a shell unless the source has been reviewed.

Risk: Write and destructive Zotero actions can change or remove library data.

Mitigation: Fetch the live action schema, confirm the exact JSON payload and target with the user, and require explicit approval before running write or delete actions.

## Reference(s):

- [ClawHub Zotero skill page](https://clawhub.ai/oomol/skills/oo-zotero)
- [Zotero homepage](https://www.zotero.org)
- [OOMOL oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing connector payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
