## Description:

Operate Zenkit through the OOMOL oo CLI to read, create, update, search, and delete workspace, collection, and entry data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zenkit workspaces and collections from an agent, including listing resources, retrieving details, searching entries, and managing entries after confirmation for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct users to execute a remote installer script in a shell.

Mitigation: Review the installer path before installing and prefer official, verifiable release or package-manager instructions.

Risk: Create, update, and delete actions can change or remove Zenkit data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [Zenkit homepage](https://zenkit.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zenkit skill page](https://clawhub.ai/oomol/skills/oo-zenkit)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zenkit connector responses as JSON when actions are executed.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
