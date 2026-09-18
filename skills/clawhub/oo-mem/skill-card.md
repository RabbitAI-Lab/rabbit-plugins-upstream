## Description:

Use Mem (mem.ai) for reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Mem notes through an OOMOL-connected account, including reading, searching, creating, updating, trashing, restoring, and permanently deleting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may use remote installer commands that execute changing external code.

Mitigation: Prefer official installation documentation, reviewed downloads, package-manager installs, and explicit approval before running any setup command.

Risk: Mem note write and destructive actions can change, trash, or permanently delete user data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or destructive operations.

Risk: Mem actions are performed through OOMOL as an intermediary service.

Mitigation: Install only when the user accepts OOMOL-mediated Mem actions and understands that credentials are handled through that connected account flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mem)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Mem homepage](https://mem.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill icon](https://static.oomol.com/logo/third-party/mem.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read results from Mem connector actions and proposals for write or destructive Mem operations that require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
