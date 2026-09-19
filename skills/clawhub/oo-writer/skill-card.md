## Description:

Writer (writer.com) lets an agent operate Writer through an OOMOL-connected account for reading, creating, and updating Writer data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Writer connector schemas, run Writer actions through the OOMOL oo CLI, generate non-streaming Writer chat completions, and list available Writer models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute code on a user's machine.

Mitigation: Use an official, versioned oo CLI installer with checksum or signature verification, and review setup steps before granting local execution or account access.

Risk: The skill operates Writer through an OOMOL-connected account and can run write actions.

Mitigation: Install only if the user is comfortable connecting Writer through OOMOL, inspect the live action schema before payload construction, and confirm write or destructive action effects before execution.

## Reference(s):

- [ClawHub Writer skill page](https://clawhub.ai/oomol/skills/oo-writer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Writer homepage](https://writer.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Writer app connection setup](https://console.oomol.com/app-connections?provider=writer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Writer connector schema inspection before constructing action payloads; non-streaming chat completions are produced through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
