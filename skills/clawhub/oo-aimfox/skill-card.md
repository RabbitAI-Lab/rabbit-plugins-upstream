## Description:

Aimfox lets agents read, create, update, and delete Aimfox data through OOMOL's oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Aimfox campaigns, leads, labels, and interaction data through an OOMOL-connected account. It supports read workflows and confirmed write or destructive campaign audience changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute scripts directly in a shell.

Mitigation: Use a verified, pinned, or signed oo CLI installation path before installing.

Risk: The skill can run Aimfox write and destructive actions that modify campaign audiences.

Mitigation: Require explicit user confirmation of the target, payload, and effect before running write or destructive actions.

## Reference(s):

- [Aimfox homepage](https://aimfox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect live Aimfox connector schemas and run connector actions.]

## Skill Version(s):

1.0.3 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
