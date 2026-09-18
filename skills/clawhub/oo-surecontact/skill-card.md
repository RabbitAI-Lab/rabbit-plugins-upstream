## Description:

SureContact enables an agent to read, create, update, and delete SureContact contacts, lists, and tags through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage SureContact account data from an agent workflow, including contact lookup, list and tag management, and confirmed write or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary notes fallback setup commands that execute a remotely fetched installer directly in a shell.

Mitigation: Review installation steps before use; prefer official, version-pinned installation instructions with checksum or signature verification.

Risk: The skill can perform write and destructive SureContact actions that modify or remove contacts, lists, or tags.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [SureContact skill release](https://clawhub.ai/oomol/skills/oo-surecontact)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SureContact homepage](https://surecontact.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON connector responses from SureContact actions, including data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
