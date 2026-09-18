## Description:

Google Docs automation for reading, creating, updating, and deleting documents through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to operate Google Docs through an OOMOL-connected account for document search, retrieval, export, creation, editing, formatting, and deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, or delete Google Docs content.

Mitigation: Confirm the target document, payload, and expected effect before write or destructive actions.

Risk: First-time setup includes remote pipe-to-shell installer commands for the oo CLI.

Mitigation: Avoid pipe-to-shell installation unless the installer source is independently trusted and verified; prefer a pinned, signed, or manually inspected installation path.

Risk: Read, search, and export actions can expose document contents.

Mitigation: Limit requests to user-authorized documents and review returned content for sensitive information before sharing it.

## Reference(s):

- [Google Docs](https://workspace.google.com/products/docs/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Google Docs content, document metadata, exported PDF results, or action confirmations through the oo CLI.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
