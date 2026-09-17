## Description:

Kernel lets an agent manage Kernel browser sessions through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to list, inspect, create, update, and delete Kernel browser sessions through an OOMOL-connected account. It is intended for workflows where the agent should inspect live action schemas before constructing connector payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts directly in a shell.

Mitigation: Review the installer path before installing and prefer a documented package manager, pinned release, checksum, or signature-verified download when available.

Risk: Write actions can create or update Kernel browser session state.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

Risk: The destructive delete action can remove a Kernel browser session.

Mitigation: Confirm the target session and obtain explicit user approval before running destructive deletion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kernel)
- [Kernel Homepage](https://kernel.sh)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before composing connector payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
