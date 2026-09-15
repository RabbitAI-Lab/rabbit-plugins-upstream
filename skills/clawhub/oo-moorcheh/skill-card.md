## Description:

Moorcheh helps agents operate Moorcheh through the OOMOL oo CLI connector for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Moorcheh connector schemas and run Moorcheh read, search, upload, namespace, and document-management actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code on the user's machine.

Mitigation: Do not let an agent run the remote installer inline; install the oo CLI through a verified, user-controlled method and review official installation steps first.

Risk: Moorcheh write and destructive actions can change or delete account data.

Mitigation: Review write and delete payloads carefully, confirm the exact target and effect with the user, and require explicit approval before destructive deletion.

## Reference(s):

- [Moorcheh homepage](https://www.moorcheh.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-moorcheh)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
