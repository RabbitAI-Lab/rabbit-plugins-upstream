## Description:

Google Docs lets agents search, read, create, export, and edit Google Docs through the OOMOL googledocs connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to work with Google Docs documents from an agent session, including document discovery, content retrieval, document creation, export, and structured edits. It is suited for workflows that need Google Docs operations through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the setup instructions before installing and prefer a verified package or signed release path for the oo CLI.

Risk: Write and destructive actions can modify, overwrite, or remove Google Docs content.

Mitigation: Confirm the target document, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-googledocs)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Docs](https://workspace.google.com/products/docs/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, action names, schema-inspection steps, and confirmation guidance for write or destructive Google Docs operations.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
