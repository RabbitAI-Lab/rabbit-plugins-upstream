## Description:

This skill operates Mem0 through an OOMOL-connected account, allowing agents to read, search, create, update, and delete Mem0 memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage Mem0 memories through an OOMOL-connected account while inspecting live connector schemas before actions run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include piping a remote installer script into a shell.

Mitigation: Use a verified or manual OOMOL CLI installation path and review the installer before execution.

Risk: The skill can add, update, or delete Mem0 memories.

Mitigation: Require explicit user confirmation for write and destructive actions, including the target and payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mem0)
- [Mem0 homepage](https://mem0.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
