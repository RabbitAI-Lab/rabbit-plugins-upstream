## Description:

Writer lets an agent use an OOMOL-connected Writer account to create non-streaming chat completions and list available Writer models through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask Writer for plain-text chat completions and to inspect available Writer models from an already connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Have the user review the oo CLI installer and prefer a verified manual installation path before any agent uses the CLI.

Risk: Authentication, connection, scope, credential, or billing failures can prevent Writer actions from running.

Mitigation: Run Writer actions only after the user has installed the CLI, signed in, connected Writer, and resolved billing or connection errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-writer)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Writer homepage](https://writer.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before action payloads; chat completion support is non-streaming.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
